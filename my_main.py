# my_main.py
# Author: Pamela Emmrich

from my_assistant import BakeryAssistant
from my_tool import BakeryLookup

ORDERS = {
    "B100": "baking",
    "B101": "ready for pickup",
    "B102": "delivered",
}

tool = BakeryLookup(ORDERS)
bot = BakeryAssistant("Biscuit", tool)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
