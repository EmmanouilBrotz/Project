accounts = { #Account credentials for each user.
    "clerk" : "clerk123",
    "delivery": "delivery123",
    "manager": "manager123"
}
orders=[]
def login(): #Function for logging in. This will always run first.
    username = input("WELCOME TO THE ORDER SYSTEM\n USERNAME: ") 
    password = input("PASSWORD: ")
    username_stripped = username.strip() #Stripping the name so spaces don't matter.
    if username_stripped.lower() in accounts and password == accounts[username_stripped.lower()]: #Matching the name with all lowercase letters, cause username should not be case-sensitive. Password should be though!
        print("Login successful!")
        username = username.strip()
        display_options(username) #Transfers to the second function, in order to maintain username, so each user gets different options.
    else:
        print("Login failed. Please input correct credentials.")
def display_options(username):
    user_options = { #Options for each user, will display different stuff depending on the option.
        "clerk": ["New Order", "Import From File", "View Undelivered Orders", "Exit"],
        "delivery": ["Mark Order as Delivered", "Exit"],
        "manager": ["Orders from Customer", "Orders of Day", "Total number of orders delivered", "Total Price of Orders of Customer", "Total Price of Orders of Day", "Exit"]
    }
    print(f"Welcome, {username.capitalize()}! Your options are:") #Displays the options for different users.
    while True:
        options = user_options[username.lower()]
        for index, option in enumerate(options, start=1):
            print(f"{index if index < len(options) else 0}. {option}")
        try:
            choice = int(input("Please input choice: "))
        except ValueError as e:
            print("You have most likely not input an integer. Please try again.")
        else:
            if username == "clerk":
                match choice:
                   case 1:
                    new_order()
                   case 2:
                    import_from_file()
                   case 3:
                    view_undelivered_orders()
                   case 0:
                    break
                   case _:
                    print("Incorrect value.")
def new_order():
    print("Test1")
def import_from_file():
    print("Test2")
def view_undelivered_orders():
    print("Test3")


                     
        

    

login()
