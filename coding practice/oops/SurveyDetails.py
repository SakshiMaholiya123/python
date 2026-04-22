class Survey:
    def __init__(self,survey_name,ques_number):   # init constructor= special method which runs automatically when an object is created
        self.survey_name=survey_name
        self.ques_number=ques_number

    def __str__(self): # if we create init method so we have to create the str method to get the desired output otherwise it will give 
        return f"Survey name is {self.survey_name} and number of questions available is {self.ques_number}"
    

        
obj=Survey.__init__("impact of ai",3)
print(obj)
