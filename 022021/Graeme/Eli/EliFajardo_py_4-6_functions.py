print ("..Calculator..")

#exc = 1 #initializing ex
#hours = 1
#rate = 1

def computepay (hours, rate):
    #COMPUTE RATE
    if exc < 0 :
        print("\nTry again, INPUT JUST NUMBERS!!")
    else : 
        if hours > 40 :
            xT = hours - 40 #extra time
            xPay = rate * 0.5 * xT #payment of the extra time
            tPay = (hours * rate) + xPay #total payment
            #print("Pay:", tPay)
            return(tPay)
        else :
            tPay = hours * rate #regular payment
            #print("Pay:", tPay)
            return(tPay)

#INPUT HOURS
hours = input("Enter hours: ")
exc = 1 #initializing exc
try : 
    hours = float(hours)
except : 
    exc = -1
    #print("Not a number")
#INPUT RATE
rate = input ("Enter rate: ")
try :
    rate = float(rate)
except :
    exc = -1
    #print("Not a number")

payment = computepay (hours, rate)
print("Pay:", payment)






