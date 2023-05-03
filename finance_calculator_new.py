import math
investment_1 = 'simple interest'
investment_2 = 'compound interest'
bond = 'bond'
interest_type = str(input('Please enter the type of interest you would like to choose: Simple or Compound interest.')).lower

user_input = str(input('Please input what you would like to calculate. ')).lower
if user_input == 'investment':
    interest_type = str(input('Please enter the type of interest you would like to choose: Simple or Compound interest.')).lower
    if interest_type == 'simple interest':
        amount = int(input('Please enter the initial amount you have deposited in the investment you are calculating: '))
        interest_rate = int(input('Please enter the interest rate chosen for the amount as a number without the \'%\' sign: '))
        time = int(input('Please enter in years the intended length of your investment: '))
        print(str(amount + interest_rate + time))
        simple_interest = (amount(1+((interest_rate/100)*time)))
        print('The total amount you will earn by the end of the investment is £' + simple_interest)