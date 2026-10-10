def calculate():
    print("Hello , pls select one of all")
    print("1 - BMI (Body Mass Index Calculator)")
    print("2 - Chinese Zodiac Calculator")
    print("3 - Birthday Guessing Game")

    # task2 ucun olanlae
    zodiacreqem = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    zodiacanimal = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
                    'Sheep']

    # task3 ucun olanlar
    dogumgunu = 0
    set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
    set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
    set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
    set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    n = int(input())

    # BMI Calculator
    if n == 1:
        print("pls enter your weight in kilograms")
        print("pls enter your height in meters")
        weight = int(input())
        height = float(input())
        BMI = weight / (height ** 2)
        if BMI < 18.5:
            print("Underweight")
            print("Do you want to contunie? (1-yes, 0-no)")
            heyox = int(input())
            if heyox == 1:
                calculate()
            else:
                print("GOOD BAY")
        if BMI >= 18.5 and BMI < 24.9:
            print("Normal Weight")
            print("Do you want to contunie? (1-yes, 0-no)")
            heyox = int(input())
            if heyox == 1:
                calculate()
            else:
                print("GOOD BAY")
        if BMI >= 25.0 and BMI < 29.9:
            print("Overweight")
            print("Do you want to contunie? (1-yes, 0-no)")
            heyox = int(input())
            if heyox == 1:
                calculate()
            else:
                print("GOOD BAY")
        if BMI >= 30.0:
            print("Obese")
            print("Do you want to contunie? (1-yes, 0-no)")
            heyox = int(input())
            if heyox == 1:
                calculate()
            else:
                print("GOOD BAY")

    # Chinese Zodiac Calculator
    if n == 2:
        print("pls enter your birth year")
        birthyear = int(input())
        qaliq = birthyear % 12
        k = zodiacreqem.index(qaliq)
        print(zodiacanimal[k])
        print("Do you want to contunie? (1-yes, 0-no)")
        heyox=int(input())
        if heyox == 1:
            calculate ()
        else:
            print("GOOD BAY")

    # Birthday Guessing Game
    if n == 3:
        print(set1)
        print("Is your date of birth in set 1? yes or not")
        cavabi = int(input())
        if cavabi == 1:
            dogumgunu = dogumgunu + set1[0]
        print(set2)
        print("Is your date of birth in set 2? yes or not")
        cavabi = int(input())
        if cavabi == 1:
            dogumgunu = dogumgunu + set2[0]
        print(set3)
        print("Is your date of birth in set 3? yes or not")
        cavabi = int(input())
        if cavabi == 1:
            dogumgunu = dogumgunu + set3[0]
        print(set4)
        print("Is your date of birth in set 4? yes or not")
        cavabi = int(input())
        if cavabi == 1:
            dogumgunu = dogumgunu + set4[0]
        print(set5)
        print("Is your date of birth in set 5? yes or not")
        cavabi = int(input())
        if cavabi == 1:
            dogumgunu = dogumgunu + set5[0]
        print(dogumgunu)
        print("Do you want to contunie? (1-yes, 0-no)")
        heyox = int(input())
        if heyox == 1:
            calculate()
        else:
            print("GOOD BAY")
calculate()