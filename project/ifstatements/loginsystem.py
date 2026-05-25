username="admin"
password="vaishu"
u=input()
p=input()

if u==username:
    if p==password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Password")
        