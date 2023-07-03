from data import questions_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

questions_bank = []
for question in questions_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
