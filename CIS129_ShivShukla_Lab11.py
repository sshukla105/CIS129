"""Shiv Shukla
CIS 129
Griwzow
Module 11 Lab"""

# Exercise 9.1:

with open('grades.txt', mode='w') as grades: # creates grades.txt txt file in writing mode and calls the file "grades"
    while True: # creates while loop to accept inputs until break
        grade = input('Enter grade (0-100) or type "done" to finish: ') # requests user input
        if grade.lower() == 'done': # creates loop break for user input "done"
            break
        try: # converts user input to a floating point. Then writes the value onto the text file formatted to two decimal places and a skipped line
            gradeValue = float(grade)
            grades.write(f'{gradeValue:.2f}\n')
        except ValueError: # for values which can not be converted to float (i.e. string, symbols, etc.), a triggered ValueError will cause script to notify user and request new valid input
            print('Invalid input. Please try again with a numeric input or enter "done"')

# Exercise 9.2:

with open('grades.txt', mode='r') as grades: # opens grades text file in reading mode 
    reports = grades.readlines() # defines "reports" variable to the text lines prepared by .readlines() in the grades text file

total = 0 # initializes total variable
count = 0 # initialzes count variable (both to be used in calculation of mean)

print('Grades:') # prints the Grades: header
for report in reports: # creates a for loop to iterate through all "report"s in the reports' lines
    grade = float(report.strip()) # defines each grade as a floating point for each report stripped of the \n (leading whitespace)
    print(f'{grade:.2f}') # prints each grade formatted to two decimal places
    total += grade # adds every iterated grade to the total variable
    count += 1 # every iterated grade adds 1 to the count

if count > 0: # ensures count of grades is more than 0 (empty text file)
    average = total/count # calculates average
    print(f'Total is: {total:.2f}') # prints total
    print(f'Count is: {count}') # prints count
    print(f'Average is: {average:.2f}') # prints average
else: # if count is less than or equal to 0, user will be notified
    print('No grades available.')

# Exercise 9.3:

import csv # imports the csv module

with open('grades.csv', mode='w', newline='') as threeGrades: # creates grades csv file and calls the object threeGrades
    writer = csv.writer(threeGrades) # defines writer as a csv writer/editor
    writer.writerow(['First Name', 'Last Name', 'Exam 1 Grade', 'Exam 2 Grade', 'Exam 3 Grade']) # writes a header row with string literals
    while True: # creates a main while loop for entering student data
        firstName = input("Enter student's first name: ")# requests student first name
        lastName = input("Enter student's last name: ") # requests student last name
        while True: # creates nested while loop to collect grade inputs as floating points. 
            try:
                exam1Grade = float(input("Enter student's Exam 1 grade: "))
                break
            except ValueError:
                print('Invalid input. Please enter a numerical value')
        while True: # grade while loops are separated to prevent except blocks from continuing to re-request Exam 1 grades if an invalid input is entered for Exam 2 or 3
            try:
                exam2Grade = float(input("Enter student's Exam 2 grade: "))
                break
            except ValueError:
                print('Invalid input. Please enter a numerical value')
        while True:
            try:
                exam3Grade = float(input("Enter student's Exam 3 grade: "))
                break
            except ValueError:
                print('Invalid input. Please enter a numerical value')
            
        exam1Grade = f'{exam1Grade:.2f}' # formats grades to two decimal places (though Excel seems to recognize as integers unless a floating point is inputted manually)
        exam2Grade = f'{exam2Grade:.2f}'
        exam3Grade = f'{exam3Grade:.2f}'
        writer.writerow([firstName, lastName, exam1Grade, exam2Grade, exam3Grade]) # writes a row with the inputted student data

        while True: # creates a nested while loop to ask if user would like to enter more student data
            askAgain = input("Do you want to enter another student's grades? (yes/no): ").lower()
            if askAgain == 'yes': # yes response will break this loop and cause continuation of the main while loop
                break
            elif askAgain == 'no': # no will break this nested loop and ...
                break
            else: # will request user to input a valid response
                print('Invalid reponse. Please answer yes or no.')
        if askAgain == 'no': # ... will break the main loop 
            break
