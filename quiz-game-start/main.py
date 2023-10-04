from quiz_brain import quizBrain
from data import question_data
from question_model import Question
from cool_quiz import CoolQuizBrain

question_list = []

input_choice = input("Do you want to play normal or fun game? ('normal' / 'fun') \n").lower()

if input_choice == "normal":
    for el in question_data:
        question = Question(el["text"], el["answer"])
        question_list.append(question)

    quiz_brain = quizBrain(question_list)

    print(quiz_brain.answercheck())
else:
    cool_quiz = CoolQuizBrain()
    print(cool_quiz.answercheck())


