class QuizBrain:

    def __init__(self, ques_ls):
        self.question_number = 0
        self.question_list = ques_ls
        self.score = 0

    def next_question(self):
        next_ques = self.question_list[self.question_number]
        self.question_number += 1
        next_answer = input(str(f"Q.{self.question_number} {next_ques.question}. (True/False)? "))
        self.check_answer(next_answer, next_ques.correct_answer)

    def still_has_questions(self):
        return self.question_number <= len(self.question_list) - 1

    def check_answer(self, user_answer, correct_ans):
        if user_answer.lower() == correct_ans.lower():
            print("You got it right....!!!!")
            self.score += 1
        else:
            print("That's wrong....!!!!")

        print(f"Your score is {self.score}/{self.question_number}")
        print(f"The correct answer is {correct_ans}")
        print("\n")

        if self.still_has_questions():
            pass
        else:
            print(f"Your final score is :{self.score}/{self.question_number}")
