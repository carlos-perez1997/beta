#Script description:
'''
1.Get 2 numbers (float or integer)
2.Show main menu: (1). Add, (2). sub, (3). mul, (4). Div
3.select an option
4.create a function to get the result accordig with the opt
other: clear screen
'''
import os 

def calc1(x,y,z):
    if (z == '1'):
        ans = x + y

    if (z == '2'):
        ans = x - y 

    if (z == '3'):
        ans = x * y
                
    if (z == '4'):
        if y == 0:
            return "No dividir x 0"
        ans = x / y
        return ans
    elif (z == '5'):
        if y == 0:
            division = "No dividir x 0"
        else:
            division = x / y
        return (f"add: ({x + y}) / sub: ({x - y}) / mult: ({x * y}) / div: ({division})")
    
    return "numeros validos del 1 al 5"

def calc2(x,y,z):
    if (z == '1'):
          ans = x + y
    else:
          if (z == '2'):
           ans = x - y
          else:
              if (z == '3'):
                  ans = x * y
              else:
                    if (z == '4'):
                        if y == 0:
                            return " No dividir x 0"
                        ans = x / y
                    else:
                        if (z == '5'):
                            if y == 0:
                                division = "no dividir x 0"
                            else:
                                division = x / y
                            return (f"Add: ({x + y}) / Sub: ({x - y}) / Mult: ({x * y}) / Div: ({division})")
    
                        return "numeros validos del 1 al 5"
    return ans

def calc3(x,y,z):
    if (z == '1'):
        ans = x + y

    elif (z == '2'):
        ans = x - y 

    elif (z == '3'):
         ans = x * y

    elif (z == '4'):
        if y == 0:
            return"no dividir x 0"  
        ans = x / y
    elif (z == '5'):
        if y == 0:
            division = "no dividir x 0"
        else :
            division = x / y
        return (f"add: ({x + y}) / sub: ({x - y}) / mul: ({x * y}) / div:({division})")
    else:
        return "numeros validos del 1 al 5"
    

    return ans

##### main ##############################
num1 = float(input('press first number:'))
num2 = float(input('press second number:'))


print("### MAIN MENU ###")
print("[1]. Add")
print("[2]. sub")
print("[3]. mult")
print("[4]. Div")
print("[5]. all operations")
opt = input("::. pres any option: ")
#print(type(opt))
#os.system('pause')

res1 = calc1(num1, num2, opt)
print(f"The result is: {res1}")

res2 = calc2(num1, num2, opt)
print(f"The result is: {res2}")

res3 = calc3(num1, num2, opt)
print(f"The result is: {res3}")