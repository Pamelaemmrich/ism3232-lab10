# two_bots.py
# Author: Pamela Emmrich

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
stock_tool = StockLookup({"rain jacket": 12})

sunny = SupportChatbot("Sunny", "You are cheerful and brief.", order_tool, stock_tool)
river = SupportChatbot("River", "You are formal and detailed.", order_tool, stock_tool)

first_sunny_reply = sunny.respond("hello")
sunny.respond("Where is order A100?")
first_river_reply = river.respond("hello")

print(sunny.name, len(sunny.history))
print(river.name, len(river.history))
print(first_sunny_reply)
print(first_river_reply)
print(sunny.instructions)
print(river.instructions)
