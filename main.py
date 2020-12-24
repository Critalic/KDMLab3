reverse = [] #Needed for isDouble
listOfvalues = [ #needed for the table of validity
                [0, 0, 0],
                [0, 0, 1],
                [0, 1, 0],
                [0, 1, 1],
                [1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
            ]

# the function input
function = [ ]
code = ""
def convertInput ():
    code= input("Enter your code (should consist of 8 numbers (1 or 0) without spaces): ")
    if(len(code)!=8): raise ValueError("The code must only contain 8 digits")

    for o in range (len(code)):
        if(int(code[0])!= 1 or int(code[0])!= 1 ):
            raise ValueError("Check your input")
            break

        function.append(int(code[o]))


def printer (listOfvalues, function):

        header = "| X | Y | Z | F |"
        underLine = "____________________"


        print (header)
        print(underLine)

        for i in range (len(listOfvalues)):
                print("|", listOfvalues[i][0], "|",  listOfvalues[i][1], "|", listOfvalues[i][2], "|", function[i], "|")

        print(underLine)

def keepsZero (listOfvalues):
        if(listOfvalues[0] ==0): print("The given function keeps 0")
        else: print("The given function doesn't keep 0")

def keepsOne (listOfvalues) :
        if (listOfvalues[7] == 1):
                print("The given function keeps 1")
        else:
                print("The given function doesn't keep 1")

def isDouble (function):

        for i in range (len(function)):
                if(function[i]==1): reverse.append(0)
                elif(function[i]==0): reverse.append(1)
        print("The given function is dual to ", reverse)
        return reverse

def isSelfDual (function):
        isDouble(function)
        if(function == reverse): print("The given function is self dual")
        print("The given function is not self dual")

def dknf(listOfvalues, function):
    print( "DKNF:",end = " " )
    for i in range (len(function)):
            values  = []
            if(function[i]==0) :
                    for b in range (len(listOfvalues[i])):
                            if(b==0 and listOfvalues[i][b]==0 ):values.append("x")
                            if (b == 0 and listOfvalues[i][b] == 1):values.append("!x")
                            if (b == 1 and listOfvalues[i][b] == 0):values.append("y")
                            if (b == 1 and listOfvalues[i][b] == 1):values.append("!y")
                            if (b == 2 and listOfvalues[i][b] == 1):values.append("!z")
                            if (b == 2 and listOfvalues[i][b] == 0):values.append("z")
                    print("(", values[0],"+", values[1], "+", values[2], end=") ")
    print( " ")

def ddnf(listOfvalues, function):

    print("DDNF:", end=" ")
    values = []
    for i in range (len(function)):
            if(function[i]==1) :
                    for b in range (len(listOfvalues[i])):
                            if(b==0 and listOfvalues[i][b]==0 ):values.append("!x")
                            if (b == 0 and listOfvalues[i][b] == 1):values.append("x")
                            if (b == 1 and listOfvalues[i][b] == 0):values.append("!y")
                            if (b == 1 and listOfvalues[i][b] == 1):values.append("y")
                            if (b == 2 and listOfvalues[i][b] == 1):values.append("z")
                            if (b == 2 and listOfvalues[i][b] == 0):values.append("!z")
    i = len(values)
    b=0
    while (i >=3):
            if (i != 3):
                    print("(", values[b], "*", values[b+1], "*", values[b+2 ], end=" ) + ")
            elif (i == 3):
                    print("(", values[b], "*", values[b+1], "*", values[b+2], end=" ) ")
            i -=3
            b +=3
    print(" ")


def sum_mod_2(a, b):
    return int(not a == b)

def conjunction(a, b):
    return int(a == b == 1)

def make_pascal_triangle(f):
    data = [f]

    for i in range(len(f)-1,0,-1):
        row = []
        for j in range(0,i):
            row.append(sum_mod_2(data[-1][j],data[-1][j+1]))
        data.append(row)

    return data


def is_linear(func, base):

    if sum(func) < 3:
        return False

    triangle = make_pascal_triangle(func)

    for i in range(1, len(triangle)):
        if triangle[i][0] == 1 and base[i][0] + base[i][1] + base[i][2] != 1:
            return False

    return True

#Execution
try:
        convertInput()
except Exception as e:
        print(e)
        exit()

printer(listOfvalues, function)
keepsZero (listOfvalues)
keepsOne (listOfvalues)
isSelfDual(function)
print("The given function is linear:", is_linear(function, listOfvalues))
ddnf(listOfvalues,function)
dknf(listOfvalues, function)