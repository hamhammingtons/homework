# Roblox Inspect Discord Bot (Python)

Usage:

- Set your bot token in `DISCORD_BOT_TOKEN` at the top of `inspect_bot.py` or export `DISCORD_BOT_TOKEN` as an environment variable.
- Install requirements:

```
pip install -r requirements.txt
```

- Run the bot:

```
python inspect_bot.py
```

Command format in Discord (message):

```
/inspect {url_or_username_or_id} {sortby} {output}
```

Examples:

- `/inspect Builderman all for_humans`
- `/inspect 1 items json`
- `/inspect https://www.roblox.com/users/12345/profile groups txt`

Supported `sortby` options: `all`, `items` (collectibles), `groups`, `friends`, `badges`. Multiple can be comma-separated.
Supported `output`: `json`, `txt`, `for_humans` (easy readable summary).

Notes:

- This uses public Roblox endpoints; rate limits may apply.
- Keep your bot token secret.
this is for my homwoerk and self-made projects not related to it-step

also i am sure that this will never be useful however if you would like to check it out uhhh feel free to
