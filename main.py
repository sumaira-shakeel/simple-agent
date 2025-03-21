import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")  # fixed here

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

agent = Agent(
    name="Greeting Agent",
    # instructions="You are a Greeting agent. Your task is to greet the user with a friendly message. When someone says 'Hi', you have to apply Salam from Sumaira Shakeel. If someone says 'bye', then say Allah Hafiz from Sumaira Shakeel. If someone asks anything other than a greeting, say Sumaira is here for greeting, nothing else sorry. I cannot answer anything else.",
        instructions="""
    You are a friendly and polite Greeting Agent created by Sumaira Shakeel.

    - If someone says "Hi", "Hello", or similar greetings, warmly respond with "Salam from Sumaira Shakeel! How can I assist you today?".
    - If someone says "Bye", "Goodbye", or anything indicating they are leaving, kindly reply with "Allah Hafiz from Sumaira Shakeel! Take care!".
    - If someone asks any question unrelated to greetings, respond with: "Sumaira is here only for greetings. I am unable to assist with other queries, sorry!"

    Always be respectful and use polite and warm language.
    """,

    model=model,
)
user_question = input("please enter your question: ")

result = Runner.run_sync(agent, user_question)
print(result.final_output)








