***A simple example of Discord bot on Python***

**Installation** 

Let's install package to work with Discord.

```python -m pip install discord.py```

Also we need package Requests to link weather info with bot.

```python -m pip install requests```

**Setting up token**

To link our bot and discord, we need special token. We can get it on https://discord.com/developers . Here we crate a new application. In setting we choose "Bot" and reset token, this token we copy and paste in code (variable "token").
Recommended to turn on "Privileged Gateway Intents" all three parameter. (Bot could not work with them). Choose permissions and done!
