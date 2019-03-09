import sys
import re

#file from Arguments
inputFile = sys.argv[1]
outputFile = sys.argv[2]

#read from input
input = open(inputFile, "r")
output = open(outputFile, 'w')

List_Num = input.read()
#listOfDigits = re.findall(r"[\w']+",input)
List_Num = [x for x in List_Num if ((x!= ' ') and (x !='\n'))]
List_Num = list(map(int,List_Num))

#CODE GOES HERE
def Solver():
    global solution
    global Score
    global Eval

    point = 0
    lastsymbol = ""

    # Score += point
    List_Num.sort(reverse = True) #Sort Descending
    solution = str(List_Num[0])
    point = 0
    lastsymbol = ""
    for i in range(1,4):
        #Pertambahan
        maks_equationlocal = solution + "+" + str(List_Num[i]) 
        maks_localpoint = eval(maks_equationlocal)
        lastsymbol_local = "+"
        #Pengurangan
        localequation = solution + "-" + str(List_Num[i]) 
        localpoint = eval(localequation) 
        if(abs(localpoint-24) < abs(maks_localpoint-24)):
            maks_localpoint = localpoint
            maks_equationlocal = localequation
            lastsymbol_local = "-"
        #Perkalian
        localequation = solution + "*" + str(List_Num[i]) 
        localpoint = eval(localequation) 
        if(abs(localpoint-24) < abs(maks_localpoint-24)):
            maks_localpoint = localpoint
            maks_equationlocal = localequation
            lastsymbol_local = "*"
        if(lastsymbol == "+" or lastsymbol == "-"):
            localequation = "(" + solution + ")*" + str(List_Num[i]) 
            localpoint = eval(localequation) 
            if(abs(localpoint-24) < abs(maks_localpoint-24)):
                maks_localpoint = localpoint
                maks_equationlocal = localequation
                lastsymbol_local = "*"
        #Pembagian
        localequation = solution + "/" + str(List_Num[i]) 
        localpoint = eval(localequation)
        if(abs(localpoint-24) < abs(maks_localpoint-24)):
            maks_localpoint = localpoint
            maks_equationlocal = localequation
            lastsymbol_local = "/"
        if(lastsymbol == "+" or lastsymbol == "-"):
            localequation = "(" + solution + ")/" + str(List_Num[i]) 
            localpoint = eval(localequation) 
            if(abs(localpoint-24) < abs(maks_localpoint-24)):
                maks_localpoint = localpoint
                maks_equationlocal = localequation
                lastsymbol_local = "/"
        solution = maks_equationlocal
        maks_global = maks_localpoint
        if(lastsymbol_local == "+"):
            point += 5
        elif(lastsymbol_local == "-"):
            point += 4
        elif(lastsymbol_local == "*"):
            point += 3
        elif(lastsymbol_local == "/"):
            point += 2
    point -= abs(maks_global - 24) - solution.count("(")
    Score = point
    Eval = eval(solution)

#CODE GOES HERE

Solver()
output.write(solution)

input.close()
output.close()