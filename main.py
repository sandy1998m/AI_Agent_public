from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from tools import tool_playsound, tool_stt, tool_persons
import os
from dotenv import load_dotenv
load_dotenv()

# keyfile = open("Key.txt", "r")
# key = keyfile.readline()
key = os.getenv("API_KEY")
model = "gpt-3.5-turbo"

# 設定 Model 和 Tools
Model = ChatOpenAI(
    model = model,
    openai_api_key = key
)
Tools = [tool_playsound, tool_stt, tool_persons]

# 設定 prompt
prompt = ChatPromptTemplate.from_messages(
	[
		("system", "You are a helpful assistant"),
		("human", "{input}"),
		MessagesPlaceholder(variable_name = "agent_scratchpad") # 存放及插入執行過程
	]
)

# 建立agent
agent = create_openai_functions_agent(
	llm = Model,
	prompt = prompt,
	tools = Tools,
)

# 設定執行 Agent
agent_executor = AgentExecutor(
	agent = agent,
	tools = Tools,
	# verbose = True # print
)

while True:
	user_input = str(input("使用者輸入(輸入停止即結束):"))

	if user_input == "停止":
		break
	else:
		response = agent_executor.invoke({"input": user_input})
