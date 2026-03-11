from qa_service import answer_question

questions = [

    # A. Simple QA
    "Who directed the film Creed?",
    "Who is John Aaron?",

    # B. Retrieval test
    "What film stars Jim Carrey as Andy Kaufman?",

    # C. Multi-hop test
    "Which movie directed by Ryan Coogler is part of the Rocky series?"

]

for q in questions:
    print("\n==============================")
    print("Question:", q)

    answer = answer_question(q)

    print("Answer:", answer)