
master_pwd = input("What is your master password?: ")

def add():
    
    name = input("Account Name:")
    pwd = input("Password:")


    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

def view():
     with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:", user ,"," , "Password:", passw)



while True:
    mode = input("Do you want to add the password ? or view the existing ones or press q to quit (add/view):").lower()

    if mode == "q" :
        break

    if mode == "add":
        add()
        

    elif mode == "view":
        view()

    else:
        print("Invalid command!!")
        continue