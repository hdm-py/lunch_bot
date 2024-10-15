from os import getenv
from dotenv import load_dotenv
from discord import Intents, Message, Embed
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timedelta
import response
import os
import sys

class BotContainer:
    def __init__(self, bot_token) -> None:
        # Initialize the bot with the provided token
        self.bot_token = bot_token

    def run(self):
        # Set up intents for the bot
        intents = Intents.default()
        intents.message_content = True
        bot = Bot(command_prefix="!", intents=intents, help_command=None, case_insensitive=True)

        @bot.event
        async def on_ready():
            # Print a message when the bot is ready
            print(f"{bot.user} is ready")

            # Loop through all guilds (servers) the bot is in
            for guild in bot.guilds:
                # Loop through all text channels in the guild
                for channel in guild.text_channels:
                    # Check if the bot has permission to send messages in the channel
                    if channel.permissions_for(guild.me).send_messages:
                        await channel.send("Hello, how can I assist you today? Please type !help to see the available commands.")
                        break

        @bot.event
        async def on_message(message: Message):
            # Ignore messages from the bot itself
            if message.author == bot.user:
                return
            # Process commands and handle errors
            if message.content.startswith("!"):
                command_name = message.content.split(" ")[0][1:]
                try:
                    if command_name in bot.all_commands:
                    # Attempt to process the command recevied in the message
                        await bot.process_commands(message)
                    else:
                    # If the command is not found, send a message indicating it doesn't exist
                        await message.channel.send("This command does not exist, please try again.")
                except KeyError:
                    # Handle any errors that may occur while fetching data
                    await message.channel.send("An error occurred while fetching the menu.")
            else:
                await bot.process_commands(message)

        def get_date_for_day(day_name: str) -> str:
            # Get the date for the specified day of the week
            today = datetime.now()
            days_of_week = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
            target_day_idx = days_of_week.index(day_name)

            delta = target_day_idx - today.weekday()
            if delta < 0:
                delta += 7

            target_date = today + timedelta(days=delta)
            return target_date.strftime("%Y-%m-%d") 

        def create_embed(day: str, menu: list):
            # Create an embed message for Discord with the lunch menu
            date_for_day = get_date_for_day(day)
            description = "\n".join(menu) if menu else "No menu available for today."

            embed = Embed(title=f"{day}s lunch meny ({date_for_day})", description=description, color=0x00ff00)
            embed.set_footer(text="Restaurang 61:an - Karolinska")
            return embed

        @bot.command()
        async def monday(ctx):
            # Command to fetch Monday's lunch menu
            menu = response.fetch_lunch_menu("Måndag")
            embed = create_embed("Måndag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def tuesday(ctx):
            # Command to fetch Tuesday's lunch menu
            menu = response.fetch_lunch_menu("Tisdag")
            embed = create_embed("Tisdag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def wednesday(ctx):
            # Command to fetch Wednesday's lunch menu
            menu = response.fetch_lunch_menu("Onsdag")
            embed = create_embed("Onsdag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def thursday(ctx):
            # Command to fetch Thursday's lunch menu
            menu = response.fetch_lunch_menu("Torsdag")
            embed = create_embed("Torsdag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def friday(ctx):
            # Command to fetch Friday's lunch menu
            menu = response.fetch_lunch_menu("Fredag")
            embed = create_embed("Fredag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def today(ctx):
            # Command to fetch today's lunch menu
            menu = response.fetch_lunch_menu("Today")
            if menu:
                day = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"][datetime.today().weekday()]
                embed = create_embed(day, menu)
            else:
                embed = create_embed("Today", ["No menu available for today."])
            await ctx.send(embed=embed)

        @bot.command()
        async def help(ctx):
            help_message = (
        "Here are the available commands:\n"
        "- **!monday**: Get Monday's lunch menu.\n"
        "- **!tuesday**: Get Tuesday's lunch menu.\n"
        "- **!wednesday**: Get Wednesday's lunch menu.\n"
        "- **!thursday**: Get Thursday's lunch menu.\n"
        "- **!friday**: Get Friday's lunch menu.\n"
        "- **!today**: Get today's lunch menu.\n"
        "- **!help**: Get help with using the bot.\n"
        "- **!restart**: Restart the bot (Admin only).\n"
        "- **!shutdown**: Shut down the bot (Admin only)."
        )
            await ctx.send(help_message)

        @bot.command()
        @commands.has_permissions(administrator=True)
        async def shutdown(ctx):
            # Command to shut down the bot
            await ctx.send("Shutting down... Have a great day!")
            await bot.close()

        @bot.command()
        @commands.has_permissions(administrator=True)
        async def restart(ctx):
            # Command to restart the bot
            await ctx.send("Restarting...")
            os.execv(sys.executable, ['python'] + sys.argv)
        
        bot.run(self.bot_token)

if __name__ == "__main__":
    load_dotenv()
    bot_token = getenv("DISCORD_TOKEN")
    if bot_token:
        bot = BotContainer(bot_token)
        bot.run()
    else:
        print("Bot token not found.")