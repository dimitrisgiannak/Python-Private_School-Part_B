CREATE DATABASE Private_School;
USE Private_School;

CREATE TABLE CoursesType(
CourseTypeID int unsigned auto_increment,
Course_type varchar(100) not null,
primary key (CourseTypeID)
);

CREATE TABLE CoursesLanguage(
CourseLangID int unsigned auto_increment,
Course_language varchar(20) not null,
primary key (CourseLangID)
);


CREATE TABLE Courses(
CourseID int unsigned auto_increment,
CourseTitle varchar(100) not null,
CourseLangID int unsigned ,
CourseDescr varchar(50) not null,
CourseTypeID int unsigned,
primary key (CourseID) ,
foreign key (CourseTypeID)
references CoursesType(CourseTypeID),
foreign key (CourseLangID)
references CoursesLanguage(CourseLangID)
);
                     
CREATE TABLE Assignments(
AssignID int unsigned auto_increment,
AssignTitle varchar(100) not null,
AssignDescr varchar(50) not null,
AssignSubDay date not null,
AssignTotMark int  not null,
AssignOralMark int  not null,
primary key (AssignID) 
);
                         
CREATE TABLE Students(
StudentID int unsigned auto_increment,
FirstName varchar(50) not null,
LastName varchar(50) not null,
DateOfBirth date not null,
Email varchar(100) not null,
primary key (StudentID) 
);

CREATE TABLE Trainers(
TrainerID int unsigned auto_increment,
TFirstName varchar(50) not null,
TLastName varchar(50) not null,
TEmail varchar(100) not null,
primary key (TrainerID)  
);    

CREATE TABLE AssignmentsCourses(
AssignID int unsigned not null,
CourseID int unsigned not null,
foreign key (AssignID) 
references Assignments(AssignID),
foreign key (CourseID) 
references Courses(CourseID)
);

CREATE TABLE StudentsCourses(
Stud_CourID int unsigned auto_increment,
StudentID int unsigned not null,
CourseID int unsigned not null,
primary key (Stud_CourID),
foreign key (StudentID) 
references Students(StudentID),
foreign key (CourseID) 
references Courses(CourseID)
); 

CREATE TABLE Stud_Cour_fees(
FeesID int unsigned auto_increment,
Stud_CourID int unsigned,
Fees int ,
primary key (FeesID),
foreign key (Stud_CourID)
references StudentsCourses(Stud_CourID)
);

CREATE TABLE TrainersCourses(
Train_CourseID int unsigned auto_increment, 
TrainerID int unsigned not null,
CourseID int unsigned not null,
primary key (Train_CourseID),
foreign key (TrainerID) 
references Trainers(TrainerID),
foreign key (CourseID) 
references Courses(CourseID)
);

CREATE TABLE Train_Cour_Sub(
SubID int unsigned auto_increment,
Train_CourseID int unsigned,
subj varchar(20) ,
primary key (SubID),
foreign key (Train_CourseID)
references TrainersCourses(Train_CourseID)
);


CREATE TABLE ACS(
AssignID int unsigned not null,
Stud_CourID int unsigned not null,
foreign key (Stud_CourID)
references StudentsCourses(Stud_CourID),
foreign key (AssignID)
references Assignments(AssignID)
);

INSERT INTO CoursesType
values (default,'To implement'), 
(default,'part time'),
(default,'full time')
;

INSERT INTO CoursesLanguage
values (default , 'To implement'),
(default , 'python'),
(default , 'java'),
(default , 'javascript'),
(default , 'c#')
;

INSERT INTO Courses
values   (default , 'cb1PTPY' , 2 , '24 weeks' , 2),
(default , 'cb1FTPY' , 2 , '12 weeks' , 3),
(default , 'cb1PTJV' ,  3  , '24 weeks' ,2),
(default , 'cb1FTJV' , 3 , '12 weeks' , 3),
(default , 'cb1PTJS' , 4 , '24 weeks' , 2),
(default , 'cb1FTJS' , 4 , '12 weeks' , 3),
(default , 'cb1PTC#' , 5 , '24 weeks' , 2),
(default , 'cb1FTC#' , 5 , '12 weeks' , 3)
;

INSERT INTO Assignments
values  (default,'PY asgnmnt','recap','2021/05/13',100,20),
(default,'JV asgnmnt','recap','2021/05/13',100,20),
(default,'JS asgnmnt','recap','2021/05/13',100,20),
(default,'C# asgnmnt','recap','2021/05/13',100,20),
(default,'PY asgnmnt2','advanced','2021/09/25',100,20),
(default,'JV asgnmnt2','advanced','2021/09/25',100,20),
(default,'JS asgnmnt2','advanced','2021/09/25',100,20),
(default,'C# asgnmnt2','advanced','2021/09/25',100,20)
;

INSERT INTO Trainers
values   (default,'Maria','Papantoniou','mariapapantoniou@hotmail.com'),
(default,'Mpampis','Ksigkoros','mpampisksigkoros@hotmail.com'),
(default,'Giannis','Mparmpounis','giannismparmpounis@gmail.com'),
(default,'Manos','Karagiannis','manoskaragiannis@yahoo.gr'),
(default,'John','Cena','johncena@hotmail.co.uk'),
(default,'Tyrion','Lanister','dwarflion@casterlyrock.west'),
(default,'Anna','Bandi','rivals@hotmail.gr'),
(default,'Sarantia','Tyrovola','sarantiatyrovola@hotmail.com')
;

INSERT INTO Students
values   (default,'Dimitris','Giannakopoulos','1990/03/01','dimitrgiannak@hotmail.com'),
(default,'Aggelos','Lukoudis','1991/04/02','aggeloslukoudis@hotmail.com'),
(default,'Maria','Semeli','0000/00/00','semelimaria@gmail.gr'),
(default,'Katerina','Mitsotaki','1995/06/20','katerinamitsotaki@gmail.com'),
(default,'Frodo','Bagins','0000/00/00','........'),
(default,'Giannis','Krompas','2000/09/12','gianniskro@gmail.com'),
(default,'Dimitris','Gaitanaros','2001/08/22','dimgait@hotmail.com'),
(default,'Baggelis','Anastasopoulos','2003/03/01','baggas@hotmail.com'),
(default,'Ntinos','Kassas','0000/00/00','ntinoskassas@yahhoo.gr'),
(default,'Aleksis','Georgakilas','1994/12/12','aleksisgeo@hotmail.com')
;
/*(default,'Nionios','Mallias','00-00-00','nioniosmallias@gmail.com',2400),
(default,'Tsiros','Takis','23-08-85','takistsiros@hotmail.com',2000),
(default,'Iwanna','Kontogiorgi','23-12-92','ioannakond@hotmail.gr',2000),
(default,'Eleutheria','Papadogianni','21-03-87','teleferik@hotmail.com',1500),
(default,'Elli','Kokkinou','23-01-65','ellikokkinou@yahoo.gr',2000),
(default,'Eulogitos','Lampsi','??-??-??','foskolos@ant1.gr',2000),
(default,'Paola','Bratsp','23-09-70','sfeteristria@gaou.gov',50000),
(default,'Aleksis','Pappas','02-09-80','filiaroufixta@survivor.gr',60000),
(default,'Junior Jack','Jackovia','03-04-18','jackalicius@hot.com',0),
(default,'Ilias','Dimopoulos','17-10-90','ILdimop@hotmail.com',2000),
(default,'Nikos','Peribolaris','12-04-88','peribolaris@hotmail.com',1500),
(default,'Nikos','Karoumpas','12-08-90','karoumpalos@hotmail.com',1500),
(default,'Petros','Nikas','19-10-89','forthewin@hotmail.com',1400),
(default,'Akis','Manolakis','10-09-88','akismanolakis@hotmail.com',1500)

;*/

INSERT INTO StudentsCourses (StudentID , CourseID)
values   (1,8),(1,1),(1,3),
         (2,1),
         (3,1),
         (4,2),
         (5,3),(5,5),(5,7),
         (6,4),
         (7,5),
         (8,6),
         (9,7),(9,3),
         (10,1)
         ;

INSERT INTO Stud_Cour_fees (Stud_CourID , Fees)
values   (1 , 2000)  ,(2 , 2000) , (3  ,1500),
         (4 , 1800) , (5 , 2000) , (6 , 1000),
         (7 , 1010) , (8 , 1230) , (9 , 900),
         (10 , 2030) , (11 , 1890) , (12 ,1200),
         (13 , 250) , (14 , 234) , (15 , 499)
         ;
         

INSERT INTO Assignmentscourses 
values   (1,1),(1,2),
         (5,1),(5,2),
         (2,3),(2,4),
         (6,3),(6,4),
         (3,5),(3,6),
         (7,5),(7,6),
         (4,7),(4,8),(8,7),
         (8,8)
;

INSERT INTO TrainersCourses (TrainerID , CourseID)
values   (1 , 1),(1, 2),
         (2, 3),(2, 4),
         (3, 5),(3, 6),
         (4, 7),(4, 8),
         (5, 1),(5, 2),
         (6, 7),(6, 8),
         (8, 3),(8, 4)
;

INSERT INTO Train_Cour_Sub (Train_CourseID , subj)
values  (1, "python") , (2, "python"),
        (3, "java") , (4 , "java"),
        (5 , "javascript") , (6,"javascript"),
        (7, "c#") , (8,"c#"),
        (9,"python") , (10, "python"),
        (11 , "c#") , (12,"c#"),
        (13, "java") , (14,"java")
        ;

INSERT INTO ACS 
values (1,2),(1,4),(1,5),(1,15),(1,6),
       (5,2),(5,4),(5,5),(5,15),(5,6),
       (2,3),(2,7),(2,14),(2,10),
       (6,3),(6,7),(6,14),(6,10),
       (3,8),(3,11),(3,12),
       (7,8),(7,11),(7,12),
       (4,9),(4,13),(4,1),
       (8,9),(8,13),(8,1)
       ;
       








