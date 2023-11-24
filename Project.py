import csv #Will be used for importing/exporting .csv files. Also can be used for importing txt files through DictReader

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
        "manager": ["Orders Overview", "Logistics Overview","Export to file..", "Exit"]
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
               match choice:
                  case 1:
                     orders_overview()
                  case 2:
                     logistics_overview()
                  case 3:
                     export_file()
                  case 0:
                     break
                  case _:
                     print("Incorrect value.")
            elif username == "delivery": 
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
    order.update({"Name" : name, "Address" : address, "Description" : description, "Date" : date, "Price" : price, "ID" : len(orders) + 1, "Delivered" : "False"}) #Appending the order on the placeholder dictionary.
    orders.append(order) #Appending the order on the list of orders.

def import_from_file(): #Import a csv or txt file into the orders list
    file_type = input("What file type would you like to input? csv/txt: ")
    file_type.strip()
    if file_type.lower() == "csv":
        file = input("Specify the name of the file: ")
        try:
            with open(file, 'r') as csvfile:
                csvreader =   csv.DictReader(csvfile)
                for row in csvreader:
                    orders.append(row)
        except FileNotFoundError:
            print("Error: File doesn't exist.")      
    elif file_type.lower() == "txt":
        file = input("Specify the name of the file: ")
        try:
            with open(file, 'r') as txtfile:
                txtreader = csv.DictReader(txtfile)
                for row in txtreader:
                    orders.append(row)
        except FileNotFoundError:
            print("Error: File doesn't exist.")
    else:
        print("Incorrect file type. Please try again.")
    while True:
        answer = input("Would you like to import another file? Y/N: ")
        answer.strip()
        if answer.lower() == "Y":
            import_from_file()
        elif answer.lower() == "N":
            break
        else:
            print("Incorrect Value.")
            continue
        
    
def view_undelivered_orders(): #Checks the orders list for orders that have not been delivered, and prints them.
    for order in orders:
       if str(order.get("Delivered")) == "False":
        print(order)
def mark_order_as_delivered():
    for order in orders: #Printing all non-delivered orders so the deliver can check the ID of the order they delivered, to mark it as delivered.
        if str(order.get("Delivered")) == "False":
            print(order)
    try:
        delivered = int(input("Please input ID of Delivered Order: ")) #Asking for input of delivered order ID.
    except ValueError as e:
        print("You have most likely not input an integer. Please try again.")
    else:
        for order in orders:
            if int(order.get("ID")) == delivered:
                order["Delivered"] = "True"
                break
        else:
           print(f"Order with ID {delivered} either doesn't exist or has already been delivered.")
        while True:
            answer = input("Would you like to mark another delivery as Delivered? Y/N: ")
            answer.strip()
            if answer.upper() == "Y":
                mark_order_as_delivered()
            elif answer.upper() == "N":  
                break 
            else:
                print("Incorrect Value.")
                continue
def orders_overview(): #Reads the Orders list, and acts accordingly to what the manager wants
    try:
        choice = int(input("Welcome to the Orders overview. Please select one of the choices available: \n 1. No. of orders from customer \n 2. No. of orders of specific day \n 3. Total amount of orders delivered \n 0. Exit \n Input your choice: "))
    except ValueError as e:
        print("You have most likely not input an integer. Please try again.")
    else:
        match choice:
            case 1:
                name = input("Please input the name of the customer: ")
                count = 0
                for order in orders:
                    if order.get("Name") == name:
                        print(order)
                        count += 1
                print(f"Total number of orders by {name}: {count}")
            case 2:
                date = input("Please input date to see orders that day (DD/MM/YY format): ")
                count = 0
                for order in orders:
                    if order.get("Date") == date:
                        print(order)
                        count =+ 1
                print(f"Total number of orders in {date}: {count}")
            case 3:
                count = 0
                for order in orders:
                    if str(order.get("Delivered")) == "True":
                        print(order)
                        count += 1
                print(f"Total amount of orders delivered: {count}")
            case 0:
                display_options()
            case _:
                print("Choice not found.")
    while True:
        answer = input("Would you like to re-enter the Orders overview? Y/N: ")
        answer.strip()
        if answer == "Y":
            orders_overview()
        elif answer == "N":
            break
        else:
            print("Incorrect choice. Try again.")
            continue
        
   
def logistics_overview(): #Reads from the orders list and gives financial data depending on what the manager wants.
    try:
        choice = int(input("Welcome to the Logistics overview. Please select one of the choices available: \n 1. Total price of orders from customer \n 2. Total price of orders in a day \n 0. Exit \n Input your choice: "))
    except ValueError as e:
        print("You have most likely not input an integer. Please try again.")
    else:
        match choice:
            case 1:
                name = input("Please input name of customer: ")
                count = 0
                for order in orders:
                    if order.get("Name") == name:
                        count =+ int(order.get("Price"))
                print(f"Total price of all orders from {name}: {count}")                
            case 2:
                date = input("Please input date (format: DD/MM/YY): ")
                count = 0
                for order in orders:
                    if order.get("Date") == date:
                        count =+ int(order.get("Price"))
                print(f"Total price of all orders from {date}: {count}")                
            case 0:
                pass
            case _:
                print("Incorrect Value.")
                pass
    while True:
        answer = input("Would you like to re-enter the Logistics overview? Y/N: ")
        answer.strip()
        if answer == "Y":
            logistics_overview()
        elif answer == "N":
            break
        else:
            print("Incorrect choice. Try again.")
            continue
    
def export_file():
    base_filename = input("Enter the filename for the CSV export: ")
    filename = f"{base_filename}.csv"
    fieldnames = ["ID", "Name", "Address", "Description", "Date", "Price", "Delivered"]

    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #Initializing a writer object so it can export the details to a .csv file
            writer.writeheader()
            for order in orders: #Writes data
                writer.writerow({key: order[key] for key in fieldnames})

        print(f"Orders exported to {filename} successfully.")
    except Exception as e:
        print(f"Error exporting file: {e}")
        
login()   
while True: 
    answer = input(("Would you like to use the program again? Y/N: "))
    answer.strip()
    if answer.upper() == "Y":
       login()
    elif answer.upper() == "N":
       break
    else:
       print("Incorrect Value entered.")
       continue