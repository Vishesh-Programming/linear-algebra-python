import inputMatrix
print("Linear Algebra")

# options 

# 1 - Addition of matrix
# 2 - Subtraction of matrix
# 3 - Multiplication of matrix
# 4 - Square of matrix
# 5 - Determinant of matrix

while True :
    print()
    print("Operations available : ")
    print("-------------------------------")
    print("1 -> Addition of matrix")
    print("2 -> Subtraction of matrix")
    print("3 -> Multiplication of matrix")
    print("4 -> Square of matrix")
    print("5 -> Determinant of matrix")
    print("6 -> Help")
    print("7 -> Settings")
    print("8 -> Exit program")
    print("-------------------------------")
    ch = input("Enter your choice : ")

    if ch == "5" :
        print("Please select the order of matrix")
        print("1 -> 2x2")
        print("2 -> 3x3")
        ch = input("Enter youir choice :")
        
        if ch == "1" :
            mat = inputMatrix.orderTwo()
            det = (mat[0][0] * mat[1][1] ) -  (mat[1][0] * mat[0][1] )

            print("Determinant of given matrix is :")
            print(det)
  
    
    elif ch == "8" :
        print("Thank you")
        break
    
    else:
        print("Invalid input. Please try again")