 
DELIMITER //
CREATE procedure allout(IN course VARCHAR(20))
BEGIN
    IF course = 'courses' THEN
       SELECT CourseID as 'course id' , CourseTitle as 'course title' , Course_language as 'course language' , CourseDescr as 'course description' , Course_type as 'course type' FROM courses
       INNER JOIN courseslanguage
	      USING (CourseLangID)
	    INNER JOIN coursestype
         USING (CourseTypeID)
		 ORDER BY CourseID;
        
	 ELSEIF course = 'students' THEN
       SELECT * FROM students
       ORDER BY StudentID;
       
	 ELSEIF course = 'trainers' THEN
       SELECT * FROM trainers
       ORDER BY TrainerID;
       
	 ELSEIF course = 'assignments' THEN
       SELECT * FROM assignments
       ORDER BY AssignID;
	
	END IF;
        
END //
DELIMITER ;

DELIMITER //
CREATE procedure asgn_crs(IN course VARCHAR(20))
BEGIN
    SELECT assigntitle as 'assignment title',assigndescr as 'assignment description',coursetitle as 'course title' FROM assignmentscourses
       INNER JOIN assignments
	      USING  (AssignID)
	   INNER JOIN courses
		  USING (CourseID)
	  WHERE CourseTitle = course;

END //
DELIMITER ;

DELIMITER //
CREATE procedure stdnt_crs(IN course VARCHAR(20))
BEGIN
    SELECT firstname as 'student name',lastname as 'student surname',coursetitle as 'course title'  FROM studentscourses
       INNER JOIN students
	      USING (StudentID)
	   INNER JOIN courses
		  USING (CourseID)
	   WHERE CourseTitle = course;
END //
DELIMITER ;

DELIMITER //
CREATE procedure trnr_crs(IN course VARCHAR(20))
BEGIN
    SELECT DISTINCT tfirstname as 'trainer name' ,tlastname as 'trainer surname',coursetitle as 'course title' FROM trainerscourses
	   INNER JOIN trainers
	      USING (TrainerID)
	   INNER JOIN courses
		  USING (CourseID)
	   WHERE CourseTitle = course;

END //
DELIMITER ;

DELIMITER //
CREATE procedure stdnt_more_crs(IN course VARCHAR(20))
BEGIN
    SELECT studentid as 'student ID',firstname as 'student name',lastname as 'student surname' FROM studentscourses
	   INNER JOIN students
          USING (studentid)
       GROUP BY studentscourses.studentid
          HAVING count(studentid) > 1;
END //
DELIMITER ;


DELIMITER //
CREATE procedure assign_per_course_per_student(IN course VARCHAR(20))
BEGIN
    SELECT assigntitle as 'assignment title',coursetitle as 'course title',firstname as 'student name',lastname as 'student surname' FROM acs
	   INNER JOIN studentscourses
          USING (stud_courid)
       INNER JOIN students
		  USING (studentid)
       INNER JOIN courses
          USING (courseid)
       INNER JOIN assignments
          USING (assignid)
    WHERE CourseTitle = course
    ORDER BY firstname,lastname;
END //
DELIMITER ;




