import random

class Questions:
    def __init__(self, id_question:int):
        self.id_question = id_question
        self.question = ""

    def random_question(self, id_answer: int):
        
        if(id_answer == 1):
            self.question = "What animal can be seen on the Porsche logo?"
        
        return self.question
    


"""class Answers:
    def __init__(self, id_answer: int, choice: int):
        self.id_answer = id_answer
        self.choice= choice

    def answer(self):"""

example=Questions(6)
print(example.random_question(1))


