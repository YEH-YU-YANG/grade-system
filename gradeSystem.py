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
        Input new student ID, name, and grades. 
        If the student ID doesn't exist in the database, the function adds the student's name and grades into the database.
        
        :param: None
        :return: None

        Running Example:
        
        >>>> object.add_student()
        new student ID: 55688
        new student NAME: Ale
        new student GRADEs: lab1 70 
        
        Student added successfully:
            ID: 55688
            Name: Ale
            Grades: 
            lab1: 70
            lab2: 0
            lab3: 0
            mid_term: 0
            final_exam: 0
            
        >>>> object.add_student()
        new student ID: 111
        new student NAME: Dyla
        new student GRADEs: lab1 70 lab2 80 lab3 90 mid_term 100 final_exam 90   
        
        Student added successfully:
            ID: 111
            Name: Dyla
            Grades: 
            lab1: 70
            lab2: 80
            lab3: 90
            mid_term: 100
            final_exam: 90
            
        >>>> object.add_student()
        new student ID: 7777
        new student NAME: Rend
        new student GRADEs: final_exam 60 mid_term 80 lab3 70 lab2 60 lab1 55 
        
        Student added successfully:
            ID: 7777
            Name: Rend
            Grades: 
            lab1: 55
            lab2: 60
            lab3: 70
            mid_term: 80
            final_exam: 60
            
        >>>> object.add_student() # when providing already exist ID
        new student ID: 7777
        print("Student already exists.")
        """
        id = input("\nPlease enter the new student's ID: ")
        if id not in self.student:
            name = input("\nPlease enter the new student's NAME: ")
            self.student[id] = { 
                "name": name,
                "scores":{"lab1": 0,"lab2": 0,"lab3": 0,"mid_term": 0,"final_exam": 0} 
            }         
            grades_str = input("\nPlease enter the new student's grades, formatted as test1 grade1 test2 grade2 ...: ")
            grades_list = grades_str.strip().split()
            grades_json = self.list_to_json(grades_list)
            for test, grade in grades_json.items():
                self.student[id]['scores'][test] = int(grade)
            self.display_data_with_prefix(prefix_str='Grades', print_grades=True, print_name=True, print_id=True, student_id=id)
        else:
            print("Student already exists.")
    
    def update_grade(self):
        """
        Update a student's specific grade.
        i.e., Provide "ID, updated information", and make the update.
        
        :param: None
        :return: None
        
        Running Example:
        
        >>>> object.update_grade() # when providing invalid ID
        Please enter id: 1234 
        invalid input ! Please enter new ID again !
        
        >>>> object.update_grade() # when providing correct format
        Please enter id: 955002056 
        Old grades: lab1 88 lab2 92 lab3 88 mid_term 98 final_exam 91
        Please enter new grades: lab1 80
        New grades: lab1 80 lab2 92 lab3 88 mid_term 98 final_exam 91
        
        >>>> object.update_grade() # when providing correct format in random order
        Please enter id: 955002056 
        Old grades: lab1 88 lab2 92 lab3 88 mid_term 98 final_exam 91
        Please enter new grades: final_exam 100 lab1 70 lab3 22
        New grades: lab1 70 lab2 92 lab3 22 mid_term 98 final_exam 100
        """
        
        id = input('\n'+"Please enter id: ");
        if id in self.student:
            self.display_data_with_prefix('Old grades',print_grades=True,student_id=id)
            new_grades_str = input("\nPlease enter new grades: ");
            new_grades_list = new_grades_str.strip().split()
            new_grades_json = self.list_to_json(new_grades_list)
            for test, grade in new_grades_json.items():
                if grade.isdigit():
                    self.student[id]['scores'][test] = int(grade)
            self.display_data_with_prefix('New grades',print_grades=True,student_id=id)         
        else:
            print("Invalid input ! Please enter new ID again !")
            
        
    def display_data_with_prefix(self, prefix_str="", print_weight=False, print_grades=False, print_name=False, print_id=False, student_id=None):
        """
        Print weights or grades with a specified prefix string.

        :param prefix_str: The prefix string to be displayed before the weights or grades.
        :type prefix_str: str
        
        :param print_weight: Whether to print weights or not. Defaults to False.
        :type print_weight: bool, optional
        
        :param print_grades: Whether to print grades or not. Defaults to False.
        :type print_grades: bool, optional
        
        :param student_id: The ID of the student whose grades are to be printed. Defaults to None.
        :type student_id: str, optional

        Running Example:
        
        >>>> object.display_data_with_prefix('Old weights', print_weight=True)
        Old weights: lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4

        >>>> object.display_data_with_prefix('New weights', print_weight=True)
        New weights: lab1 0.5 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0

        >>>> object.display_data_with_prefix('Old Grades', print_grades=True, student_id='123')
        New grades: lab1 70 lab2 80 lab3 80 mid_term 80 final_exam 80
        
        >>>> object.display_data_with_prefix('New Grades', print_grades=True, student_id='123')
        New grades: lab1 90 lab2 80 lab3 80 mid_term 80 final_exam 80
        
        """
        print('')
        if print_id:  
            print(f'ID: {student_id}')
        if print_name:
            student_name = self.student[student_id]['name']  
            print(f'Student: {student_name}')
        if len(prefix_str) >= 1:
            print(f'{prefix_str}:', end=' ')
        if print_weight:
            print(' '.join([f'{key} {value}' for key, value in self.weights.items()]))
        if print_grades and student_id in self.student:
            student_scores = self.student[student_id]['scores']
            print(' '.join([f'{key} {int(value)}' for key, value in student_scores.items()]))
        
    def valid_weights(self, weights):
        """
        Validates whether the provided weights are valid or not.
        
        :param new_weights: A dictionary containing test names as keys and their corresponding weights as values.
        :type new_weighs: JSON
        
        :return: A boolean indicating whether the weights are valid (True) or not (False).
        :rtype: bool
        
        Example: 
        
        default_weights = {
            'lab1': 0.1,      
            'lab2': 0.1,      
            'lab3': 0.1,      
            'mid_term': 0.3,  
            'final_exam': 0.4,
        }
        
        >>> new_weights = {"lab1": 0.2, "lab2": 0} 
        >>> object.valid_weights(new_weights)
        True
        
        >>> new_weights = {"lab1": 0.2} 
        >>> object.valid_weights(new_weights)
        False
        
        """
        is_valid = True
        for test, weight in weights.items():
            weights[test] = weight
        total_weight = sum(weights.values())
        if not total_weight == 1:
            is_valid =  False   

        return is_valid
    
    def format_weights_value(self, weights):
        """
        Converting percentages/decimals to floats if necessary.
        
        :param weights: A JSON object containing weights.
        :type weights: JSON
        
        "return new_weights" A JSON object with formatted(float) weights.
        :rtype new_weights: JSON
        
        Example:
        
        weights = {
            "test1": "50%",
            "test2": "0.75",
            "test3": "35"
        }
        >>>> new_weights = format_weights_value(weights)
        new_weights = {
            "test1": 0.5,
            "test2": 0.75,
            "test3": 0.35
        }
        """
        
        new_weights = self.weights.copy()
        for test, weight in weights.items():
            if '%' in weight:
                weight = float(weight.strip('%')) / 100
            elif 1 <= float(weight) and float(weight) <=100:
                weight = float(weight) / 100
            else:
                weight = float(weight)
            new_weights[test] = weight
        return new_weights
    
    def list_to_json(self, list):
        """
        Convert a list to a JSON.
        
        :param weights_list: A list containing test names and values.
                             For example: ["test1", "value1", "test2", "value2", ...]
        :type weights_list: List
        
        :return weights_json:  A JSON-formatted dictionary containing test names as keys and corresponding values.
        :rtype weights_json: dict
        """
        json = {}
        for i in range(0, len(list), 2):
            test = list[i]
            value = list[i+1]
            json[test] = value
        return json
    
    def update_weights(self):
        """
        This method prompts the user to input new weights for the grading system. 
        If the provided weights are valid, they are updated; otherwise, no changes are made.
        
        :param: None
        :type: None
        
        :return: None
        :rtype: None
        
        Running Example:
        
        >>>> object.update_weights() ; # when providing float input
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        Please enter new weights: lab1 0.2 lab2 0
        New weights: : lab1 0.2 lab2 0.0 lab3 0.1 mid_term 0.3 final_exam 0.4
        
        >>>> object.update_weights() ; # when providing decimal input
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        Please enter new weights: lab1 20 lab2 0
        New weights: : lab1 0.2 lab2 0.0 lab3 0.1 mid_term 0.3 final_exam 0.4
        
        >>>> object.update_weights() ; # # when providing percentage input
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        Please enter new weights: lab1 20% lab2 0
        New weights: : lab1 0.2 lab2 0.0 lab3 0.1 mid_term 0.3 final_exam 0.4
        
        >>>> object.update_weights() ; # when providing invalid input
        Old weights: : lab1 0.1 lab2 0.1 lab3 0.1 mid_term 0.3 final_exam 0.4
        Please enter new weights: lab1 0.3
        Invalid input ! Please enter new weights again !
        """
        self.display_data_with_prefix('Old weights',print_weight=True)
        new_weights_str = input("\nPlease enter new weights: ");  
        new_weights_list = new_weights_str.strip().split()
        new_weights_json = self.list_to_json(new_weights_list)
        new_weights_json = self.format_weights_value(new_weights_json)
        if self.valid_weights(weights=new_weights_json):
            for test, weight in new_weights_json.items():
                self.weights[test] = float(weight)
            self.display_data_with_prefix('New weights',print_weight=True)         
        else:
            print("Invalid input ! Please enter new weights again !")
              
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
            elif user_input == '7': self.add_student()
            elif user_input == '8': self.update_grade(); 
            elif user_input == '9': self.update_weights(); 
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
            student_id, student_name, lab1, lab2, lab3, mid_term, final_exam = data[0], data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6])
            self.student[student_id] = {
                "name": student_name,
                "scores":{                    
                    "lab1": lab1,
                    "lab2": lab2,
                    "lab3": lab3,
                    "mid_term": mid_term,
                    "final_exam": final_exam,
                } 
            }
            
        
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

    
        