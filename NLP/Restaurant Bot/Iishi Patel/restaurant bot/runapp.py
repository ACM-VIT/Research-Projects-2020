
# from rasa_core.agent import Agent
# from rasa_core.utils import EndpointConfig
# from rasa_core.interpreter import RasaNLUInterpreter

# agent = Agent.load('models/dialogue',interpreter=RasaNLUInterpreter('./models/nlu/default/restaurantbot/'),
#         action_endpoint=EndpointConfig(url="http://127.0.0.1:5055/webhook"))
# print("Bot is ready to talk! Start conversation with 'hi'")
# while True:
#     st = input()
#     if st == 'stop':
#         break
#     responses = agent.handle_text(st)
#     for response in responses:
#         print(response["text"])        

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

from bot_server_channel import BotServerInputChannel


def load_agent():
	nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantbot/')
	action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
	agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)
	return agent

def main_server():
    agent = load_agent()

    channel = BotServerInputChannel(agent, port=5005)
    agent.handle_channels([channel], http_port=5005)

main_server()