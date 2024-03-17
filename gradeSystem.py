"""
Docstring for Every Method:

1.  Description: 說明此 function 的功能

2.  :param : 說明各個 parameters 的作用，一個 function 可寫多個 @param
    :type  : 說明各個 parameters 的型態

3.  :return : 簡述 return value 的作用
    :rtype  : 說明各 return parameters 的 type

4.  Running Example : 舉例說明如何使用此 function
    
    Running Example:
    >>> find_maximum([3, 7, 2, 9, 5])
    9
    
"""

import pandas as pd

class ScoreSystem:
    
    def __init__(self):
        """        
        Constructor for the GradingSystem class.
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """
        self.student = {}

        
    def show_score(self):
        """
        Display all grades of the student (five scores).
        i.e., Provide "ID" and display "the five scores".
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    
    def show_grade_letter(self):
        """    
        Display the grade level of the student (e.g., A-).
        i.e., Provide "ID" and display "the grade level".
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """


    def show_average(self):
        """
        Display the student's weighted average grade.
        i.e., Provide "ID" and display "their weighted average score".
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """    

        
    def show_rank(self):
        """
        Display the student's ranking (based on weighted average).
        i.e., Provide "ID" and display "their rank".
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    
    def show_distribution(self): 
        """    
        Display the number of students in each grade range (weighted).
        Grade ranges: 
            A+ (90-100), A (85-89), A- (80-84), 
            B+ (77-79), B (73-76), B- (70-72), 
            C+ (67-69), C (63-66), C- (60-62), 
            D (50-59), 
            E (1-49)
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    
    def filtering(self):
        """
        Display information of students with scores greater than or equal to a certain score.
        i.e., Provide "score", and display "their information".
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    
    def add_student(self):
        """
        Add new student grade information.
        i.e., Provide "new information", and add it.
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    
    def update_grade(self):
        """
        Update a student's specific grade.
        i.e., Provide "ID, updated information", and make the update.
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    
    def update_weights(self):
        """
        Update the weighting of the grading system.
        i.e., Provide "updated weighting", and make the update.
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    def function_menu_and_exit(self):
        """
        The menu of functions for the grading system & Exit system.
        i.e., Ability to select the above functions and exit the system.
        
        :param :
        :type :
        
        :return:
        :rtype:
        
        Running Example:
        """

    

    def load_input_data(self):
        """
        Function to load input data required for the grading system.
        And store them in self.student in json.

        :param : None
        :returns : None
        """
        with open('input.txt', 'r') as file:
            txt_content = file.read()
        
        lines = txt_content.split('\n')
        
        for line in lines:
            data = line.split(' ')
            if(len(data) <= 1) :continue
            student_id = data[0]
            student_name = data[1]
            scores = list(map(float, data[2:]))
            self.student.update({f"{student_id}" : {"name": student_name, "scores": scores}})
            
        
    def run(self):
        """
        Main function to run the grading system.

        :param : None
        :returns : None
        """
        
        self.load_input_data()
        self.function_menu_and_exit()
        
        

if __name__ == "__main__":
    
    system = ScoreSystem()
    system.run()

    
        