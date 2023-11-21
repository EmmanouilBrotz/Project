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
            choice = int(input("Please input choice: ")) #Asking for user input for the feature they want to use.
        except ValueError as e:
            print("You have most likely not input an integer. Please try again.")
        else:
            if username == "clerk": #Match user input with choice.
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
            elif username == "manager":
               pass
            else: #Last username should be Delivery anyway. It should be impossible to get here with a different username.
               match choice:
                  case 1:
                     mark_order_as_delivered()
                  case 0:
                     break
                  case _:
                     print("Incorrect value.")
def new_order(): 
    order = {} #Initializing a dictionary for the order, which will then be implemented into the orders list which is on the global scope.
    name = input("NEW ORDER:\n Name of customer: ") #The next 5 LoC are details about the order.
    address = input("Address of customer: ")
    description = input("Description of order of customer: ")
    date = input("Date of order (INPUT IN DD/MM/YY): ")
    price = input("Price of order: ")
    order.update({"Name" : name, "Address" : address, "Description" : description, "Date" : date, "Price" : price, "ID" : len(orders) + 1, "Delivered" : False}) #Appending the order on the placeholder dictionary.
    orders.append(order) #Appending the order on the list of orders.

def import_from_file(): #WIP
    print("Test2")
def view_undelivered_orders(): #Checks the orders list for orders that have not been delivered, and prints them.
    for order in orders:
       if order.get("Delivered") == False:
        print(order)
def mark_order_as_delivered():
    while True:
        for order in orders: #Printing all non-delivered orders so the deliver can check the ID of the order they delivered, to mark it as delivered.
            if order.get("Delivered") == False:
                print(order)
        try:
            delivered = int(input("Please input ID of Delivered Order: ")) #Asking for input of delivered order ID.
        except ValueError as e:
            print("You have most likely not input an integer. Please try again.")
        else:
            for order in orders:
                if order.get("ID") == delivered:
                    order["Delivered"] = True
            answer = input("Would you like to mark another delivery as Delivered? Y/N: ")
            if answer == "Y":
                 mark_order_as_delivered()
            elif answer == "N":  
               break 
            else:
                print("Incorrect Value.")
                break
           
while True: 
    login()
    answer = input(("Would you like to use the program again? Y/N: "))
    if answer == "Y":
       continue
    elif answer == "N":
       break
    else:
       print("Incorrect Value entered. Will exit program.")