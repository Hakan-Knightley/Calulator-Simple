#imports
import math
# Assigning Variables
number=[]
strings=["first","second"]
operations_front_end = ["Add","Subtract","Divide","Multiply"]
operations_back_end =["+","-","/","*"]
#Lists

operation = ""
result=""
#strings

again=True
#booleans

#subroutines
def Set_Numbers(number,strings):
    for i in range(0,2):
        number[i]=(str(input("Enter your "+strings[i]+" number.")))
        try:
            int(number[i])
        except:
            while (number[i]).isnumeric()==False:
                number[i] = str(input("Please enter a valid integer(0-9)."))
            number[i]= int(number[i])
    return number
#Gets number 1 and number 2

def Set_Operation(words,characters):
    count=0
    choice=" "
    print("Select which operation you would like to do:")
    for i in words:
        print(str(count+1)+":",words[count],"\n")
        count+=1
    while choice.isnumeric() == False or (choice.isnumeric() == True and (int(choice)< 1 or int(choice) > 4)):
        choice=str(input("Enter a number from 1 to 4"))
    choice=int(choice) - 1
    return characters[choice]
#Gets mathematical operations

def Do_Operation(number,operation):
    result=(str(number[0])+operation+str(number[1]))
    result= result.replace("'"," ")
    try:
        eval(result)
    except:
        result="Undefined"
    else:
        result=( result+ " = " + str(math.trunc(eval(result))))
    return result
#Evaluates the expression
def Go_Again(again):
    valid_answer=False
    while valid_answer == False:
        again=str(input("Would you like to go again?"))
        if again.lower() == 'yes':
            again = True
            valid_answer = True
        elif again.lower() == 'no':
            again = False
            valid_answer = True
        else:
            print("Please enter 'Yes' or 'no'.")
    return again
        
while again == True:  #allows programme to repeat            
    #Calling SubRoutines and short functions
    number = Set_Numbers(number,strings)
    operation = Set_Operation(operations_front_end,operations_back_end)
    result=Do_Operation(number,operation)
    print (result+"\n")
    again = Go_Again(again)
quit() #quits programme
 
#meow
