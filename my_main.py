# my_main.py
# Author: Pamela Emmrich

from my_assistant import BakeryAssistant
from my_tool import BakeryLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Biscuit, a helpful assistant for a small neighborhood bakery.
Answer in one short sentence.
The bakery is open 7 am to 3 pm, Tuesday to Sunday, and closed on Monday.
Custom cakes need 48 hours notice.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to a baker."""

ORDERS = {
    "B100": "baking",
    "B101": "ready for pickup",
    "B102": "delivered",
}

tool = BakeryLookup(ORDERS)
model = OllamaModel(MODEL_NAME)
bot = BakeryAssistant("Biscuit", INSTRUCTIONS, tool, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
