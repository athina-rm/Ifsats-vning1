g_u_name = input("Username : ")
g_pwd = input("Password : ")
u_name="user123"
pwd="safetYFirst"
if g_u_name==u_name :
    if g_pwd == pwd:
        print ("Du är inloggad")
    else :
        print ("Fel lösenord!")
else :
    print ("Fel användarnamn")
