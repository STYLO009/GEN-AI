from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

invoke = input("Enter what you want to ask : ")
response = model.invoke(invoke)

print(response.content)