from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain


question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'] , question["answer"]))
    
quizz = QuizzBrain(question_bank)



while quizz.stil_has_question():
    quizz.next_question()
    
print("You hace completed the quizz")
print(f"Your final score was: {quizz.score} / {quizz.quetion_number}")    