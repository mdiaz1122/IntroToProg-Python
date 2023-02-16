# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Michelle Diaz,2.14.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # A data file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
lstRow = []  # A list that stores each dictionary entry for printing
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open(strFile, 'r')
    for row in objFile:
        strData = row.split(',')
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except:
    print()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        if not len(lstTable):
            print("There are no tasks to list. Please choose another option.")
            input("Press Enter to continue...")
        else:
            for row in lstTable:
                print(row)
            input("Press Enter to continue...")
            continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("Enter a task: ")
        strPriority = input("Enter the task priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority.strip()}
        lstTable.append(dicRow)
        input("Press Enter to continue...")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        task = input("What task would you like to delete?: ")
        for row in range(len(lstTable)):
            if lstTable[row]['Task'] == task:
                del lstTable[row]
                print("\nThe " + task + " task has been deleted.")
                input("Press Enter to continue...")
                break
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        txtFile = open("ToDoList.txt", "w")
        for row in lstTable:
            txtFile.write(str(row["Task"]) + ',' + str(row["Priority"]) + '\n')
        txtFile.close()
        print("Data was saved to ToDoList.txt")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting program...")
        break  # and Exit the program
