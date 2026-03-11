class ConversationMemory:

    def __init__(self, max_turns=10):
        self.history = []
        self.max_turns = max_turns

    def add(self, user, assistant):

        self.history.append({
            "user": user,
            "assistant": assistant
        })

        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_history_text(self):

        text = ""

        for h in self.history:
            text += f"User: {h['user']}\n"
            text += f"Assistant: {h['assistant']}\n"

        return text