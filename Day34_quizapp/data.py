
import requests

from Day34_quizapp.question_model import Question

question_bank = []

def get_questions():

    params = {
        "amount": "10",
        "type": "boolean"
    }
    response = requests.get("https://opentdb.com/api.php", params =  params)
    questions = response.json()['results']
    for question in questions:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

get_questions()
