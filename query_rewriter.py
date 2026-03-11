from llm_client import generate


def rewrite_question(question, history):

    prompt = f"""
You are a system that rewrites follow-up questions into standalone questions.

Conversation:
{history}

Question:
{question}

Rewrite the question so it can be understood without the conversation.
Return ONLY the rewritten question.
"""

    rewritten = generate(prompt)

    return rewritten.strip()