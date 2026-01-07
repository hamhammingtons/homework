import re
import json
import requests
import asyncio
import os
import io
from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands

# Set your token here (or export DISCORD_BOT_TOKEN in your environment)
DISCORD_BOT_TOKEN = ""
# Optional guild id for faster command sync during development (set as env var)
GUILD_ID = os.environ.get("1412040033413894176")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


def extract_user_identifier(target: str) -> dict:
    """Return dict with either 'id' (int) or 'username' (str) parsed from target."""
    target = target.strip()
    # If it's a URL that contains /users/{id}/profile
    m = re.search(r"/users/(\d+)", target)
    if m:
        return {"id": int(m.group(1))}
    # If it's all digits, treat as id
    if target.isdigit():
        return {"id": int(target)}
    # Otherwise treat as username (strip possible URL parts)
    # e.g. https://www.roblox.com/username
    m2 = re.search(r"roblox.com/(?:users/\d+/profile|people/)?([^/?#]+)", target)
    if m2:
        uname = m2.group(1)
        return {"username": uname}
    return {"username": target}


def get_user_by_id(user_id: int) -> Optional[dict]:
    url = f"https://users.roblox.com/v1/users/{user_id}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"network error: {e}"}
    return r.json()


def get_user_by_username(username: str) -> Optional[dict]:
    # Older public endpoint
    url = "https://api.roblox.com/users/get-by-username"
    try:
        r = requests.get(url, params={"username": username}, timeout=10)
        r.raise_for_status()
        data = r.json()
        if data.get("Id"):
            return {"id": data["Id"], "name": data.get("Username")}
    except requests.RequestException:
        # fallback to v1 search below; continue
        pass

    url2 = "https://users.roblox.com/v1/usernames/users"
    try:
        r2 = requests.post(url2, json={"usernames": [username]}, timeout=10)
        r2.raise_for_status()
        data2 = r2.json()
        if data2.get("data"):
            entry = data2["data"][0]
            return {"id": entry.get("id"), "name": entry.get("name")}
    except requests.RequestException as e:
        return {"error": f"network error: {e}"}
    return None


def fetch_groups(user_id: int):
    url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json().get("data", [])
    except requests.RequestException as e:
        return {"error": f"network error: {e}"}


def fetch_friends(user_id: int):
    url = f"https://friends.roblox.com/v1/users/{user_id}/friends"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json().get("data", [])
    except requests.RequestException as e:
        return {"error": f"network error: {e}"}


def fetch_badges(user_id: int):
    url = f"https://badges.roblox.com/v1/users/{user_id}/badges"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json().get("data", [])
    except requests.RequestException as e:
        return {"error": f"network error: {e}"}


def fetch_collectibles(user_id: int, limit: int = 100):
    url = f"https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles"
    params = {"limit": limit}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json().get("data", [])
    except requests.RequestException as e:
        return {"error": f"network error: {e}"}


def inspect_user(target_input: str, sortby: str = "all") -> dict:
    parsed = extract_user_identifier(target_input)
    user_info = None

    # Prefer explicit presence check; parsed is always a dict now
    if parsed.get("id") is not None:
        user = get_user_by_id(parsed["id"])
        if user and user.get("id") is not None:
            user_info = {
                "id": user.get("id"),
                "name": user.get("name")
                or user.get("displayName")
                or user.get("username"),
            }
    else:
        user = get_user_by_username(parsed.get("username"))
        if user and user.get("id") is not None:
            user_info = {
                "id": user.get("id"),
                "name": user.get("name") or user.get("Username"),
            }

    if not user_info:
        # If user fetching returned an error dict, propagate it
        if isinstance(user, dict) and user.get("error"):
            return {"error": user.get("error")}
        return {"error": "User not found"}

    user_id = user_info["id"]
    result = {"user": user_info}

    wants = set([s.strip().lower() for s in (sortby or "all").split(",") if s.strip()])
    if "all" in wants:
        wants = {"groups", "items", "friends", "badges"}

    if "groups" in wants:
        result["groups"] = fetch_groups(user_id)
    if "friends" in wants:
        result["friends"] = fetch_friends(user_id)
    if "badges" in wants:
        result["badges"] = fetch_badges(user_id)
    if "items" in wants or "collectibles" in wants:
        result["items"] = fetch_collectibles(user_id)

    return result


def format_for_humans(data: dict) -> str:
    if data.get("error"):
        return f"Error: {data['error']}"
    u = data.get("user", {})
    parts = [f"User: {u.get('name')} (ID {u.get('id')})"]
    if "groups" in data:
        parts.append(f"Groups: {len(data['groups'])} (showing up to API limit)")
    if "items" in data:
        parts.append(f"Collectibles: {len(data['items'])}")
    if "friends" in data:
        parts.append(f"Friends: {len(data['friends'])}")
    if "badges" in data:
        parts.append(f"Badges: {len(data['badges'])}")
    return "\n".join(parts)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    try:
        if GUILD_ID:
            gid = int(GUILD_ID)
            await client.tree.sync(guild=discord.Object(id=gid))
            print(f"Synced commands to guild {gid}")
        else:
            await client.tree.sync()
            print("Synced global commands (may take up to an hour to appear)")
    except Exception as e:
        print("Command sync failed:", e)


@client.tree.command(
    name="inspect", description="Inspect a Roblox profile by username, id or URL"
)
@app_commands.describe(
    target="Username, profile URL or numeric id",
    sortby="What to fetch (comma-separated)",
    output="Output format",
)
@app_commands.choices(
    sortby=[
        app_commands.Choice(name="all", value="all"),
        app_commands.Choice(name="items", value="items"),
        app_commands.Choice(name="groups", value="groups"),
        app_commands.Choice(name="friends", value="friends"),
        app_commands.Choice(name="badges", value="badges"),
    ],
    output=[
        app_commands.Choice(name="for_humans", value="for_humans"),
        app_commands.Choice(name="json", value="json"),
        app_commands.Choice(name="txt", value="txt"),
    ],
)
async def inspect_slash(
    interaction: discord.Interaction,
    target: str,
    sortby: str = "all",
    output: str = "for_humans",
):
    await interaction.response.defer()
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, inspect_user, target, sortby)

    outtype = (output or "for_humans").lower()
    if outtype == "json":
        payload = json.dumps(data, indent=2, ensure_ascii=False)
        fname = f"inspect_{data.get('user',{}).get('id','unknown')}.json"
        await interaction.followup.send(
            file=discord.File(fp=io.BytesIO(payload.encode("utf-8")), filename=fname)
        )
        return
    if outtype == "txt":
        txt = json.dumps(data, indent=2, ensure_ascii=False)
        fname = f"inspect_{data.get('user',{}).get('id','unknown')}.txt"
        await interaction.followup.send(
            file=discord.File(fp=io.BytesIO(txt.encode("utf-8")), filename=fname)
        )
        return

    human = format_for_humans(data)
    await interaction.followup.send(human)


@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.strip()
    if not content.startswith("/inspect"):
        return

    parts = content.split(maxsplit=3)
    if len(parts) < 2:
        await message.channel.send(
            "Usage: /inspect {url|username|id} {sortby} {output}"
        )
        return

    target = parts[1]
    sortby = parts[2] if len(parts) >= 3 else "all"
    output = parts[3] if len(parts) >= 4 else "for_humans"

    await message.channel.trigger_typing()
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, inspect_user, target, sortby)

    outtype = (output or "for_humans").lower()
    if outtype == "json":
        payload = json.dumps(data, indent=2, ensure_ascii=False)
        fname = f"inspect_{data.get('user',{}).get('id','unknown')}.json"
        await message.channel.send(
            file=discord.File(fp=io.BytesIO(payload.encode("utf-8")), filename=fname)
        )
        return
    elif outtype == "txt":
        txt = json.dumps(data, indent=2, ensure_ascii=False)
        fname = f"inspect_{data.get('user',{}).get('id','unknown')}.txt"
        await message.channel.send(
            file=discord.File(fp=io.BytesIO(txt.encode("utf-8")), filename=fname)
        )
        return
    else:
        human = format_for_humans(data)
        await message.channel.send(human)


if __name__ == "__main__":
    # Allow overriding via env var if desired
    token = os.environ.get("DISCORD_BOT_TOKEN", DISCORD_BOT_TOKEN)
    if not token or token.startswith("YOUR_"):
        print("Please set DISCORD_BOT_TOKEN in the file or env var DISCORD_BOT_TOKEN.")
    else:
        client.run(token)
