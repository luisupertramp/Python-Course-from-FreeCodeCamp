def arithmetic_arranger(problems, showResults=False) :

    # Length validation
    if len(problems) > 5 :
        return("Error: Too many problems.")

    printLineX = ''
    printLineY = ''
    printLineD = ''
    printLineR = ''

    # Loop over problems
    for index, problem in enumerate(problems) :

        # Segmentation of problems by operators and operands
        probList = problem.split()

        operator = probList[1]
        xString = probList[0]
        yString = probList[2]

        # *** VALIDATION BEGINS ***

        # Validate operators
        if operator != "+" and operator != "-" :
            return("Error: Operator must be '+' or '-'.")
            
        # Validate operands

        if len(xString) > 4 or len(yString) > 4 :
            return("Error: Numbers cannot be more than four digits.")
            
        try : 
            x = int(probList[0])
            y = int(probList[2])
        except :
            return("Error: Numbers must only contain digits.")
            

        # *** CONCATENATE OPERATIONS ***

        longest = len(xString)

        # Concatenate operands depending on which one is the longest
        if len(xString) > len(yString) :
            lenDiffs = len(xString) - len(yString) # get difference between lengths

            printLineX += 2*' ' + xString # Concatenate print lines for X
            printLineY += operator + ' ' + lenDiffs*' ' + yString # Concatenate print lines for Y
        else:
            longest = len(yString)
            lenDiffs = len(yString) - len(xString)

            printLineX += 2*' ' + lenDiffs*' ' + xString # Concatenate print lines for X
            printLineY += operator + ' ' + yString # Concatenate print lines for Y

        # Concatenate print line for dashes
        printLineD += (longest+2)*'-'

        # Concatenate print line for results
        if showResults :
            rString = str(x+y) if operator == '+' else str(x-y)
            lenDiffs = longest+2 - len(rString)
            printLineR += lenDiffs*' ' + rString

        if index < len(problems)-1 :
            printLineX += 4*' '
            printLineY += 4*' '
            printLineD += 4*' '
            printLineR += 4*' '
    
    # *** PRINT RESULTS ***
    if showResults:
        return (printLineX + '\n' + printLineY + '\n' + printLineD + '\n' +
            printLineR)
    else:
        return (printLineX + '\n' + printLineY + '\n' + printLineD)


# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))