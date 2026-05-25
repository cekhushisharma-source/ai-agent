class InterrogatorAgent:

 def ask_questions(self, suspect_name, evidence):

    questions = []

    questions.append(
            f"Where were you during the crime?"
        )

    questions.append(
            f"How do you explain this evidence: {evidence}"
        )

    questions.append(
            "Can anyone verify your alibi?"
        )

return questions