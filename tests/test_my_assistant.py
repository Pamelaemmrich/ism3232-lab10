from mock_model import MockModel
from my_assistant import BakeryAssistant
from my_tool import BakeryLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_assistant():
    """Build a fresh assistant with its own tool and a mock model for each test."""
    orders = {"B100": "baking", "B101": "ready for pickup"}
    return BakeryAssistant("Biscuit", "Be friendly.", BakeryLookup(orders), MockModel())


def make_assistant_with_silent_model():
    """Build an assistant whose model never answers."""
    orders = {"B100": "baking", "B101": "ready for pickup"}
    return BakeryAssistant(
        "Biscuit", "Be friendly.", BakeryLookup(orders), SilentModel()
    )


def test_tool_finds_known_status():
    tool = BakeryLookup({"B100": "baking"})
    assert tool.find_status("B100") == "baking"


def test_tool_returns_none_for_unknown_order():
    tool = BakeryLookup({"B100": "baking"})
    assert tool.find_status("B999") is None


def test_order_question_uses_the_tool():
    bot = make_assistant()
    assert bot.respond("Where is order B101?") == "Order B101 is ready for pickup."


def test_unknown_request_goes_to_the_model():
    bot = make_assistant()
    assert "not sure" in bot.respond("Do you sell gluten free bread?")


def test_order_question_without_an_id_asks_for_one():
    bot = make_assistant()
    assert "order ID" in bot.respond("Where is my order?")


def test_refund_goes_to_a_person():
    bot = make_assistant()
    assert "baker" in bot.respond("I want a refund")


def test_respond_records_both_messages():
    bot = make_assistant()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_safe_reply_when_the_model_has_no_answer():
    bot = make_assistant_with_silent_model()
    assert "try again" in bot.respond("Do you sell gluten free bread?")


def test_order_rule_does_not_need_the_model():
    bot = make_assistant_with_silent_model()
    assert bot.respond("Where is order B101?") == "Order B101 is ready for pickup."


def test_handoff_rule_does_not_need_the_model():
    bot = make_assistant_with_silent_model()
    assert "baker" in bot.respond("I want a refund")
