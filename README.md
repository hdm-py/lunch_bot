# Karolinska Daily Lunch Bot

This is a Discord bot that fetches the daily lunch menu from the [61an Gastrogate Website](https://61an.gastrogate.com/dagens-lunch/) and provides it in a Discord server through various commands.

## Hackathon 2024 Participation

This project was developed as part of a Hackathon (light-version) held at Nackademin, on 2024-10-14. It was a collaborative effort to create a Discord bot that scrapes and displays daily lunch menus from Sodexo's Restaurant 61:an at Karolinska University Hospital.

## Features

- **Fetch lunch menus for each weekday**:
  - `!monday` - Get Monday's lunch menu.
  - `!tuesday` - Get Tuesday's lunch menu.
  - `!wednesday` - Get Wednesday's lunch menu.
  - `!thursday` - Get Thursday's lunch menu.
  - `!friday` - Get Friday's lunch menu.
  - `!today` - Get today's lunch menu.
- **Admin Commands**:
  - `!shutdown` - Shuts down the bot (admin only).
  - `!restart` - Restarts the bot (admin only).
- **Easy setup**: Uses environment variables to keep your bot token secure.
- **Web scraping**: Uses BeautifulSoup to scrape lunch menu data from [61an Gastrogate](https://61an.gastrogate.com/dagens-lunch/).

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.7+
- [Discord Developer Portal](https://discord.com/developers/applications) account to create a bot and obtain your bot token.

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hdm-py/lunch_bot
   cd lunch_bot


2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/Scripts/activate 
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root of the project and add your Discord bot token:

   ```bash
   DISCORD_TOKEN=your_discord_bot_token
   ```

5. **Run the bot:**
   ```bash
   python main.py
   ```

## Commands

The bot responds to the following commands:

| Command      | Description                          |
| ------------ | ------------------------------------ |
| `!monday`    | Fetches Monday's lunch menu.        |
| `!tuesday`   | Fetches Tuesday's lunch menu.       |
| `!wednesday` | Fetches Wednesday's lunch menu.     |
| `!thursday`  | Fetches Thursday's lunch menu.      |
| `!friday`    | Fetches Friday's lunch menu.        |
| `!today`     | Fetches today's lunch menu.         |
| `!shutdown`  | Shuts down the bot (admin only).    |
| `!restart`   | Restarts the bot (admin only).      |


## How it works

The bot scrapes the lunch menu from [61an Gastrogate](https://61an.gastrogate.com/dagens-lunch/) using the BeautifulSoup library. It fetches the menu data for each day and responds in Discord when the respective command is used.

### Example

# Example usage of the bot:

!monday

# Returns Monday's lunch menu with the correct date.

!today

# Returns today's lunch menu.

## Restaurant Information

**Restaurang 61:an**

- **Address**: Karolinska Universitetssjukhuset, Plan 6, C161, 141 86 Stockholm
- **Phone**: 08-58580046
- **Website**: [61an.sodexo.se](https://61an.sodexo.se)

**Opening Hours**:

- Weekdays: 10:30 - 14:00
- Café Bakery: 09:00 - 14:00

## Files

- `main.py`: Contains the bot logic and command handling.
- `response.py`: Responsible for fetching and processing the lunch menu via web scraping.

## Dependencies

- [discord.py](https://github.com/Rapptz/discord.py) - A Python wrapper for the Discord API.
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - A library to extract data from HTML and XML files.
- [requests](https://pypi.org/project/requests/) - A simple HTTP library for Python.

## Contributors

This project was created by:

- [Alfred](https://github.com/ajmueller0625) - Co-Founder: Contributed to the development, design, and implementation of functionalities for the Discord bot, including web scraping and integration of the restaurant menu.
- [Haidar](https://github.com/hdm-py) - Co-Founder: Contributed to the development, design, and implementation of functionalities for the Discord bot, including web scraping and integration of the restaurant menu.
- [Robert](https://github.com/LeonByte) - Co-Founder: Contributed to the development, design, and implementation of functionalities for the Discord bot, including web scraping and integration of the restaurant menu.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
