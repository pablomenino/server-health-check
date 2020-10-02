<h3 align="center">server-health-check</h3>
<p align="center">server-health-check is a Server Status & Health Check in Linux scrtip for Linux, developed in Python.</p>

<p align="center">
<img src="https://img.shields.io/github/release/pablomenino/server-health-check.svg">
<img src="https://img.shields.io/github/license/pablomenino/server-health-check.svg">
</p>

## Table of contents

* [How to Use](#how-to-use)

## <a name="how-to-use">How to Use

#### Usage

Configure hostsnames on server-health-check.py:

```
# --------------------------------------------------------------------- #
# Define allowed hostname to run
HOST_ERIC = "eric-ws"
HOST_NORC = "norc"
HOST_XPS = "xps13"
```

Configure WebHook URL in discord configuration file:

```
[discord_webhook]
norc = WEBHOOK_URL
xps13 = WEBHOOK_URL
eric = WEBHOOK_URL
```

**Execute script**

```bash
# ./server-health-check.py
```

**Example: message recived on Discord.**

![ScreenShot](https://raw.githubusercontent.com/pablomenino/server-health-check/master/images/discord.png)
