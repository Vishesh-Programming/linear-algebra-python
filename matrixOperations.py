def addition(x,y):
    pass

def subtraction(x,y):
    pass

def multiply(x,y,res=[]):

    try :
        # creating res matrix with value 0
        for i in x :
            res.append([])
            
        for i in range(len(y)):
            for j in range(len(y[0])) :
                res[i].append(0)
            
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    res[i][j] += x[i][k] * y[k][i]
        return res  # Return the multiplication

    except Exception as e :
        print("Error occured")
        print("Error ::" , e)
        return False


