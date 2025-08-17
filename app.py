from langchain_openai import ChatOpenAI


def main():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key="sk-harish7212"
    )

    questions = [
        "What is Artificial Intelligence?",
        "Explain Machine Learning in simple words.",
        "Difference between AI, ML, and Deep Learning?",
        "Real-world applications of AI in daily life?"
    ]

    print("=" * 60)
    print(" 🤖 AI Question Answer Demo using LangChain + OpenAI ")
    print("=" * 60)

    for i, question in enumerate(questions, start=1):
        try:
            answer = llm.invoke(question)

            print(f"\nQuestion {i}: {question}")
            print("-" * 60)
            print(f"Answer:\n{answer.content}")
            print("-" * 60)

        except Exception as e:
            print(f"❌ Error while processing Question {i}: {e}")

    print("\n✅ Demo Completed Successfully!")


if __name__ == "__main__":
    main()
