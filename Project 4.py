import datetime
import csv
import pandas

Dictionary1={}
def takeUserDay():
    try:
        day =int(input('Enter day: '))

        if day != str:
            if day <= 0 or day > 31:
                print('Enter a valid day!!! ')
                return takeUserDay()
            
            else:
                return day
    except:
        print('ERROR: Only Numbers are accepted!')
        return takeUserDay()



def takeUserMonth():
    month = input('Enter month: ')
    if month == 'January' or month == '1' or month == 'Jan' or month == 'january' or month == 'jan' or month == '01':
        monthNumber = 1
        return monthNumber
    elif month=='February' or month == '2' or month == 'Feb' or month =='february' or month =='feb' or month =='02' :
        monthNumber = 2
        return monthNumber
    elif month=='March' or month =='3' or month =='Mar' or month =='march' or month =='mar' or month =='03':
        monthNumber = 3
        return monthNumber
    elif month=='April' or month =='4' or month =='Apr' or month =='april' or month =='apr' or month =='04':
        monthNumber = 4
        return monthNumber
    elif month=='May' or month =='5' or month =='may' or month =='05':
        monthNumber = 5
        return monthNumber
    elif month=='June' or month =='6' or month =='june' or month =='06':
        monthNumber = 6
        return monthNumber
    elif month=='July' or month =='7' or month =='july' or month =='07':
        monthNumber = 7
        return monthNumber
    elif month=='August' or month =='8' or month =='Aug' or month =='august' or month =='aug' or month =='08':
        monthNumber = 8
        return monthNumber
    elif month=='September' or month =='9' or month =='Sept' or month =='september' or month =='sept' or month =='09':
        monthNumber = 9
        return monthNumber
    elif month=='October' or month =='10' or month =='Oct' or month =='october' or month =='oct':
        monthNumber = 10
        return monthNumber
    elif month=='November' or month =='11' or month =='Nov' or month =='november' or month =='nov':
        monthNumber = 11
        return monthNumber
    elif month=='December' or month =='12' or month =='Dec' or month =='december' or month =='dec':
        monthNumber = 12
        return monthNumber
    else:
        print('ERROR: Enter a valid month ')
        return takeUserMonth()
