from SQL_CONNECT import sql_multi_insert as sqlmi
from SQL_CONNECT import sql_output as sqlout
from datetime import date

'''
For details check README 
'''
error_message = 'Invalid input.Data NOT stored'
error_message2 = 'Please give me a valid input' 
error_message3 = 'You must input an integer' 
success_message = 'Successfully added\n'
course = []

#--------------------------------------------------------------------------------------------------------------------------------------

def rolling(courses_board , print_message , procedure_name):
    roll = 0
    
    for crs in courses_board:
        roll += 1
        print(roll,': ' + crs.course_title) 

    s_t_a_choice = input('Please choose the Course according to the NUMBER above\n')
    print(print_message)

    if not s_t_a_choice:
        print(error_message.center(75),'\n')
    else:
        for i in range(1 , roll + 1):
            if s_t_a_choice == str(i):
                sqlout(procedure_name , (courses_board[i - 1].course_title,))

  

#---------------------------------------------------------------------------------------------------------------------------------------        


def course_input(table , element_id , courses_board):
    sub_categories = ["python" , "java" , "javascript" , "c#"]
    yes_no = '1'
    course = []
    fees = []
    subject = []
    course.clear()       
    fees.clear()
    subject.clear()        
       
    while yes_no == '1':
        sub_roll = 0
        roll = 0
        for crs in courses_board:
            roll += 1
            print(roll,': ' + crs.course_title)     
        c_choice = input('Please input the right number for the specific course\nIf number is out of range it wont be stored\n')
        if not c_choice:
            print(error_message.center(75),'\n')
        
        
        elif c_choice:
            if table == 'studentscourses (StudentID , CourseID)':
                while True:
                    try:
                        fees_choice = int(input('Please input the amount of tuition fees\n'))
                        fees.append(fees_choice) 
                        break
                    except ValueError:
                        print(error_message3.center(75))

                for i in range(1 , roll + 1):
                    if c_choice == str(i):
                        course.append(courses_board[i - 1].course_title)


            elif table == "trainerscourses (TrainerID , CourseID)":
                for sub in sub_categories :
                    sub_roll += 1
                    print(sub_roll,": " + sub)
                while True :

                    subj = int(input("Please input the subject"))
                    if subj < 1 and subj > 4 :
                        print(error_message2)
                    elif subj >= 1 and subj <= 4 :
                        subject.append(sub_categories[subj - 1])
                        break
                    else:
                        print(error_message3)

                for i in range(1 , roll + 1):
                    if c_choice == str(i):
                        course.append(courses_board[i - 1].course_title)

            else:                                                                 
                for i in range(1 , roll + 1):                                       
                    if c_choice == str(i):                                         
                        course.append(courses_board[i - 1].course_title)            
                                                                                    
                                                                                    
              
        while True:  
            print('Is there another active course?\n')
            yes_no = input('1: YES\n2: NO\n')
            print()
            if yes_no == '1':
                break
            elif yes_no == '2':
                print((success_message.center(75)),'\n')
                break
            else:
                print(error_message2.center(75) , '\n')
    else:
        
        new_subject = subject
        new_course = course    
        new_fees = fees
        sqlmi(table , element_id , tuple(new_course) ,tuple(new_fees) ,  tuple(new_subject))   #<-- , tuple(new_subject)
       
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
