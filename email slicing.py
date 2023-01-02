while True:
    email = input("Enter an email to slice: ")
    
    if email.count("@") == 1 and len(email[:email.index("@")]) >0 and len(email[email.index("@")+1:])>3:
        
        print("Your username is : " + email[:email.index("@")])
        
        print("Your domain is : " + email[email.index("@")+1:])
    
    else:
        print("Invalid email!")