lowrcas = False
upprc = False
special = False
num = False
leng = False
count = 0
start = input("Do you want to check your password [Y] or N: ")
mode_on = False
if start.upper() == 'Y':
    mode_on = True
else:
    mode_on = False
while mode_on == True:
    print(" RULES \n Checkpoint(1) Length must be more than or equal to 10 and less than or equal 18.\n Checkpoint(2) must contain lowercase letters. \n Checkpoint(3) must contain uppercase letters. \n Checkpoint(4) must contain numbers. \n Checkpoint(5) must contain special characters.")
    pswd = input('Enter your password: ')
    for letter in pswd:
        if  letter in 'abcdefghijklmnopqrstuvwxyz':
            lowrcas= True
        elif letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            upprc= True 
        elif letter in '123456789':
            num= True
        elif letter in '!@~#$%^&*()_+=/?':
            special= True
    if len(pswd) > 9 and  len(pswd) <= 18:
        print("Checkpoint(1) PASSED✅")
        leng = True
        count =count+1
    if leng == False:
        print("Checkpoint(1) FAILED, Because password must be must more than or equal to 10 and less than or equal 18❌.")
    if lowrcas == True:
        print("Checkpoint(2) PASSED✅")
        count =count+1
    if lowrcas == False:
        print('Checkpoint(2) FAILED, Because password must contain lowercase❌.')
    if upprc == True:
        print("Checkpoint(3) PASSED✅")
        count =count+1
    if upprc == False:
        print('Checkpoint(3) FAILED, Because password must contain uppercase❌.')
    if num == True:
        print("Checkpoint(4) PASSED✅")
        count =count+1
    if num == False:
        print('Checkpoint(4) FAILED, Because password must contain numbers❌.')
    if special == True:
        print("Checkpoint(5) PASSED✅")
        count =count+1
    if special == False:
        print('Checkpoint(5) FAILED, Because password must contain special characters❌.')
    if count == 5:
        print("Congratulations your password is eligible to be used✅")
    if count < 5:
        print("Sorry your password not eligible to be used❌")
    else:
        mode_on = False
    mode_on=False