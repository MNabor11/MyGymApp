def exerciseFunction():

    exercise_Type = input('\nWhat workout did you do? ')
    exercise_Set = int(input('How many sets did you do? '))
    exercise_Rep = int(input('For how many repetitions? '))
    exercise_Weight = float(input('How much weight did you use? '))

    print(
        f'\nAwesome, you did {exercise_Type} for {exercise_Set} sets of {exercise_Rep}, for {exercise_Weight} lbs.')

    totalWeight = (exercise_Set*exercise_Rep)*exercise_Weight

    print(f'A total of {totalWeight} lbs.\n')

    return {
        'Workout': exercise_Type,
        'Sets': exercise_Set,
        'reps': exercise_Rep,
        'Weight': exercise_Weight,
    }


workoutList = []

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
                    f'\n{x['Workout']} for {x['Sets']} sets of {x['reps']} and {x['Weight']}lbs.\n')

        case 3:
            print('Exiting program...')
            break

        case _:
            print("Not a valid option,\nplease choose a valid option")
