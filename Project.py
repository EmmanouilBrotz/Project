accounts = { #Account credentials for each user.
    "clerk" : "clerk123",
    "delivery": "delivery123",
    "manager": "manager123"
}
def login(): #Function for logging in. This will always run first.
    username = input("WELCOME TO THE ORDER SYSTEM\n USERNAME: ") 
    password = input("PASSWORD: ")
    username_stripped = username.strip() #Stripping the name so spaces don't matter.
    if username_stripped.lower() in accounts and password == accounts[username_stripped.lower()]: #Matching the name with all lowercase letters, cause username should not be case-sensitive. Password should be though!
        print("Login successful!")
        display_options(username) #Transfers to the second function, in order to maintain username, so each user gets different options.
    else:
        print("Login failed. Please input correct credentials.")
def display_options(username):
    user_options = { #Options for each user, will display different stuff depending on the option.
        "clerk": ["Option 1", "Option 2", "Option 3", "Exit"],
        "delivery": ["Option A", "Option B", "Option C", "Exit"],
        "manager": ["Option X", "Option Y", "Option Z", "Exit"]
    }
    while True:
        print(f"Welcome, {username.capitalize()}! Your options are:")
        for index, option in enumerate(user_options[username.lower()], start=1):
            print(f"{index}. {option}")
        break
    

login()
