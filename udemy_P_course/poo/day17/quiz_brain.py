class QuizzBrain():
    def __init__(self , question_list):
        self.quetion_number = 0
        self.question_list = question_list
        self.score = 0
        
    
    def stil_has_question(self):
        return self.quetion_number < len(self.question_list)
       
       
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it")
            print(f"Current score {self.score}/ {self.quetion_number + 1}")
            print("\n")
        else:
            print("You Wrong")
            print(f"Current score {self.score}/ {self.quetion_number + 1}")
            print("\n")
            exit    
                        
    def next_question(self):
        current_question = self.quetion_number
        user_aswer = input(f"Q{current_question + 1}: " + self.question_list[self.quetion_number].text + ". (True/False)? :")
        correct_answer = self.question_list[self.quetion_number].answer
        self.check_answer(user_aswer, correct_answer)
        self.quetion_number += 1
        
   
            