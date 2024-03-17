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

import statistics as stat
import numpy as np

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
        
        self.weights = {
            'lab1': 0.1,
            'lab2': 0.1,
            'lab3': 0.1,
            'mid_term': 0.3,
            'final_exam': 0.4,   
        }

        
    def show_score(self):
        """
        Display all grades of the student (five scores).
        i.e., Provide "ID" and display "the five scores".
        
        :param : None
        :type : None
        
        :return: None
        :rtype: None
        
        Running Example:
        >>> object.show_score()
        Please enter student id: 12345
        Student's scores:
        +--------------+-------+
        |    Subject   | Score |
        +--------------+-------+
        |     Lab 1    |   90   |
        |     Lab 2    |   85   |
        |     Lab 3    |   92   |
        |   Mid-Term   |   88   |
        |  Final Exam  |   95   |
        +--------------+-------+
        """
        
        user_input = input("Please enter student id: ")
        
        student_data = self.student.get(user_input)
    
        # Check if the student exists
        if student_data:
            student_score = student_data['scores']
            # Extract individual scores
            lab1, lab2, lab3, mid_term, final_exam = student_score
            
            # Print the student's scores in a table format
            print("Student's scores:")
            print("+--------------+-------+")
            print("|    Subject   | Score |")
            print("+--------------+-------+")
            print(f"|     Lab 1    |   {int(lab1)}   |")
            print(f"|     Lab 2    |   {int(lab2)}   |")
            print(f"|     Lab 3    |   {int(lab3)}   |")
            print(f"|   Mid-Term   |   {int(mid_term)}   |")
            print(f"|  Final Exam  |   {int(final_exam)}   |")
            print("+--------------+-------+")
        else:
            print("Student ID not found.")
    
    def score_to_grad_letter(self, score):
        """    
        Display the grade level of the student (e.g., A-).
        i.e., Provide "ID" and display "the grade level".
        
        :param : score
        :type : int
        
        :return: grade_letter
        :rtype: int
        
        Running Example:
        """
        
        if   score >= 90: grade_letter = 'A+'
        elif score >= 85: grade_letter = 'A '
        elif score >= 80: grade_letter = 'A-'
        elif score >= 77: grade_letter = 'B+'
        elif score >= 73: grade_letter = 'B '
        elif score >= 70: grade_letter = 'B-'
        elif score >= 67: grade_letter = 'C+'
        elif score >= 63: grade_letter = 'C '
        elif score >= 60: grade_letter = 'C-'
        elif score >= 50: grade_letter = 'D '
        else: grade_letter = 'E '
        
        return grade_letter
    
    def show_grade_letter(self):
        """    
        Display the grade level of the student (e.g., A-).
        i.e., Provide "ID" and display "the grade level".
        
        :param : None
        :type : None
        
        :return: None
        :rtype: None
        
        Running Example:
        """
        
        user_input = input("Please enter student id: ")
        student_data = self.student.get(user_input)
    
        # Check if the student exists
        if student_data:
            student_score = student_data['scores']
            # Extract individual scores
            lab1, lab2, lab3, mid_term, final_exam = [self.score_to_grad_letter(score) for score in student_score]
            
            # Print the student's scores in a table format
            print("Student's scores:")
            print("+--------------+-------+")
            print("|    Subject   | Score |")
            print("+--------------+-------+")
            print(f"|     Lab 1    |   {lab1}  |")
            print(f"|     Lab 2    |   {lab2}  |")
            print(f"|     Lab 3    |   {lab3}  |")
            print(f"|   Mid-Term   |   {mid_term}  |")
            print(f"|  Final Exam  |   {final_exam}  |")
            print("+--------------+-------+")
        else:
            print("Student ID not found.")

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
        
        user_input = input("Please enter student id: ")
        student_data = self.student.get(user_input)
        weights = self.weights.values()
        # Check if the student exists
        if student_data:
            student_scores = student_data['scores']     
            weighted_score = []
            for student_score, weight in zip(student_scores, weights):
                weighted_score.append(student_score * weight)
            mean_score = sum(weighted_score)
            print(f"Student's average scores: {mean_score:.2f}")
        else:
            print("Student ID not found.")

        
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
    def print_weights(self,prefix_str):
        """
        Print the weights along with a specified prefix string.

        :param prefix_str: The prefix string to be displayed before the weights.
        :type prefix_str: str

        :return: None
        :rtype: None

        Running Example:
        >>>> object.print_weights('Old weights')
        Old weights: lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4

        >>>> object.print_weights('New weights')
        New weights: lab1 0.2 lab2 0.1 lab3 0.5 mid_term 0.3 final_exam 0.33
        """
        if len(prefix_str) >= 1:
            print(f'{prefix_str}:', end=' ')
        print(' '.join([f'{key} {value}' for key, value in self.weights.items()]))
    
    def update_weights(self, new_weights_str):
        """
        Update the weighting of the grading system.

        :param new_weights_str: A string representing the new weights for various tests.
                                Format: "test1 weight1 test2 weight2 ..."
                                Example: "lab1 20% mid_term 10 final_exam 50%"
        :type new_weights_str: str
        
        :return: None
        :rtype: None
        
        Running Example:
        
        >>>> object.update_weights("lab1 20%")
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        New weights: : lab1 0.2 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        
        >>>> object.update_weights("lab1 20")
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        New weights: : lab1 0.2 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        
        >>>> object.update_weights("lab1 0.2")
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        New weights: : lab1 0.2 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        
        >>>> object.update_weights("lab1 0.2 mid_term 10 final_exam 50%")
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        New weights: : lab1 0.2 lab2 0.1 lab3 0.1 mid_term 0.1 final_exam 0.5
        
        >>>> object.update_weights("mid_term 10 lab1 0.2 final_exam 35% lab2 25")
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        New weights: : lab1 0.2 lab2 0.25 lab3 0.1 mid_term 0.1 final_exam 0.35
        """
        self.print_weights('Old weights: ')            
        new_weights_list = new_weights_str.split()
        for i in range(0, len(new_weights_list), 2):
            test = new_weights_list[i]
            weight = new_weights_list[i+1]
            if '%' in weight:
                weight = float(weight.strip('%')) / 100
            elif 1 <= float(weight) and float(weight) <=100:
                weight = float(weight) / 100
            else:
                weight = float(weight)
            self.weights[test] = weight
        self.print_weights('New weights: ')            
        
    def show_menu(self):
        """
        This function prints out the menu options available for the grading system.
        Users can select from these options to perform various functions related to grading,
        as well as to exit the system.

        :param: None
        :type: None

        :return: None
        :rtype: None

        Running Example: None
        """
        print("")
        print("Function Menu")
        print("1) Show grade ")
        print("2) Show grade letter") 
        print("3) Show average")
        print("4) Show rank")
        print("5) Show distribution")
        print("6) Filtering")
        print("7) Add student")
        print("8) Update grade")
        print("9) Update weights")
        print("10) Exit")
        print("")
        
    def function_menu_and_exit(self):
        """
        Menu options for the grading system and exit functionality.
        Allows users to select various functions and exit the system.
        
        :param: None
        :type: None
        
        :return: None
        :rtype: None
        
        Running Example:
        
        >>> object.function_menu_and_exit()  # Some information will be displayed below
        
        Welcome to the Grade System.

        Function Menu
        1) Show grade 
        2) Show grade letter
        3) Show average
        4) Show rank
        5) Show distribution
        6) Filtering
        7) Add student
        8) Update grade
        9) Update weights
        10) Exit

        Please enter a command (1-10) to begin :
        """
        print("Welcome to the Grade System.") 
        while True:
            self.show_menu()
            user_input = input("Please enter a command (1-10) to begin: ")
            if   user_input == '1': self.show_score()
            elif user_input == '2': self.show_grade_letter()
            elif user_input == '3': self.show_average()
            elif user_input == '4': self.show_rank()
            elif user_input == '5': self.show_distribution()
            elif user_input == '6': user_input = input('\n'+"Please enter a score: ");            self.filtering(user_input)
            elif user_input == '7': user_input = input('\n'+"Please enter new student's data: "); self.add_student(user_input)
            elif user_input == '8': user_input = input('\n'+"Please enter id and new grade: ");   self.update_grade(user_input); 
            elif user_input == '9': user_input = input('\n'+"Please enter new weights: ");        self.update_weights(user_input); 
            else : 
                print("Exit, see you next time.")
                break
                
    
    def load_input_data(self):
        """
        Function to load input data required for the grading system.
        And store them in self.student in json.

        :param : None
        :returns : None
        """
        with open('input.txt', 'r', encoding='utf-8') as file:
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

    
        