from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-proj-xxxxxxxxxxxxxxxxx"
)

prompt = ChatPromptTemplate.from_template("You are an AI Assistant. Answer this: {question}")

chain = prompt | llm

response = chain.invoke({"question": "What is Artificial Intelligence?"})

print("AI Response:", response.content)
