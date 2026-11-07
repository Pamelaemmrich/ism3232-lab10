# Bakery Assistant

## Mock assistant: Biscuit

Biscuit is a fictional bakery assistant that informs clients of the "baking" or "ready for pickup" status of a cake order. The orders are imaginary sample data, and their responses are derived from basic Python keyword rules rather than an AI model. Because they deal with money or altering an order, messages that contain the terms "refund," "payment," or "cancel" are forwarded to a human, a virtual assistant shouldn't make those decisions. Anything else receives an appropriate response stating that it is unsure of how to assist. Since nothing verifies who is requesting, anyone who entered another customer's order ID may access the status of that order using actual customer data.

### Model Testing and Design Decisions

During my test, Biscuit correctly answered the question, "When are you open?" by providing the bakery's hours, which worked because the information was included in its instructions. However, when I asked, "Do you sell gluten free bread?" it could not provide an answer and directed me to ask a baker for more details. This showed that the model could answer questions using its provided information but should not guess when it does not know something. I kept the order lookup and refund handoff in the code because these actions require accurate and consistent results every time. Having these tasks handled by code instead of relying on the model helps prevent incorrect order information or mistakes involving refunds.