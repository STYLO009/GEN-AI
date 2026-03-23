from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
model = ChatGroq(model = 'openai/gpt-oss-120b')

invoke = input("Enter what you want to ask : ")
response = model.invoke(invoke)

print(response.content)