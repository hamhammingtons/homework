import discord  # type: ignore
from discord import app_commands  # type: ignore
import requests  # type: ignore
import json
import re
import io
from urllib.parse import urljoin
import matplotlib.pyplot as plt  # type: ignore
import matplotlib  # type: ignore

matplotlib.use("Agg")  # Use non-interactive backend

# --- SETTINGS ---
# REMINDER: Reset this token in the Discord Dev Portal since it was posted publicly!
BOT_TOKEN = "enter yo token here if you want"


class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")


client = MyBot()


def generate_bar_chart(data, max_bars=10):
    """Generate ASCII bar chart from numerical data."""
    lines = []
    if isinstance(data, (list, tuple)):
        items = list(enumerate(data))
    elif isinstance(data, dict):
        items = list(data.items())
    else:
        return "No numerical data found."

    # Filter numeric items
    numeric_items = [(k, v) for k, v in items if isinstance(v, (int, float))]
    if not numeric_items:
        return "No numerical values found."

    numeric_items = numeric_items[:max_bars]
    if not numeric_items:
        return "No numerical values found."

    max_val = max(v for _, v in numeric_items) or 1

    for key, val in numeric_items:
        bar_len = int((val / max_val) * 20) if max_val > 0 else 0
        bar = "█" * bar_len
        lines.append(f"{str(key)[:15]:15} {bar:20} {val}")

    return "```\n" + "\n".join(lines) + "\n```"


def generate_embed_from_json(data, title="Data"):
    """Generate a Discord embed from JSON data."""
    embed = discord.Embed(title=title, color=discord.Color.blue())

    if isinstance(data, dict):
        for key, value in list(data.items())[:25]:  # Discord embed limit
            if isinstance(value, (list, dict)):
                val_str = json.dumps(value)[:100] + (
                    "..." if len(json.dumps(value)) > 100 else ""
                )
            else:
                val_str = str(value)[:100]
            embed.add_field(name=key, value=val_str or "N/A", inline=False)
    else:
        embed.description = json.dumps(data, indent=2)[:1024]

    return embed


def generate_graph_image(data):
    """Generate a high-quality graph image (PNG) from numerical data, including nested structures."""
    try:
        # Recursively extract all numerical values with labels
        def extract_numbers(obj, prefix=""):
            """Recursively extract numerical values and their paths."""
            results = []

            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_prefix = f"{prefix}.{key}" if prefix else key
                    if isinstance(value, (int, float)):
                        results.append((new_prefix, value))
                    elif isinstance(value, (dict, list)):
                        results.extend(extract_numbers(value, new_prefix))
            elif isinstance(obj, (list, tuple)):
                for idx, item in enumerate(obj):
                    new_prefix = f"{prefix}[{idx}]"
                    if isinstance(item, (int, float)):
                        results.append((new_prefix, item))
                    elif isinstance(item, (dict, list)):
                        results.extend(extract_numbers(item, new_prefix))

            return results

        items = extract_numbers(data)
        if not items:
            return None

        # Limit to 15 items for readability
        items = items[:15]
        labels = [label for label, _ in items]
        values = [val for _, val in items]

        plt.clf()
        fig, ax = plt.subplots(figsize=(12, 6))

        # Create bar chart
        ax.bar(labels, values, color="steelblue", edgecolor="navy", alpha=0.7)
        ax.set_ylabel("Values", fontsize=12)
        ax.set_xlabel("Keys", fontsize=12)
        ax.set_title("Data Visualization", fontsize=14, fontweight="bold")
        ax.grid(axis="y", alpha=0.3)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        # Save to BytesIO buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=100, bbox_inches="tight")
        buf.seek(0)
        plt.close(fig)

        return buf
    except Exception as e:
        print(f"Graph generation error: {e}")
        return None


@client.tree.command(
    name="view", description="View JSON data (raw, visualized, translator, or renderer)"
)
@app_commands.describe(
    website="Example: httpbin.org/get or jsonplaceholder.typicode.com/posts/1",
    mode="Display mode: raw (default), visualized (ASCII), translator (embed), or renderer (PNG graph)",
)
@app_commands.choices(
    mode=[
        app_commands.Choice(name="raw", value="raw"),
        app_commands.Choice(name="visualized", value="visualized"),
        app_commands.Choice(name="translator", value="translator"),
        app_commands.Choice(name="renderer", value="renderer"),
    ]
)
async def view(interaction: discord.Interaction, website: str, mode: str = "raw"):
    await interaction.response.defer()

    url = (
        website if website.startswith(("http://", "https://")) else f"https://{website}"
    )

    # This header makes the website think you are a real Chrome browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        # 1. Request the main URL
        response = requests.get(url, headers=headers, timeout=5)

        def is_json(resp):
            return (
                "application/json" in (resp.headers.get("Content-Type") or "").lower()
            )

        def discover_api_candidates(html, base_url, max_candidates=12):
            candidates = []
            seen = set()

            # 1) JSON-LD script blocks may contain URLs
            for block in re.findall(
                r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                html,
                re.I | re.S,
            ):
                try:
                    doc = json.loads(block.strip())
                    if isinstance(doc, dict):
                        for key in ("@id", "url", "sameAs"):
                            v = doc.get(key)
                            if isinstance(v, str):
                                u = urljoin(base_url, v)
                                if u not in seen:
                                    seen.add(u)
                                    candidates.append(u)
                except Exception:
                    pass

            # 2) href/src links
            for u in re.findall(r'(?:href|src)=["\']([^"\']+)["\']', html, re.I):
                full = urljoin(base_url, u)
                if full not in seen:
                    seen.add(full)
                    candidates.append(full)

            # 3) fetch/XHR and xhr.open patterns in inline scripts
            for u in re.findall(r'fetch\(\s*["\']([^"\']+)["\']', html, re.I):
                full = urljoin(base_url, u)
                if full not in seen:
                    seen.add(full)
                    candidates.append(full)
            for u in re.findall(
                r'open\(\s*["\'](?:GET|POST)["\']\s*,\s*["\']([^"\']+)["\']', html, re.I
            ):
                full = urljoin(base_url, u)
                if full not in seen:
                    seen.add(full)
                    candidates.append(full)

            # 4) Common API endpoints derived from the base URL
            common_paths = [
                "/api",
                "/api/v1",
                "/wp-json/wp/v2",
                "/graphql",
                "/api.json",
                "/index.json",
                "/search.json",
            ]
            for p in common_paths:
                u = urljoin(base_url, p)
                if u not in seen:
                    seen.add(u)
                    candidates.append(u)

            # 5) Prioritize likely JSON endpoints (contain keywords or end with .json)
            def score(u):
                u_l = u.lower()
                s = 0
                if any(
                    k in u_l
                    for k in ("api", "json", "graphql", "wp-json", "posts", "data")
                ):
                    s -= 1
                if u_l.endswith(".json"):
                    s -= 2
                return s

            candidates = sorted(candidates, key=score)
            return candidates[:max_candidates]

        parsed = None

        # 2. If the main response claims to be JSON, try parsing it
        if is_json(response):
            try:
                parsed = response.json()
            except (ValueError, json.JSONDecodeError):
                parsed = None

        # 3. If not parsed yet, try the /api fallback
        if parsed is None:
            api_url = f"{url.rstrip('/')}/api"
            try:
                res = requests.get(api_url, headers=headers, timeout=3)
                if is_json(res):
                    try:
                        parsed = res.json()
                        response = res
                    except (ValueError, json.JSONDecodeError):
                        parsed = None
            except Exception:
                pass

        # 4. As a last resort, try to parse the original response body even if headers lied
        if parsed is None:
            try:
                parsed = response.json()
            except (ValueError, json.JSONDecodeError):
                parsed = None

        # 5. If still nothing, try to discover API endpoints from the HTML/body
        if parsed is None:
            try:
                html_text = response.text if hasattr(response, "text") else ""
                candidates = discover_api_candidates(html_text, url)
                for cand in candidates:
                    try:
                        r2 = requests.get(cand, headers=headers, timeout=4)
                        if is_json(r2):
                            try:
                                parsed = r2.json()
                                response = r2
                                break
                            except (ValueError, json.JSONDecodeError):
                                parsed = None
                        else:
                            # try to parse even if headers lied
                            try:
                                parsed = r2.json()
                                response = r2
                                break
                            except Exception:
                                parsed = None
                    except Exception:
                        continue
            except Exception:
                pass

        if parsed is None:
            await interaction.followup.send(
                "❌ Error: Could not find valid JSON. (Make sure the URL points to an API or JSON file)"
            )
            return

        raw_data = parsed

        # Handle three display modes
        if mode == "visualized":
            chart = generate_bar_chart(parsed)
            if len(chart) > 1900:
                fp = io.BytesIO(chart.encode("utf-8"))
                fp.seek(0)
                await interaction.followup.send(
                    "📊 Visualized Data (attached due to size):",
                    file=discord.File(fp, filename="chart.txt"),
                )
            else:
                await interaction.followup.send(f"📊 Visualized Data:\n{chart}")

        elif mode == "translator":
            try:
                title = url.split("/")[-1][:50] or "Data"
                embed = generate_embed_from_json(parsed, title=title)
                await interaction.followup.send(embed=embed)
            except Exception as e:
                print(f"Embed error: {e}")
                await interaction.followup.send("❌ Error: Could not generate embed.")

        elif mode == "renderer":
            graph_buf = generate_graph_image(parsed)
            if graph_buf:
                await interaction.followup.send(
                    "📈 Graph Visualization:",
                    file=discord.File(graph_buf, filename="graph.png"),
                )
            else:
                await interaction.followup.send(
                    "❌ Error: Could not generate graph (no numerical data found)."
                )

        else:  # mode == "raw" (default)
            formatted_json = json.dumps(raw_data, indent=4)

            # If the JSON is too large for a Discord message, send it as a .txt attachment
            if len(formatted_json) > 1900:
                fp = io.BytesIO(formatted_json.encode("utf-8"))
                fp.seek(0)
                filename = "data.txt"
                await interaction.followup.send(
                    "success: raw json data extracted; attached as a .txt file",
                    file=discord.File(fp, filename=filename),
                )
            else:
                await interaction.followup.send(
                    f"success: raw json data extracted;\n```json\n{formatted_json}\n```"
                )

    except Exception as e:
        # We print 'e' to the console so you can see the exact error
        print(f"Error occurred: {e}")
        await interaction.followup.send(
            "❌ Error: Could not find valid JSON. (Make sure the URL points to an API or JSON file)"
        )


client.run(BOT_TOKEN)
