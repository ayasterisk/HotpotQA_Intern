from hybrid_retrieval import hybrid_retrieve
from llm_client import generate
from conversation_memory import ConversationMemory
from query_rewriter import rewrite_question


memory = ConversationMemory()


def answer_question(question):

    # lấy lịch sử
    history = memory.get_history_text()

    # rewrite câu hỏi
    standalone_question = rewrite_question(question, history)

    # retrieval
    docs = hybrid_retrieve(standalone_question, k=10)

    context = "\n\n".join([d["text"] for d in docs])

    prompt = f"""
You are a helpful assistant.

Context:
{context}

Question:
{standalone_question}

Answer based only on the context.
"""

    answer = generate(prompt)

    # lưu history
    memory.add(question, answer)

    return answer