import inputMatrix
import determinant
import matrixOperations

from help import inputRules

# options 

# 1 - Addition of matrix
# 2 - Subtraction of matrix
# 3 - Multiplication of matrix
# 4 - Square of matrix
# 5 - Determinant of matrix

print("Linear Algebra")

while True :
    print()
    print("Operations available : ")
    print("-------------------------------")
    print("1 -> Addition of matrix")
    print("2 -> Subtraction of matrix")
    print("3 -> Multiplication of matrix")
    print("4 -> Square of matrix")
    print("5 -> Determinant of matrix")
    print("6 -> Help ( How to use ? )")
    print("7 -> Settings ( Comming Soon ) ")
    print("8 -> Exit program")
    print("-------------------------------")
    mainMenuChoice = input("Enter your choice : ")

    if mainMenuChoice == "1" :
        pass

    elif mainMenuChoice == "2" :
        pass

    elif mainMenuChoice == "3" :
        print("Please select the order of matrix")
        print("1 -> 2x2")
        print("2 -> 3x3")
        
        orderOfMatrixChoice = input("Enter youir choice :")
        
        if orderOfMatrixChoice == "1" :
            
            firstOrderTwoMatrix = inputMatrix.orderTwo()

            secondOrderTwoMatrix = inputMatrix.orderTwo()

            res = matrixOperations.multiply(firstOrderTwoMatrix , secondOrderTwoMatrix)

            print(res)
            
            

        elif orderOfMatrixChoice == "2" :
            orderThreeMatrix = inputMatrix.orderThree()

        else:
            print("Invalid input")
        
       


    elif mainMenuChoice == "4" :
        pass

    # Finding determinant of matrix
    elif mainMenuChoice == "5" :
        print("Please select the order of matrix")
        print("1 -> 2x2")
        print("2 -> 3x3")
        orderOfMatrixChoice = input("Enter youir choice :")
        
        if orderOfMatrixChoice == "1" :
            orderTwoMatrix = inputMatrix.orderTwo()
            det = determinant.orderTwo(orderTwoMatrix)
            print("Determinant of given matrix is :")
            print(det)

        elif orderOfMatrixChoice == "2" :
            orderThreeMatrix = inputMatrix.orderThree()
            det = determinant.orderThree(orderThreeMatrix)
            print("Determinant of give matrix is : ")
            print(det)

        else :
            print("Invalid input ( Only order 2x2 and 3x3 is allowed )")

    elif mainMenuChoice == "6" :
        print("1 - Input Rules")
        print("2 - Go back to Main Menu")

        helpChoice = input("Enter your choice :")

        if helpChoice == 1 :
            inputRules()

    elif mainMenuChoice == "7" :
        print("Settings - Comming Soon")
    
    elif mainMenuChoice == "8" :
        print("Thank you")
        break
    
    else:
        print("Invalid input. Please try again")