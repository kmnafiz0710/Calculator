usernames={"nafiz","khaled","sumiya","saiful","masud"}
while True:
    username=input("Enter your username: ".lower())
    if username in usernames:
        print("Your name is correct.")
        break
    else:
        print("Your username is invalid.")