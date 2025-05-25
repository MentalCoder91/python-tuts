class Question:
    text = ''
    answer = ''

    def __init__(self, text: str, answer: str):
        self.question = text
        self.correct_answer = answer

    def print_obj(self):
        print(self.question + " " + str(self.correct_answer))
