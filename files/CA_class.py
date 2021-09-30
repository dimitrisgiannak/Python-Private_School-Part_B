from datetime import date
from PV_methods2 import getmarks
from PV_methods2 import getdate

'''
For details check README 
'''

error_message = 'Please give me a valid input\n'

class Course:
   
   '''Class Course.Follows the same routine as Students class '''
  
   form = {'course_title' : 'Course Title\n' , 'course_description' : 'Course Description\n'}

   specify_course = ('course_title',)
   
   def __init__(self , course_title , course_language , course_description , course_type):
      self.course_title = course_title
      self.course_language = course_language
      self.course_description = course_description               
      self.course_type = course_type

   @classmethod
   def from_input(cls):
      course_form = {}
      for key,value in cls.form.items():

         if key in cls.specify_course:
            while True:
               print('1: FTPY\n2: PTPY\n3: FTJV\n4: PTJV\n5: FTJVS\n6: PTJVS\n7: FTC#\n8: PTC#\n')
               ch_course = input('Please choose the course title accoring to the NUMBER!This will be the second half of the full title \n')
               
               if ch_course:
                  if ch_course == '1':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'FTPY'
                     course_form['course_language'] = 'python'
                     course_form['course_type'] = 'full time'
                     break
                  elif ch_course == '2':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'PTPY'
                     course_form['course_language'] = 'python'
                     course_form['course_type'] = 'part time'
                     break
                  elif ch_course == '3':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'FTJV'
                     course_form['course_language'] = 'java'
                     course_form['course_type'] = 'full time'
                     break
                  elif ch_course == '4':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'PTJV'
                     course_form['course_language'] = 'java'
                     course_form['course_type'] = 'part time'
                     break
                  elif ch_course == '5':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'FTJS'
                     course_form['course_language'] = 'javascript'
                     course_form['course_type'] = 'full time'
                     break
                  elif ch_course == '6':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'PTJS'
                     course_form['course_language'] = 'javascript'
                     course_form['course_type'] = 'part time'
                     break
                  elif ch_course == '7':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'FTC#'
                     course_form['course_language'] = 'c#'
                     course_form['course_type'] = 'full time'
                     break
                  elif ch_course == '8':
                     specify_title = input('Please edit the first half of the title \n')
                     course_form[key] = specify_title + 'PTC#'
                     course_form['course_language'] = 'c#'
                     course_form['course_type'] = 'part time'
                     break
                  else:
                     print(error_message.center(70))
               
               elif not ch_course:
                  course_form[key] = 'To implement'
                  course_form['course_language'] = 'To implement'
                  course_form['course_type'] = 'To implement'
                  break      
                  
         else:
            course_form[key] = input(value)
            if not course_form[key]:
               course_form[key] = 'To implement'
      return cls(**course_form)

   def __str__(self):
      return (f'-->Course Title       : {self.course_title}\n '
              f'  Course Language    : {self.course_language}\n'       
              f'   Course Description : {self.course_description}\n'
              f'   Course Type        : {self.course_type}\n')
   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Assignment:
   
   '''Class Assignment.Follows the same routine as Students class'''
   
   form = {'title' : 'Assignment Title\n' , 'description' : 'Assignment Description\n',
           'sub_day' : 'Date of Submission\n' , 'total_mark' : 'Total Mark\n' , 'oral_mark' : 'Oral Mark\n'}

   
   def __init__(self , title , description , sub_day , total_mark , oral_mark):
      self.title = title
      self.description = description
      self.sub_day = sub_day
      self.total_mark = total_mark
      self.oral_mark = oral_mark

   int_data = ('total_mark' , 'oral_mark' , 'sub_day')

   @classmethod                                                  
   def from_input(cls):
      asgmnt_form = {}
      for key,value in cls.form.items():
         if key in cls.int_data:
            if key == 'total_mark':
               asgmnt_form[key] = getmarks(value)
       
            elif key == 'oral_mark':
               asgmnt_form[key] = getmarks(value)
 
            elif key == 'sub_day':
               while True:
                  try:
                     year = getdate('year' , 'submission date' , '1111')
                     month = getdate('month' , 'submission date' , '11')
                     day = getdate('day' , 'submission date' , '11')
                     asgmnt_form[key] = date(year , month , day)
                     break
                  except ValueError as error:
                     print(error , '\n')          

         else:
            asgmnt_form[key] = input(value)
            if not asgmnt_form[key]:                               
               asgmnt_form[key] = 'To implement'                 
                       
      return cls(**asgmnt_form) 

   def __str__(self):
      return (f'--> Assignment Title      : {self.title}\n '
              f'   Assignment Description: {self.description}\n '
              f'   Submission Date       : {self.sub_day}\n'
              f'    Total Mark            : {self.total_mark}\n'
              f'    Oral Mark             : {self.oral_mark}\n')
                
  
              
   
   
   
              
              
   
