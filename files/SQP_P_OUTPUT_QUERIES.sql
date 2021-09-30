  SELECT * FROM students; -- A list of all the students
  
  -- ######################################################################################################################################################################### 
  SELECT * FROM trainers; -- A list of all the trainers
  
  -- ######################################################################################################################################################################### 
  SELECT * FROM assignments; -- A list of all the assignments
  
  -- ######################################################################################################################################################################### 
  SELECT * FROM courses; -- A list of all the courses
  
  -- ######################################################################################################################################################################### 
  SELECT firstname as 'student name',lastname as 'student surname',coursetitle as 'course title'
  FROM studentscourses
     INNER JOIN students
	    USING (StudentID)
	 INNER JOIN courses
		USING (CourseID)
	 WHERE CourseTitle = 'coursetitle';      -- A list of all the students per course.You need to input CourseTitle
										     -- Chooce from : 'cb1PTPY' , 'cb1FTPY' , 'cb1PTJV' , 'cb1FTJV' , 'cb1PTJVS' ,'cb1FTJVS' , 'cb1PTC#' , 'cb1FTC#'
                                         
  -- ######################################################################################################################################################################### 
    
  SELECT tfirstname as 'trainer name' ,tlastname as 'trainer surname',courselanguage as 'course language',coursetype as 'course type' 
  FROM trainerscourses
     INNER JOIN trainers
	    USING (TrainerID)
	 INNER JOIN courses
		USING (CourseID)
	 WHERE CourseTitle = 'coursetitle';      -- A list of all the students per course.You need to input CourseTitle
										     -- Chooce from : 'cb1PTPY' , 'cb1FTPY' , 'cb1PTJV' , 'cb1FTJV' , 'cb1PTJVS' ,'cb1FTJVS' , 'cb1PTC#' , 'cb1FTC#'
                                           
  -- ######################################################################################################################################################################### 
    
  SELECT assigntitle as 'assignment title',assigndescr as 'assignment description',courselanguage as 'course language',coursetype as 'course type' 
  FROM assignmentscourses
     INNER JOIN assignments
        USING  (AssignID)
	 INNER JOIN courses
		USING (CourseID)
	 WHERE CourseTitle = 'coursetitle';      -- A list of all the students per course.You need to input CourseTitle
										     -- Chooce from : 'cb1PTPY' , 'cb1FTPY' , 'cb1PTJV' , 'cb1FTJV' , 'cb1PTJVS' ,'cb1FTJVS' , 'cb1PTC#' , 'cb1FTC#'
                                           
  -- ######################################################################################################################################################################### 
  
  SELECT assigntitle as 'assignment title',assigndescr as 'assignment description',courselanguage as 'course language',coursetype as 'course type',firstname as 'student name',lastname as 'student surname' 
  FROM acs
     INNER JOIN studentscourses
        USING (stud_courid)
	 INNER JOIN students
		USING (studentid)
	 INNER JOIN courses
		USING (courseid)
	 INNER JOIN assignments
		USING (assignid)
     WHERE courseTitle = 'coursetitle'
     ORDER BY firstname,lastname;            -- A list of all the students per course.You need to input CourseTitle
										     -- Chooce from : 'cb1PTPY' , 'cb1FTPY' , 'cb1PTJV' , 'cb1FTJV' , 'cb1PTJVS' ,'cb1FTJVS' , 'cb1PTC#' , 'cb1FTC#'
                                       
  -- #########################################################################################################################################################################
  
  SELECT studentid as 'student ID',firstname as 'student name',lastname as 'student surname' 
  FROM studentscourses
     INNER JOIN students
	    USING (studentid)
	 GROUP BY studentscourses.studentid
		HAVING count(studentid) > 1;      -- A list of all the students with more than one course
                                       
                                           