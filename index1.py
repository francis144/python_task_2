#get user details
def get_info():
    first_name=input("Enter your First Name below: ")
    second_name=input("Enter your Second Name below: ")
    user_email=input("Enter your Email Address below: ")
    
    info = [first_name,second_name,user_email]
    
    return info
#generate password using details
def gen_password(info):
    
    characters =string.asci_letters
    length =5
    randon_password = ''.join(randon_choice(characters) for i in range(length))
    
    password = str(info[0][0:2] + info[1][-2:] + randon_password)
    
    return password

#main program
status = True
put = []

while status:
    #get user details
    info = get_user()
    
    #show generated password
    password = gen_password(info)
    print ("Your password is: " + str(password))
    
    #ask if he would like to continue
    password_like = input(str("do you like to generate password. If yes enter Yes if no, enter No and supply your"))
    password_loop = True
    
    while password_loop:
        if password_like =="YES":
            #add password to user details
            details.append(password)
            
            #add user details to overall container
            put.append(info)
            
            password_loop = False:
            
        else:
            
            #enter a password longer than or equal to 7
            user_password = input(str("Enter password Longer tha or equal to 7"))              
            #password  length loop
            pass_len = True
            
            while pass_len:
                if  len(user_password) >= 7:
                
                 #add password to user details
                    info.append(user_password)
                
                #add user details to container
                    put.append(info)
                
                #break out of password length check loop
                    password_loop = False
                else:
                    print("Your password is less than 7")
                    user_password = input(str("Enter password Longer than or equal to 7"))
                #new user
                    new_user = input(str("would you like to enter a new user? YES or NO"))
                    if (new_user == "No"):
                        status = False
                        for item in put:
                        print(item)
                    else:
                        status=True 