from llm_client import ask_llm

def test_llm():

    prompt = "Explain what GraphRAG is in one sentence."

    answer = ask_llm(prompt)

    print("LLM Response:")
    print(answer)


if __name__ == "__main__":
    test_llm()