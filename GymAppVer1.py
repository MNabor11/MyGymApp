exercise_Type = input('What workout did you do? ')
exercise_Set = int(input('How many sets did you do? '))
exercise_Weight = float(input('How much weight did you use? '))
print(
    f'Awesome, you did {exercise_Type} for {exercise_Set} sets of {exercise_Weight}')
print(f'A total of {exercise_Weight*exercise_Set}')
# how can keep this going? How can I make this scalable
# how can i make this easy to read and simple enough that it wont look like a hot mess
# exercise function


def exerciseFunction():
    exercise_Type = input('What workout did you do? ')
    exercise_Set = int(input('How many sets did you do? '))
    exercise_Weight = float(input('How much weight did you use? '))
    print(
        f'Awesome, you did {exercise_Type} for {exercise_Set} sets of {exercise_Weight}')
    print(f'A total of {exercise_Weight*exercise_Set}')
    return {
        'Workout': exercise_Type,
        'Sets': exercise_Set,
        'Weight': exercise_Weight
    }


workoutList = []
# creating a loop to keep creating functions so it will store new workouts until the user is done
print('Hello, welcome to G-Tracker')
while (True):
    option = int(
        input('1) Enter a workout\n2) View your progress\n3) Exit program\n'))
    match option:
        case 1:
            workoutList.append(exerciseFunction())
        case 2:
            for x in workoutList:
                print(
                    f'Workout{x['Workout']} for {x['Sets']} sets and {x['Weight']}')
        case 3:
            print('Exiting program...')
            break
