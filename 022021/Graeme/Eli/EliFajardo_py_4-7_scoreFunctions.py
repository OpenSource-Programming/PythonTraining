#This program return grades based on given scores

# F U N C T  I O N S
def computegrade (score):
    #RETURN GRADE
    if 0 <= score <= 1:
            if score >= 0.9:
                return("A")
            elif score >= 0.8:
                return ("B")
            elif score >= 0.7:
                return ("C")
            elif score >= 0.6:
                return ("D")
            elif score < 0.6:
                return ("F")
    else:
        print ("Score is out of range, try again")

print ("::: EASY GRADES :::")

#INPUT SCORE
score = 1
score = input ("Enter score: ")
try:
    score = float(score)
except:
    score = -1 
    print ("Try input numbers")
    exit(score)

grade = computegrade(score)
print ("Grade:", grade)
    