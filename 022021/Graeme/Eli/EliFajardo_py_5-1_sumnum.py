print("Enter a number, when you done type 'done'")
sum = 0
loop = 1
count = 0
while loop >= 1 : 
    line = input ("Enter number: ")
    try:
        line = float(line)
        #print("chido 1")
        loop = 1
    except:
        if line == 'done': 
            print(" ")
            break
        else: 
            #print("chido 2")
            loop = 2
            
    if loop == 2 :
        print("\nTry again, INPUT JUST NUMBERS!!\n")
        continue
    else : 
        count = count + 1
        sum = sum + line
print ("TOTAL:", sum, "\nCOUNT:", count, "\nAVERAGE", sum/count)

