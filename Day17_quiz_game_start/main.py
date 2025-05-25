from quiz_brain import QuizBrain
from question_model import Question
from data import question_data



question_bank = []


def create_question_bank():
    for question in question_data:
        question_bank.append(Question(question['question'], question['correct_answer']))
    return question_bank

create_question_bank()

q_brain = QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()


