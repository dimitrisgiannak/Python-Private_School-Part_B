from datetime import date

'''
For details check README 
'''

error_message3 = 'You must input an integer' 

def getdate(datetime_ , statement , empty):
    while True:
        date1 = 0
        try:
            print_message = f'Please write the {datetime_} of the {statement} '
            date = input(print_message + '\n')
            if not date:
                date1 = int(empty)
                break
            else:
                date1 = int(date)
                break

        except ValueError:
            print(error_message3.center(75) , '\n')
    
    return date1

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def getmarks(value):
    while True:
        mark1 = 0
        try:
            mark = input(value) 
            if not mark:
                mark = -1
                break
            else:
                mark1 = int(mark)
                break
        except ValueError:
            print(error_message3 , '\n')
    
    return mark1