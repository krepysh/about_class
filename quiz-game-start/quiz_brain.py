
class quizBrain:
    def __init__(self, question_data):
        self.question_data = question_data
        self.question_number = 0
        self.question_correct = 0

    def correctQuestion(self):
        self.question_correct += 1

    def nextQuestion(self):
        self.question_number += 1

    def answercheck(self):
        for question in self.question_data:

            self.question = question.text
            user_input = input(f"True or False: {self.question} \n").lower()
            self.answer = question.answer.lower()
            if user_input == self.answer.lower():
                self.correctQuestion()
                self.nextQuestion()
                print("Correct!")
            else:
                self.nextQuestion()
                print("Incorrect!")

            print(f"{self.question_correct}/{self.question_number} correct")


