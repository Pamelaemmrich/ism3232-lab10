from my_assistant import BakeryAssistant
from my_tool import BakeryLookup


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    orders = {"B100": "baking", "B101": "ready for pickup"}
    return BakeryAssistant("Biscuit", BakeryLookup(orders))


def test_tool_finds_known_status():
    tool = BakeryLookup({"B100": "baking"})
    assert tool.find_status("B100") == "baking"


def test_tool_returns_none_for_unknown_order():
    tool = BakeryLookup({"B100": "baking"})
    assert tool.find_status("B999") is None


def test_order_question_uses_the_tool():
    bot = make_assistant()
    assert bot.respond("Where is order B101?") == "Order B101 is ready for pickup."


def test_order_question_without_an_id_asks_for_one():
    bot = make_assistant()
    assert "order ID" in bot.respond("Where is my order?")


def test_refund_goes_to_a_person():
    bot = make_assistant()
    assert "baker" in bot.respond("I want a refund")


def test_unknown_request_gets_a_safe_reply():
    bot = make_assistant()
    assert "not sure" in bot.respond("Do you sell gluten free bread?")


def test_respond_records_both_messages():
    bot = make_assistant()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
