#Ricky CS101L 
#ASSIGNMENT 8
def add_test():
    global tests
    while True: 
        try:
            score = float(input('Enter the new Test score 0-100 ==> '))
            if score > 0:
                break
            else:
                print('Score must be greater than 0')
                continue
        except(ValueError):
            print('Score must be a number between 0-100')
        
    tests.append(score)

def clear_tests():
    global tests
    tests = []
    return tests

def clear_assignments():
    global assignments
    assignments = []
    return assignments

def add_assignment():
    global assignments
    while True:
        try:
            score = float(input('Enter the new Assignment score 0-100 ==> '))
            if score > 0:
                break
            else:
                print('Score must be greater than 0')
                continue
        except(ValueError):
            print('Score must be a number between 0-100')
        
    assignments.append(score)

def remove_assignment():
    global assignments
    try:
        score = float(input('Enter the Test score to remove 0-100 ==> '))
        if score < 0:
            print('Score must be greater than 0')
        if score in assignments:
            assignments.remove(score)
        else:
            print('Score could not be found')
    except(ValueError):
        print('Score must be a number between 0-100')
def remove_test():
    global tests
    try:
        score = float(input('Enter the Test score to remove 0-100 ==> '))
        if score < 0:
            print('Score must be greater than 0')
        if score in tests:
            tests.remove(score)
        else:
            print('Could not find that score to remove')
    except(ValueError):
        print('Score must be a number between 0-100')

def calculate_stats(scores, score_name):
    if len(scores) > 0:
        mean = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        std_factors = list(map(lambda x: (x - mean) ** 2, scores))
        std_numerator = functools.reduce(lambda x,y: x + y, std_factors) 
        if std_numerator > 0:
            std = math.sqrt((std_numerator) / len(scores))
        else:
            std = 0
        mean_str = '{:.2f}'.format(mean)
        std_str = '{:.2f}'.format(std)
        print(score_name.ljust(20), str(len(scores)).ljust(10), str(min_score).ljust(10), str(max_score).ljust(10), mean_str.ljust(10), std_str.ljust(10))
    else:
        print(score_name.ljust(20), str(len(scores)).ljust(10), 'n/a'.ljust(10), 'n/a'.ljust(10), 'n/a'.ljust(10), 'n/a'.ljust(10))

def display_scores(tests, assignments):
    print_display_header()
    calculate_stats(tests, 'Tests')
    calculate_stats(assignments, 'Programs')
    print()

    if (len(tests) > 0) and (len(assignments) > 0):
        test_mean = sum(tests) / len(tests)
        assignment_mean = sum(assignments) / len(assignments)
        final_grade = (test_mean * 0.6) + (assignment_mean * 0.4)
    elif (len(tests) > 0) and (len(assignments) == 0):
        test_mean = sum(tests) / len(tests)
        final_grade = (test_mean * 0.6)
    elif(len(assignments) > 0) and (len(tests) == 0):
        assignment_mean = sum(assignments) / len(assignments)
        final_grade = (assignments * 0.4)
    else:
        final_grade = 0
    print('The weighted score is       {:.2f}'.format(final_grade))

def print_display_header():
    score_type = 'Type'.ljust(21)
    score_quant = '#'.ljust(11)
    score_min = 'min'.ljust(11)
    score_max = 'max'.ljust(11)
    score_avg = 'avg'.ljust(11)
    score_std = 'std'.ljust(11)

    header = score_type + score_quant + score_min + score_max + score_avg + score_std
    print(header)
    print('=' * 69)
def print_menu(): 
    print('Grade Menu'.rjust(20))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
    print()


import functools
import math
tests = []
assignments = []
while True:
    print()
    print_menu()
    choice = input('==>  ')
    print()

    if choice == '1':
        add_test()
    elif choice == '2':
        remove_test()
    elif choice == '3':
        clear_tests()
    elif choice == '4':
        add_assignment()
    elif choice == '5':
        remove_assignment()
    elif choice == '6':
        clear_assignments()
    elif choice.upper() == 'D':
        display_scores(tests, assignments)
    elif choice.upper() == 'Q':
        break
    else: 
        print('You must enter one of the following options: 1/2/3/4/5/6/D/Q')