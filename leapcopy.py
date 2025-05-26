print("wellcome back rho i am very existed")

def bmi_calculator(height,weight):
    heightin_cm=height/100
    bmi=weight/heightin_cm**2
    
    return float(f"{bmi:.2f}")

bmioutput=bmi_calculator(160,63)
print(bmioutput)

def bmi_validation(bmi):
    if bmi<18.5:
        return "UnderWeigth"
    elif bmi>=18.5 and bmi< 25:
        return "Normal Weight"
    elif bmi>25 and bmi <30:
        return "Over Weight"
    elif bmi>30 and bmi<45:
        return "Obesity"
    elif bmi<0 or bmi >45:
        return "enter proper bmi"
    
print(bmi_validation(bmioutput)   )

# for num in range(1,6):
#     print(num)

# i=6
# print("while loop")    
# while i<=10:
#     print(i)    
#     i+=1
    
    
# for num in range(10,0,-1):
#     print (num)   

# down=10
# print("while")
# while down>=1:
#     print(down)
#     down-=1
sum=0
n=10
# for i in range(1,n+1):
#     sum+=i
# print(sum)
i=0
while i<=10:
    sum+=i
    i+=1
    
print(sum)    