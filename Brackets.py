"""
This Program will check for Matching brackets.

**Only valid for Round brackets.
**If any opening bracket present after any closing bracket ..invalid expression

"""
input_exp = input("Enter the Expression: \n")
numberOfOpeningBrackets = input_exp.count("(")
numberOfClosingBrackets = input_exp.count(")")

if numberOfOpeningBrackets == 0 and numberOfClosingBrackets == 0:
    print("Expression has NO brackets!!")
else:
    #Now we will check there should be no opening brackets after last closing bracket
    lastOpeningBracket = input_exp.rfind("(")
    lastClosingBracket = input_exp.rfind(")")
    if lastClosingBracket < lastOpeningBracket:
        print("Invalid expression")
    else:
        if numberOfClosingBrackets == numberOfOpeningBrackets:
            print("Matching Brackets!!")
        else:
            print("No Matching Brackets!!")



