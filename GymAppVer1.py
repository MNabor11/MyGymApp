exercise_Type = input('What workout did you do? ')
exercise_Set = int(input('How many sets did you do? '))
exercise_Weight = float(input('How much weight did you use? '))
print(
    f'Awesome, you did {exercise_Type} for {exercise_Set} sets of {exercise_Weight}')
print(f'A total of {exercise_Weight*exercise_Set}')
