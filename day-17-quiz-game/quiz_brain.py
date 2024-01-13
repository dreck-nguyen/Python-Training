class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        quest_count = len(self.question_list)
        if self.question_number < quest_count:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_ans = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print()
