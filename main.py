#Expense Tracker Project

expensesList=[]  # list of all expenses in form of dictionary
print("Welcome to Expense Tracker")
 

while True:
    print("========Menu========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total spending")
    print("4. Exit")

    choice=int(input("Please enter your choice (1-4): "))

    #Add Expense
    if (choice==1):
        date=input("At which date you spend money:")
        category=input("Enter the category of expense (e.g., Food, Transport, Entertainment,Makeup,Shopping): ")
        description=input("Enter a brief description of the expense: ")
        amount=float(input("Enter the amount:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expense)
        print("\n expense added successfully!")

    #View All Expenses
    elif (choice==2):
        if (len(expensesList)==0):
            print("\n No expenses recorded yet., Please spend some money first! ,Miss Stingy")
        else:
            print("\n ====== Here Is All Your Expenses======")
            count=1
            for eachkharcha in expensesList:
                print(f" Kharcha Number {count} -> {eachkharcha['date']}, {eachkharcha['category']}, {eachkharcha['description']}, {eachkharcha['amount']}")
                count+=1

     # View Total Spending
    elif (choice==3):
        total=0
        for eachkharcha in expensesList:
            total+=eachkharcha['amount']
        print("\n Total Kharcha =",total)

    # Exit
    elif (choice==4):
        print("Exiting Expense Tracker. Goodbye! and Thankyou for using our system")
        break   # to come from while loop

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")        

                





 



     







