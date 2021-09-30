from datetime import date
from CA_class import Course
from PV_methods2 import getdate

'''
For details check README 
'''

error_message = 'Please give me a valid input\n'
error_message2 = 'You must give an integer\n'

class Person:
   
   '''Super class Person.This is the parent Class for Student and Trainer.'''
   
   def __init__(self,name,surname):
      self.name = name
      self.surname = surname
      
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          

class Student(Person):
   
   '''Subclass Student IS A Child Class of Person Class.'''
   
   form = {'name' : 'First name\n' , 'surname' : 'Last name\n' , 'birthdate' : 'Date of birth\n'}  
           

   count = 0
   
   def __init__(self , name , surname , birthdate):
      super().__init__(name,surname) 
      Student.count += 1                                      
      self.birthdate = birthdate
      self.email = str(Student.count) + self.name + '.' + self.surname + '@private_school.org'
     

   int_fees = ('birthdate' ,)
     
   @classmethod
   def from_input(cls):                              
      student_form = {}                               
      for key,value in cls.form.items():
         if key in cls.int_fees:
            while True:
               try:
                  year = getdate('year' , 'Student' , '1111')
                  month = getdate('month' , 'Student' , '11')
                  day = getdate('day' , 'Student' , '11')
                  student_form[key] = date(year , month , day)
                  break
               except ValueError as error:
                  print(error, '\n')
                     
         else:
            student_form[key] = input(value)
            if not student_form[key]:
               student_form[key] = 'To implement'           
                                 
      return cls(**student_form)                      
                                                     
                                                     
   def __str__(self):                                  
      return (f'->>Full Name      : {self.name} {self.surname}\n'
                 f'   Date of birth  : {self.birthdate}\n'
                 f'   Email          : {self.email}\n'
                 )

                                 
 
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
            
class Trainer(Person):
   
   '''Subclass Trainer IS A Child Class of Person Class.'''
   
   form = {'name' : 'First name\n' , 'surname' : 'Last name\n' }
 
   count = 0

   def __init__(self , name , surname ):
      super().__init__(name , surname)
      Trainer.count += 1
      self.email = str(Trainer.count) + 'tr' + self.name + '.' + self.surname + '@private_school.org'
      


   @classmethod
   def from_input(cls):
      trainer_form = {}
      for key,value in cls.form.items():
         trainer_form[key] = input(value)
         if not trainer_form[key]:                               
            trainer_form[key] = 'To implement'          
           
      return cls(**trainer_form)


   def __str__(self):                               
      return (f'   ->>Full name: {self.name} {self.surname}\n'
              f'      Email    : {self.email}\n'
             
              )
      
 
