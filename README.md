# mega-bot
## Setup
You'll need .env with your discord token to run bot:
```
$ echo DISCORD_TOKEN = your_discord_token > .env
```
Neccessary modules:
- requests
- python_dotenv
- discord.py
```bash
$ pip3 install requests python_dotenv discord.py
```
## Run
You can run bot by:
```
$ python3 main.py
```
However I suggest running bot in detached docker container like so:
```bash
$ docker build -t mega-bot .
$ docker run -d --restart="always" --name mega-bot mega-bot
```
## Usage
Commands which bot supports:
```
!mega - lists top 3 coverages
!setmega *args - picks coverage from list of pokémon (space seperated) and lists them as a confirmation
!setdefault - sets coverage to default one and lists them as a confirmation
```
note: both !setmega and !setdefault require administrator permissions.
