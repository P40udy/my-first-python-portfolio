

working = "true"

while working == "true":
    process_calculation = input("what type of calculation would you like to do:  addition, subtraction, multiplacation or division? ")

    if process_calculation == "addition":
        numbers = int(input("how many numbers in your calculations : 2, 3, 4 or 5: "))
        if numbers == 2:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            answer = a + b
            print("the answer is ", answer)
            working = "true"
        elif numbers == 3:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            answer = a + b + c
            print("the answer is ", answer)
            working = "true"
        elif numbers == 4:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            answer = a + b + c + d
            print("the answer is ", answer)
            working = "true"
        elif numbers == 5:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            e = int(input("what is the value of your fifth number number:  "))
            answer = a + b + c + d + e
            print("the answer is ", answer)
            working = "true"
        
    elif process_calculation == "subtraction":
        numbers = int(input("how many numbers in your calculations : 2, 3, 4 or 5: "))
        if numbers == 2:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            answer = a - b
            print("the answer is ", answer)
            working = "true"
        elif numbers == 3:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            answer = a - b - c
            print("the answer is ", answer)
            working = "true"
        elif numbers == 4:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            answer = a - b - c - d
            print("the answer is ", answer)
            working = "true"
        elif numbers == 5:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            e = int(input("what is the value of your fifth number number:  "))
            answer = a - b - c - d - e
            print("the answer is ", answer)
            working = "true"
        
    elif process_calculation == "division":
        numbers = int(input("how many numbers in your calculations : 2, 3, 4 or 5: "))
        if numbers == 2:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            answer = a / b
            print("the answer is ", answer)
            working = "true"
        elif numbers == 3:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            answer = a / b / c
            print("the answer is ", answer)
            working = "true"
        elif numbers == 4:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            answer = a / b / c / d
            print("the answer is ", answer)
            working = "true"
        elif numbers == 5:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            e = int(input("what is the value of your fifth number number:  "))
            answer = a / b / c / d / e
            print("the answer is ", answer)
            working = "true"

    elif process_calculation == "multiplacation":
        numbers = int(input("how many numbers in your calculations : 2, 3, 4 or 5: "))
        if numbers == 2:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            answer = a * b
            working = "true"
            print("the answer is ", answer)
        elif numbers == 3:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            answer = a * b * c
            working = "true"
            print("the answer is ", answer)
        elif numbers == 4:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            answer = a * b * c * d
            working = "true"
            print("the answer is ", answer)
        elif numbers == 5:
            a = int(input("what is the value of your first number: "))
            b = int(input("what is the value of your second number number: "))
            c = int(input("what is the value of your third number number:  "))
            d = int(input("what is the value of your fourth number number:  "))
            e = int(input("what is the value of your fifth number number:  "))
            answer = a * b * c * d * e
            working = "true"
            print("the answer is ", answer)
        
    else:
        print("that is not an option, please try again later")