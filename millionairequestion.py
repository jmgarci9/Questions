import random

class Questions:
    def __init__(self, id_question:int):
        self.id_question = id_question
        self.question = ""

    def random_question(self, id_answer: int):
        
        if(id_answer == 1):
            self.question = "What animal can be seen on the Porsche logo?"
        
        return self.question
    

class AnswerChoices:
    def __init__(self, options: int):
        self.id_options = {1: ["a) horse", "b) tiger", "c) eagle", "d) bull"]}
        self.options = options
        
        
        
    def get_choices(self):
        if (self.options == self.id_options[1]):
            for choices in self.id_options[1]:
                print (choices)

#The number key in the dicationry is relative to the questions in the class questions.
"""class Choice:
    def __init__(self, choice: int):
        self id_answer = {1: "a"}
        self.choice= choice
        
        if (choice == id_answer[1])"""
            
        
    



example1 = AnswerChoices(1)
example1.get_choices

