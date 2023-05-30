import random
lst1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst3 = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','/','!','@','#','$','%','^','&','*','(',')','_','+','=','-','/','?','?']
lst4 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
full_pass = ''
def generator(mylst):
    w = random.choices(population=mylst,k=int(length))
    print("Your Password is: ")
    for l in w:
        print(l,end='')
mylst= lst1+lst2
start = input(print("Do you want to generate a password [Y] or N: "))
if start.upper() == 'Y':
    mode_on = True
else:
    mode_on = False
while mode_on:
    upperlower = input(print("Do you want your password to be in upper only Y or [N]: "))
    numbers = input(print("Do you want numbers in your password [Y] or N: "))
    signs = input(print("Do you want signs like($#@...etc) in your password [Y] or N: "))
    length = input(print("Enter your password length prefared from (10 to 18): "))
    if upperlower.upper() == 'Y':
        mylst = lst1
    if numbers.upper() == 'Y':
        mylst.extend(lst4)
    if signs.upper() == 'Y':
        mylst.extend(lst3)
    else:
        mode_on = False
    generator(mylst)
    break