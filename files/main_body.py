import menu
from SQL_CONNECT import sql_insert as sqlin
from SQL_CONNECT import sql_output as sqlout
from SQL_CONNECT import retrieve_data
from SQL_CONNECT import sql_close
from PV_methods import course_input as c_i         #implement dummy data , change README file
from PV_methods import rolling
import sys

'''
We dont actually need trainers_board , students_board , assignments_board lists but i left them to remind me
how much i dislike my work for part a!!proceed..
'''

courses_board = []
courses_board = retrieve_data()
trainers_board = []                                     
students_board = []
assignments_board = []
success_message = 'Successfully added\n'                                              
error_message = 'Please give me a valid input\n'                                     
redirection_message = 'The input was invalid.You will be redirected to storage menu'
exiting_program_message = 'You will now exit the program.Waiting for your feedback! '


'''
   According to your choice the programm will run the needed procedures in the input menu.For details check READ BEFORE OPERATE text docuement
'''

def input_menu():

   print('Welcome to the main input menu\n\nHere you will input all the data you need')

   while True:                                                                          
      print('1: Courses\n2: Trainers\n3: Students\n4: Assignments\n5: Output Menu\n6: Exit\n')            
      choice = input('What would you like to choose\n')  
                                                                                             
      if choice == '5':
         print('You will now exit the main input menu and go to output menu\n\n')                             
         output_menu()

      elif choice == "6":
         print("You will now exit the programm")
         sql_close()
         sys.exit()

      elif choice == '1':                                                             
         crs = sqlin(choice)
         courses_board.append(crs)
         print(crs)                                                                                                               
         print(success_message.center(75))  

      elif choice == '2':     
         trnrs,tr_id = sqlin(choice)
         trainers_board.append(trnrs)   #<-- no need
         print(trnrs,'\n',success_message.center(75))
         print('If the trainer is in an active course class\nplease choose one of the following courses :\n')
         print('If not leave it empty:\n')
         c_i('trainerscourses (TrainerID , CourseID)' , tr_id , courses_board) 
         
      elif choice == '3':
         sdnts,st_id = sqlin(choice)
         students_board.append(sdnts)   #<-- no need
         print(sdnts,'\n',success_message.center(75))
         print('If the student is in an active course class\nplease choose one of the following courses :\n')
         print('If not leave it empty:\n')
         c_i('studentscourses (StudentID , CourseID)' , st_id , courses_board)
                  
      elif choice == '4':     
         assgn,as_id = sqlin(choice)
         assignments_board.append(assgn)   #<-- no need
         print(assgn,'\n',success_message.center(75))
         print('If the assignment is in an active course class\nplease choose one of the following courses :\n')
         print('If not leave it empty:\n')
         c_i('assignmentscourses' , as_id , courses_board)
            
      else:     
         print(error_message.center(70))
                        


'''
Same as before according to your choice there will be the expected output
'''                                                                                             

def output_menu():

   print('Welcome to the storage menu\n\nNow you can see all the data and how they relate to each other\n')
   while True:
      print('1: All Courses                 6: All Trainers per Course\n'
         '2: All Trainers                7: All Assignments per Course\n'
         '3: All Students                8: All Assignments per Course per Student\n'   
         '4: All Assignments             9: Students in more than one Courses\n'
         '5: All Students per Course    10: Input Menu\n'             
         '                   11: Exit\n'
         )
      choice = input('What would you like to choose\n')
      if choice == '10':
         print('You will now exit the main input menu and go to input menu\n\n')
         input_menu()

      elif choice == "11":
         print("You will now exit the programm\n")
         sql_close()
         sys.exit()

      elif choice == '1':
         sqlout('allout' , ('courses' ,))
         print()

      elif choice == '2':
         sqlout('allout' , ('trainers',))
         print()

      elif choice == '3':
         sqlout('allout' , ('students',))  
         print() 

      elif choice == '4':
         sqlout('allout' , ('assignments',))
         print()
            
      elif choice == '5':
         rolling(courses_board , 'Students per Course :\n' , 'stdnt_crs')
                         
      elif choice == '6':
         rolling(courses_board , 'Trainers per Course :\n' , 'trnr_crs')
                          
      elif choice == '7':
         rolling(courses_board , 'Assignments per Course :\n' , 'asgn_crs')
                           
      elif choice == '8':
         rolling(courses_board , 'Assignments per Course per Student :\n' , 'assign_per_course_per_student')        
               
      elif choice == '9': 
         print('Students in more than one Courses :\n')
         sqlout('stdnt_more_crs' , ('HI',)) 

      else:     
         print(error_message.center(70),'\n') 

print('\n'*3)
print('-'*10,exiting_program_message,'-'*10)






if __name__ == "__main__" :
   input_menu()

      
         
         
         
         
         
     
         
   
         
         

      
