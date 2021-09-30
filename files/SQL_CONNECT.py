import mysql.connector
from CA_class import Course as C 
from CA_class import Assignment as A
from person_class import Trainer as T
from person_class import Student as S  
from CA_class import Course

'''
For details check README 
'''


connection = mysql.connector.connect(host = 'localhost' , user = 'root' , passwd = 'praxitelous4' , database = 'private_school')
Cursor = connection.cursor()


def sql_insert(item):
    
    if item == '1' :
        crs = C.from_input()
        cour_title = ['To implement' , 'TPY' , 'TJV' , 'TJS' , 'TC#']
        for i in range(len(cour_title)):
            if cour_title[i] in crs.course_title:
                cour_lang = i + 1

        course_type = ['To implement' , 'part time' , 'full time']
        for i in range(len(course_type)):
            if course_type[i] in crs.course_type:
                cour_type = i + 1
        
        Cursor.execute('INSERT INTO courses (CourseTitle , CourseLangID , CourseDescr , CourseTypeID) VALUES (%s , %s , %s , %s)', 
        (crs.course_title , cour_lang , crs.course_description , cour_type))

        connection.commit()

        return crs
        
    elif item == '2' :
        trnrs = T.from_input()
        Cursor.execute('INSERT INTO trainers (TFirstName , TLastName  , TEmail) VALUES (%s , %s , %s )',
        (trnrs.name , trnrs.surname , trnrs.email))
        
        connection.commit()
        return trnrs , Cursor.lastrowid

    elif item == '3' :
        sdnts = S.from_input()
        Cursor.execute('INSERT INTO students (FirstName , LastName , DateOfBirth , Email ) VALUES (%s , %s , %s , %s)',
        (sdnts.name , sdnts.surname , sdnts.birthdate , sdnts.email))

        connection.commit()
        return sdnts , Cursor.lastrowid

    elif item == '4' :
        assgn = A.from_input()
        Cursor.execute('INSERT INTO assignments (AssignTitle , AssignDescr , AssignSubDay , AssignTotMark , AssignOralMark) VALUES (%s , %s , %s , %s , %s)',
        (assgn.title , assgn.description , assgn.sub_day , assgn.total_mark , assgn.oral_mark))

        connection.commit()
        return assgn , Cursor.lastrowid


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def asgn_stdnt_crs(course , students_courses_id):
        
    query = 'SELECT AssignID FROM assignmentscourses'\
            ' INNER JOIN assignments'\
            '    using (AssignID)'\
            ' INNER JOIN courses'\
            '    using (CourseID)'\
            f' WHERE CourseTitle = "{course}"'
    Cursor.execute(query)
    fetched = Cursor.fetchall()
    for fetch in fetched:
        assign_id = fetch[0]
        Cursor.execute('INSERT INTO acs VALUES (%s , %s)' , (assign_id , students_courses_id))
        connection.commit()

    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def students_fees(id_tuple , stud_fees):
    for id , fee in zip(id_tuple , stud_fees):
        Cursor.execute('INSERT INTO stud_cour_fees (Stud_CourID , Fees) VALUES (%s , %s)' , (id , fee))
        connection.commit()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def train_cours_subj(id_tuple , trnr_crs_sub) :
    for id , subj in zip(id_tuple , trnr_crs_sub) :
        Cursor.execute('INSERT INTO train_cour_sub (Train_CourseID , subj) VALUES (%s , %s)' , (id , subj))
        connection.commit()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sql_multi_insert(table_name , element_id , courses_tuple , stud_fees , trainer_sub):  # + <-- trainer_subject
    id_list = []
    id_list.clear()
    for course in courses_tuple:
        query = f'SELECT * FROM courses WHERE CourseTitle = "{course}";'
        Cursor.execute(query)
        fetched = Cursor.fetchall()
        for item in fetched:
            cour_id = item[0]
            insert_query = f'INSERT INTO {table_name} VALUES (%s , %s)'
            Cursor.execute(insert_query , (element_id , cour_id))
            connection.commit()
            id_list.append(Cursor.lastrowid)

            if table_name == 'studentscourses (StudentID , CourseID)':
                 asgn_stdnt_crs(course , Cursor.lastrowid)
                                                                             
    if table_name == 'studentscourses (StudentID , CourseID)':

        students_fees(tuple(id_list) , stud_fees )


    if table_name == 'trainerscourses (TrainerID , CourseID)' : 
        train_cours_subj(tuple(id_list) , trainer_sub ) 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def retrieve_data():
    board = []
    query = 'SELECT CourseTitle,Course_Language,CourseDescr,Course_type FROM coursestype'\
            ' INNER JOIN courses USING (CourseTypeID)'\
            ' INNER JOIN courseslanguage USING (CourseLangID)'
    Cursor.execute(query)
    fetched = Cursor.fetchall()
    for item in fetched:
        from_tuple_to_obj = Course(item[0] , item[1] , item[2] , item[3])
        board.append(from_tuple_to_obj)

    return board



#--------------------------------------------------------------------------------------------------------------------------------------------

def sql_output(procedure , course_or_table):
    Cursor.callproc(procedure , course_or_table)
    for results in Cursor.stored_results():
        all_results = results.fetchall()
    
    for record in all_results:
        print(*record , '\n')

#----------------------------------------------------------------------------------------------------------------------------------------------

def sql_close():
    connection.close()
    
