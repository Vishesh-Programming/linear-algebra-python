import inputMatrix
import determinant
import matrixOperations

from help import inputRules

print("Linear Algebra Problem Solver")

while True:
    print()
    print("Operations available : ")
    print("-------------------------------")
    print("0 -> Know input rules ( Important )")
    print()
    print("1 -> Addition of matrix")
    print()
    print("2 -> Subtraction of matrix")
    print()
    print("3 -> Multiplication of matrix")
    print()
    print("4 -> Square of matrix")
    print()
    print("5 -> Determinant of matrix")
    print()
    print("6 -> Settings ( Comming Soon ) ")
    print()
    print("7 -> Exit program")
    print("-------------------------------")

    mainMenuChoice = input("Enter your choice : ")

    print("Please select the order of matrix")
    print("1 -> 2x2")
    print("2 -> 3x3")

    orderOfMatrixChoice = input("Enter youir choice :")

    if mainMenuChoice == "0":
        inputRules()

    elif mainMenuChoice == "1":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            secondOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrixOperations.addition(firstOrderTwoMatrix,
                                            secondOrderTwoMatrix)
            for i in res:
                print(i)
                
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            secondOrderThreeMatrix = inputMatrix.orderThree()
            res = matrixOperations.addition(orderThreeMatrix,
                                            secondOrderThreeMatrix)
            for i in res:
                print(i)
            
        else:
            print("Invalid Input")

    elif mainMenuChoice == "2":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            secondOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrixOperations.subtraction(firstOrderTwoMatrix,
                                               secondOrderTwoMatrix)

            for i in res:
                print(i)
            
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            secondOrderThreeMatrix = inputMatrix.orderThree()
            res = matrixOperations.subtraction(orderThreeMatrix,
                                               secondOrderThreeMatrix)

            for i in res:
                print(i)
        
        else:
            print("Invalid input")

    elif mainMenuChoice == "3":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            secondOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrixOperations.multiply(firstOrderTwoMatrix,
                                            secondOrderTwoMatrix)
            for i in res:
                print(i)
                
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            secondOrderThreeMatrix = inputMatrix.orderThree()
            res = matrixOperations.multiply(orderThreeMatrix,
                                            secondOrderThreeMatrix)

            for i in res:
                print(i)
                
        else:
            print("Invalid input")        
    
    elif mainMenuChoice == "4":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrixOperations.square(firstOrderTwoMatrix)

            for i in res:
                print(i)
                
        elif orderOfMatrixChoice == "2":

            firstOrderThreeMatrix = inputMatrix.orderThree()
            res = matrixOperations.square(firstOrderTwoMatrix)

            for i in res:
                print(i)
                
        else:
            print("Invalid input")

    elif mainMenuChoice == "5":

        if orderOfMatrixChoice == "1":

            orderTwoMatrix = inputMatrix.orderTwo()
            res = determinant.orderTwo(orderTwoMatrix)
            print("Determinant of given matrix is :")

            for i in res:
                print(i)
                
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            res = determinant.orderThree(orderThreeMatrix)
            print("Determinant of give matrix is : ")

            for i in res :
                print(i)
            

        else:
            print("Invalid input ( Only order 2x2 and 3x3 is allowed )")
        
    elif mainMenuChoice == "6":
        print("Settings - Comming Soon")

    elif mainMenuChoice == "7":
        print("Thank you")
        break

    else:
        print("Invalid input. Please try again")
