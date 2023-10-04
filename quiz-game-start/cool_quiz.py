import requests
import html


url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"

class CoolQuizBrain:
    def __init__(self):
        result = requests.get(url)

        self.question_data = result.json()
        self.current_question_index = 0
        self.questions = self.question_data["results"]
        self.category = self.questions[self.current_question_index]["category"]
        self.question = self.questions[self.current_question_index]["question"]
        self.answer = self.questions[self.current_question_index]["correct_answer"]

        self.question_number = 0
        self.question_correct = 0

    def correctQuestion(self):
        self.question_correct += 1

    def nextQuestion(self):
        self.question_number += 1

    def answercheck(self):
        

        for el in self.questions:
            self.question = el["question"]
            self.answer = el["correct_answer"]

            self.decoded_sentence = html.unescape(self.question)

            user_input = input(f"True or False: {self.decoded_sentence} \n").lower()
            if user_input == self.answer.lower():
                self.correctQuestion()
                self.nextQuestion()
                print("Correct!")
            else:
                self.nextQuestion()
                print("Incorrect!")

            print(f"{self.question_correct}/{self.question_number} correct")


