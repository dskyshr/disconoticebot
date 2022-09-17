# disconoticebot
 
"disconoticebot" is a bot to notify message a text-channel when someone enter or exit to voice-channels on discord.


# DEMO

 
# Features
 
 
# Requirement
 
* Python 3.5 ~
 
Environments under Pipenv for Windows is tested.


# Installation

For example,
```bash
pip install discord.py
```

First of all, you have to create a dedicated bot on Discord Debeloper Portal.
2nd, turn all "Privileged Gateway Intents" on.
3nd, grant the bot authorities of 'View Audit Log', 'Read messages/View Channels', 'View Server Insight', 'Send massages'.
Last, access the URL for inviting your server.


# Usage
 
```bash
clone [URL of this repository ]
cd disconoticebot
cp mylib/config.py.origin mylib/config.py
vim mylib/config.py
(Save your Bot's token, channel-id to notify, channel-ids to monitor.)
py disconoticebot.py
```

If you don't know these channel ids, try
```bash
py discochannles.py
```


# Note
 
I did not test environments under Linux and Mac.


# Author
 
* dskyshr
* Keio univ, faculty of economics


# License
 
This software is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
