
# ServerBuster, A minecraft server finder

This is a tool designed to find servers, and to verify the servers if they have whitelist enabled
## Features

- ✅ SHODAN powered searching
- ✅ Server Bruteforcing
- ✅ Whitelist Bot Verifier
- ✅ Discord Webhook Integration
- ✅ Easily Usable





## Installation

[1] Click the green "Code" button and press "Download zip"

![Download Zip](https://cdn.discordapp.com/attachments/589298703056240662/1068040534259671100/image.png)

[2] Drag and unzip the folder to anywhere on your pc

[3] Open the folder and edit the "config.ini" with notepad and put your credentials in like this

![Config.json](https://cdn.discordapp.com/attachments/589298703056240662/1068041994015875142/image.png)

[3] Open CMD at the location of the folder, you can do this by going to the root folder in file explorer, pressing alt + d and typing cmd then pressing enter. Do this 2 times.

[4] Install the node packages, by doing "npm i"

[5] Then run the commands found below

## How to use

#### ShodanSearch

```
python main.py shodansearch -o -v -s
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-o [--output]` | `string` | Output File name |
| `-v [--version]` | `string` | **Required** Version of minecraft to scan for |
| `-s [--additional-search]` | `string` | any additional search queries, e.g. "smp" |

#### whitelistchecker

```
  python main.py whitelistchecker -f
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `-f [filename]`      | `string` | **Required**. Input File name|



Todo List


- [ ]  Proxy support
- [ ]  multiple accounts
- [ ]  plugin finders

## Tech Stack

**Client:** Javascript, Python


## Authors

- [@taylordawson911](https://github.com/taylordawson911)

