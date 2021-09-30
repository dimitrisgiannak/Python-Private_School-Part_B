Γεία σας!

                                                                      ***UPDATE***
Στο part b του project:

*Ανοίγουμε το αρχείο SQL_P_MAIN και το τρέχουμε καθώς και το αρχείο SQL_P_PROCEDURES.
*Για να ξεκινήσουμε το πρόγραμμα μας ανοίγουμε το file main_body.py και πατάμε το αντίστοιχο run command ανάλογα τον editor μας!
*Στο αρχείο SQL_CONNECT.py στο connection χρησιμοποιηούμε τον δικό μας κωδικό για να κάνουμε log in στο mySQL Workbench.



<> SQL SCHEMA WORKBENCH


- Θεωρούμε ότι όλες οι  κύριες οντότητες έχουν σχέση πολλά προς πολλά μεταξύ τους.Το assignments π.χ μπορεί να έχει 
  πολλά courses μιας και δεν είναι course language exclusive.
  


- Στο ερώτημα 5 υπάρχουν έτοιμα τα output queries. Κάποια από αυτά θα χρειαστούν manual input ανάλογα με το course.
  Οι επιλογές αναφέρονται δίπλα και αφορούν μόνο τα courses που είναι ήδη καταχωρημένα στο table course.



- Για τις ανάγκες του ερωτήματος 6/b/vii φτιάξαμε το table studentscourses με primary key.Αυτό το key σε συνδυασμό
  με το assignments key θα καταχωρούνται στον πίνακα assignments per student per course (acs).Κάθε μοναδικός συνδυασμός
  student course θα έχει και ένα ή περισσότερα assignments.



<> ΜΑΙΝ PROGRAMM


- Ξεκινάμε κάνοντας retrieve τα data από το table courses διότι όλες οι υπόλοιπες οντότητες σχετίζονται με αυτά.
  Με αυτόν τον τρόπο μπορούμε να καταχωρήσουμε έναν καινούργιο student σε ένα από τα ήδη υπάρχοντα courses. 
  Φυσικά υπάρχει η δυνατότητα να καταχωρηθούν ακόμα όσα courses θέλουμε.
  Σε περίπτωση που δεν κάναμε retrieve θα έπρεπε να ακολουθήσουμε μια συγκεκριμένη σείρα στο input του κυρίως προγράμματος
  για να μην υπάρχει απώλεια δεδομένων.(insert courses then assignments then and only then students and trainers)



- Επίσης από την στιγμή που η βάση δεδομένων μας έχει έτοιμα data δεν χρειάζεται να υποχρεώσουμε πλέον τον user να κάνει
  insert σε όλα τα πεδία , όπως ζητήθηκε στο part a.



- Τα data των courses της SQL γίνονται retrieve σε μορφή tuple μέσα σε μια λίστα.Επειδή τα courses στο κυρίως πρόγραμμα είναι objects
  Course μετατρέπουμε αυτά τα data σε object Course για να συμφωνούν με το υπόλοιπο πρόγραμμμα.



<> METHODS :input menu


1: def sql_insert(item):

      -Είναι η πρώτη μέθοδος που χρησιμοποιείται από το πρόγραμμα.Ο χρήστης επιλέγει την οντότητα που θέλει να κάνει insert.
      -Στέλνουμε την επιλογή του στην μέθοδο sql_insert (sqlin) και ανάλογα με αυτήν δημιουργούμε ένα καινούργιο object στην
      αντίστοιχη Class.
      -Ανάλογα με την επιλογή εκτελούνται αντίστοιχες λειτουργίες ( if item == '1': , etc ).
      -Παράλληλα κάνουμε insert το καινούργιο object στον αντίστοιχο πίνακα της βάσης δεδομένων μας.
      -Μας επιστρέφει το object ή το object μαζί με το Cursor.lastrowid του αντίστοιχου πίνακα στο κυρίως πρόγραμμα.
     
     

2: def course_input(table , element_id , courses_board): (c_i)
          
      -Είναι η δεύτερη μέθοδος που χρησιμοποιείται από το πρόγραμμα.Βρισκόμαστε ακόμα στην ίδια επιλογή του χρήστη.
      -Η μέθοδος αυτή δέχεται τα στοιχεία του table που σχετίζονται με το table courses ('assignmentscourses').
      -Επίσης δέχεται τα στοιχεία του Cursor.lastrowid και τον πίνακα όλων των courses που υπάρχουν στην βάση δεδομένων μας
      (courses_board)
      -Παρατητούμε πως το table και το elemet_id δεν χρησιμοποιείται μέσα στις λειτουργίες της μεθόδου παρά μόνο
      στο τέλος που καλούμε μια νέα μέθοδο!
      -Μέσα σε μια επαναληπτική δομή ζητάμε να γίνουν input τα courses που μπόρει να έχει το συγκεκριμμένο object.
      *Τα courses θα τα διαλέγουμε με βάση το course_title (crs.course_title).
      -Για να κάνουμε output στον χρήστη τα courses χρησιμοποιούμε μια επαναληπτική δομή σε συνδυασμό με το roll
      για να βγαίνουν αριθμημένα.Η επιλογή του course θα γίνεται με τον αντίστοιχο αριθμό.
      -Στην συνέχεια ρωτάμε αν συμμετέχει και σε άλλα courses.Αν ναι , τότε η διαδικασία επαναλαμβάνεται.
      Αν όχι , τότε αποθηκεύουμε τα πιθανά courses σε μια λίστα και τα μετατρέπουμε σε tuple.
      -H μέθοδος μετά καλεί την μέθοδο / sql_multi_insert \.
     ** -Σε περίπτωση που το table αφορά τους studentscourses τότε εκτελούνται κάποιες παραπάνω λειτουργίες.
        Πρώτα απ' 'ολα  table = 'studentscourses (StudentID , CourseID)'
        Αυτό γίνεται διότι αργότερα θα χρειαστεί να κάνουμε insert στον αντίστοιχο πίνακα αλλά αυτος έχει δικό του
        primary key και είναι auto_increment!
        -Επίσης ζητάμε να γίνει input το αντίστοιχο fee για το μάθημα που έχει επιλεχθεί.(fees_choice)
        -Αποθηκευέται το fees_choice σε μια λίστα και στο τέλος της μεθόδου το μετατρέπουμε σε tuple.
        -Δεν μας πειράζει αν το tuple είναι empty.


3: def sql_multi_insert(table_name , element_id , courses_tuple , stud_fees): (sqlmi)

      -Eίναι η τρίτη μέθοδος που χρησιμοποιείται απο το πρόγραμμμα.
      -Η μέθοδος αυτή δέχεται τα στοιχεία table_name(δεν άλλαξε ποτέ) , element_id(δεν άλλαξε ποτέ) , courses_tuple , stud_fees.
      -Χρησιμοποιούμε μια επαναληπτική μέθοδο και αφορά κάθε course που επιλέχθηκε στην προηγούμενη μέθοδο.
      -Για κάθε course διαλέγουμε από το table courses όλα τα course που έχουν τον αντίστοιχο course.title.(μέθοδος 2)
      Η λογική λέει ότι πάντα θα βγαίνει ένα αποτέλεσμα. Η μόνη περίπτωση να βγουν παραπάνω είναι εάν εσκεμμένα έχουμε δύο courses
      με ίδιο course.title αλλά διαφορετικό description.Το courses table έχει δικό του Primary key άρα η μοναδικότητα των courses
      δεν εξαρτάται από το course.title.
      -Για κάθε record που βρίσκουμε κάνουμε insert στο αντίστοιχο σχεσιακό table.('assignmentscourse' , 'trainerscourses' , 'studentscourses')
      Χρησιμοποιούμε το ίδιο element_id και το αντίστοιχο cour_id.
      -Στο τέλος κάθε επανάληψης εισάγουμε το Cursor.lastrowid σε μια λίστα.(id_list) Το Cursor.lastrowid αφορά τα tables 'assignmentscourses' , 'trainerscourses' , 'studentscourses'.
      -Επίσης χρησιμοποιούε το Cursor.lastrowid στο τέλος κάθε επανάληψης μόνο όταν το table_name == 'studentscourses (StudentID , CourseID)'
      καλόντας μια νέα μέθοδο / asgn_stdnt_crs \.
      -Στο τέλος των επαναλήψεων των course μέσα στο courses_tuple εάν το table_name == 'studentscourses (StudentID , CourseID)'
      εκτελείται ακόμα μια λειτουργία καλόντας την μέθοδο / students_fees() \.


4: def asgn_stdnt_crs(course , students_courses_id):

      -Εάν το table_name == 'studentscourses (StudentID , CourseID)' , τότε καλείται αυτή η μέθοδος.
      -Η μέθοδος αυτή δέχεται τα στοιχεία course , students_courses_id.
      -Κάνουμε select όλα τα assignid που έχουν σχέση με τα courses που έχουν course_title = course.
      -Κάθε assignid το κάνουμε insert στον πίνακα assignments_per_students per_course (acs because its funnier).
      -Ένας συνδυασμός student_courses_id μπορεί να έχει περισσότερα από ένα assignid 's.


5: def students_fees(id_tuple , stud_fees):

      -'Οπως και παραπάνω η μέθοδος καλείται μόνο όταν table_name == 'studentscourses (StudentID , CourseID)'.
      -Η μέθοδος δέχεται τα στοιχεία id_tuple , stud_fees.
      -Το len(id_tuple) == len(stud_fees).Γι' αυτό τον λόγο χρησιμοποιηούμε μια επαναληπτική δομή και για τα δύο tuples.
      -Κάνουμε insert στο table stud_cour_fees έναν συνδυασμό student_courses_id με τα αντίστοιχα δίδακτρα του μαθήματος.
      

                              Με αυτήν την σειρά θα εκτελεστούν οι μέθοδοι αν υποθέσουμε ότι κάνουμε σωστά data inputs.
                              Σε κάθε άλλη περίπτωση θα ξεκινάει απ' την αρχή και θα ζητάει choice.
 


<> METHODS :output menu


1: def sql_output(procedure , course_or_table): (sqlout)

      -Χρησιμοποιείται για όλα τα output που ζητούνται.Την καλούμε είτε μέσω του main_body είτε μέσω της μεθόδου rolling().
      -Δέχεται τα στοιχεία procedure , course_or_table.
      -Το procedure αφορά το όνομα του procedure που βρίσκεται στην βάση δεδομένων μας.


2: def rolling(courses_board , print_message , procedure_name):

      -Χρησιμοποιείται για το output που αφορούν το choice 5 , 6 , 7 , 8.
      -Δέχεται τα στοιχεία courses_board , print_message , procedure_name.
      -Με μια επαναληπτική δομή σαρώνει όλα τα courses που υπάρχουν στην βάση δεδομένων μας.(Είναι μια λίστα στο κυρίως προγραμμα)
      -Επιλέγουμε το αντίστοιχο αριθμημένο course (crs.course_title).
      -Αν το s_t_a_choice υπάρχει στα αριθμημένα courses τότε καλούμε την μέθοδο sql_output με το αντίστοιχο course
      που επιλέχθηκε.



<> CLASSMETHODS  


      -Υπάρχουν στο σύνολο τέσσερα classmethods για τα αντίστοιχα objects.(Course , Assignment , Student , Trainer)
      -Ακολουθούν την ίδια λογική με μικρές αλλαγές ανάλογα με τις ανάγκες της κάθε class.
      -Η γενική ιδέα είναι να γίνονται τα input μέσα στην ίδια την class μέσω της classmethod.
      Χρησιμοποιούμε ένα dictionary με όνομα form και μέσα περιλαμβάνει τα object attributes (key) και μια πληροφορία
      για το κάθε ένα (values).
      -Σαρώνουμε το dictionary form και για κάθε key κάνουμε input με print message το value του key.Κάθε συνδυασμός
      αποθηκεύεται σε ένα καινούργιο dictionary
      -Στο τέλος της σάρωσης κάνουμε return το καινούργιο dictionary και δημιουργείται το object μέσω της def __init__().
      


      class Course
            
            -Ανάλογα με την επιλογή του χρήστη (ch_course) συμπληρώνεται το 'coutse_title' , 'course_language' , 'course_type'.
            Στην συνέχεια συμπληρώνεται ότι άλλο υπάρχει στο dictionary form.
      


      class Assignment

            -Χρησιμοποιεί δύο μεθόδους getmarks() , getdate().Οι μέθοδοι δεν βρίσκονται μέσα στην class διότι χρησιμοποιούνται
            και από άλλες classes.


      class Person

            -Parent class περιέχει το όνομα και το επώνυμο.Δεν εκτελεί κάποια λειτουργεία απο μόνη της παρά μόνο
            όταν την καλέσει η class Student ή η class Trainer


      class Student

            -Student class is a child class of class Person.Ακολουθεί την ίδια διαδικασία με τις υπόλοιπες classes.
            Επίσης χρησιμοποιεί την μέθοδο getdate().Τα στοιχεία που επιστρέφονται από την μέθοδο είναι integers.
            -Χρησιμοποιούμε μια try except μέσα σε επαναληπτική δομή γιατί οι integer μπορεί να είναι out or range
            καθώς μετατρέπουμε την πληροφορία σε date.


      class Trainer

            -Trainer class is a child class of class Person.Ακολουθεί την ίδια διαδικασία με τις υπόλοιπες classes.


<> METHODS USED BY CLASSES


1: def getdate(datetime_ , statement , empty):

      -Χρησιμοποιείται από τις classes Student και Assignments.
      -Δέχεται τα στοιχεία datetime_ , statement , empty.Το στοιχείο empty το χρησιμοποιούμε εάν ο χρήστης αφήσει κενό.
      -Το datetime_ , statement τα χρησιμοποιούμε για να δώσουμε κατάλληλο μήνυμα ανάλογα την περίπτωση.
      -Επιστρέφει τρεις τιμές integer.


2: def getmarks((value):

      -Χρησιμοποιείται απο την class Assignment.
      -Δέχεται το στοιχείο value.Το value αφορά το value του key 'total mark' ή 'oral mark'.
      -Επιστρέφει μια τιμή integer και εκχωρείται στο asgmnt_form['total mark] και asgmnt_form['oral mark'] αντίστοιχα.



<> METHOD when closing programm

1: def sql_close():

      -Χρησιμοποιείται όταν ο χρήστης επιλέξει να τερματίσει την λειτουργία του προγράμματος και τερματίζει την σύνδεση με την βάση δεδομένων μας.






     

  