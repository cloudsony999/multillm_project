from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

def openai_call(question:str):
    llm=ChatOpenAI(model="gpt-4o")
    response=llm.invoke(question)
    print('response: ',response.content)


def ollama_call(question:str):
    llm=ChatOllama(model='llama3.2')
    response=llm.invoke(question)
    print('response: ',response.content)

def gemini_call(question:str):
    llm=ChatGoogleGenerativeAI(model='gemini-flash-lite-latest')
    response=llm.invoke(question)
    print('response: ',response.text)



