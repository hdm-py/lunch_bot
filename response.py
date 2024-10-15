from bs4 import BeautifulSoup
import requests
from datetime import datetime
from discord.ext import commands 

def fetch_lunch_menu(dag: str) -> list:
    # URL of the lunch menu page
    url = "https://61an.gastrogate.com/dagens-lunch/"
    response = requests.get(url)  # Send a GET request to the URL

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        days = soup.find_all("h3")  # Find all headings for the days of the week

        menu = {}
        for day in days:
            day_name = day.text.strip()  # Get the name of the day

            # Find the dishes for the corresponding day
            dishes = day.find_next("tbody").find_all("td", class_="td_title")

            # Extract dish names and store them in a list
            list_dish = [dish.text.strip() for dish in dishes]

            # Store the day's name and its corresponding dishes in the menu dictionary
            menu[day_name] = list_dish

        # List of valid weekdays in Swedish
        days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]

        menu_items = {}

        # Organize menu items by day
        for key, value in menu.items():
            for day in days:
                if day in key:  # Match the day from the menu with the valid weekdays
                    menu_items.update({day: value})

    try:  
        if dag == "Today":
            today = datetime.today()  # Get today's date
            # Check if today is a weekday (not Saturday or Sunday)
            if today.weekday() not in (5, 6): 
                return menu_items[days[today.weekday()]]  # Return today's menu
            else:
                return None  # No menu available for weekends
        else:
            return menu_items[dag]  # Return the menu for the specified day
    except KeyError:
        return ["Ingen meny tillgänglig för den dagen."]  # Return error if day not found
    except commands.CommandNotFound:
        return None  # Handle command not found error
    except Exception:
        return None  # Catch-all for other exceptions
