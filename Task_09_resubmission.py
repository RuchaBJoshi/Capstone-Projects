#Greeting for the user.
print('\n Welcome to my program!')

# Option 1: Choose calculator to input integers and operator and obtain the calculated value as output.
# Option 2: Access and view the conetents of an existing .txt file.

print('\n You can either enter:\n \'1\' for Calculator or \n \'2\' to open a file with pre-installed equations.')
user_input = input('\n Please enter either 1 or 2: ')
if user_input == '1':
#Ask for user input
    file_name = input('\nWhat would you like to name your file? ')
    textfile_name = file_name + '.txt'
    print('You have named your file ' + '\'' + textfile_name + '\'')
    file = open(textfile_name, 'a+')
    
    while True:
        
        while True:
            try:
                val_1 = int(input('\n Please enter your first integer value: '))
                break
            except ValueError:
                print('Please enter a valid input that is an integer and not a string or a float.')

        while True:
            try:
                val_2 = int(input('\n Please enter your second integer value: '))
                break
            except ValueError:
                print('Please enter a valid input that is an integer and not a string or a float.')


        while True:
            operator = str(input('\n Please enter the operator. '+ '\n\'+\' to add, \n\'-\' to subtract, \n\'*\' to multiply and \n\'/\' to divide the two values.\n: '))
            if operator == '+':
                calculation = val_1 + val_2
                break
            elif operator == '-':
                calculation = val_1 - val_2
                break
            elif operator == '*':
                calculation = val_1 * val_2
                break
            elif operator == '/':
                try:
                    calculation = val_1 / val_2
                    break
                except ZeroDivisionError:
                    print('\nA number cannot be divided by 0. Please enter other operator to carry out a calculation with 0.')
            else:
                print('Please enter valid input values.')


# If all input values entered are as expected than the code returns with the calculation.

        print('\n The answer to ' + str(val_1) + ' ' + operator + ' ' + str(val_2) + ' is ' + str(calculation) + '\n')

# Used this block of code to insert the entered values as an equation to the created text file.

        file.write (str(val_1) + ' ' + operator + ' ' + str(val_2) + ' = ' + str(calculation) + '\n')

        next_stage = input('Enter \'c\' to continue or \'e\' to end and save the file: ')
        if next_stage == 'c':
            continue
        elif next_stage == 'e':
            file.close()
            print('\nYou have chosen to end the calculator program.')
            break
        else:
            'Please enter either c or e in lower case.'

# This is the second part of the if statement, with elif statement to be executed when the user chooses option '2'.
# input function to enter the name of the chosen file with '.txt' in the end.
# Used try and except block to open the file if input is as expected otherwise use except block to display error message
# Used finally to close the file to ensure that the program does not crash.


elif user_input == '2':
    file_name = input('\n Please enter the file name that you would like to access with \'.txt\' in the end: ')
    print('\nYou entered ' + '\'' + file_name + '\'.')

    file = None
    try:
        with open(file_name , 'r') as file:
            print('\nHere is the content of this text file: \n')
            print(file.read())

    except FileNotFoundError:
        print('\nThe file with the entered name does not exist. Please enter the correct file name with \'.txt\' at the end and try again.')

    finally:
        if file is not None:
            file.close()


# else function to tackle any invalid inputs in the first if statement: choosing option 1 or 2.
else:
    print('\nPlease try again and either choose \'1\' or \'2\'.')


# Concluding the code with a greeting.

print('\nThank you for using my code :) \n')

#End of Code.