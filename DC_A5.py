#-------------------------------------------------#
# Title: Assignmnet 5 Homework
# Dev:   Daniel Carrasco
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
objFile = open("ToDo.txt","r")
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------




# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"
	
file = open("ToDo.txt","r")
strData = ""
dicRow = {}
lstTable = []
count = -1
count2 = -1 #I may be able to do this with one counter , so will come back to this when time is available

for row in file:
    task,priority = row.strip().split(',')  #strip helped with formatting and split splits row in two variables, Priority and Task when python find a comma. Strip helped with formatting
    dicRow = {task:priority}
    lstTable.append(dicRow)
    count = count + 1
print(lstTable)
print (count)
file.close

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Showing the current Items in table '\n' ")
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        newRow = {}
        newTask = input("Enter new Task")
        newPriority = input("Set Priority of new task (high or low") # Can add if loop for error handling
        newRow = {newTask: newPriority} # new dictionary
        lstTable.append(newRow) #adding new dictionary to existing table lstTable
        count = count+1 #counter for row numbers
        print("The following has been added to the list '\n' ")
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        print(lstTable) #show user existing table
        for rows in lstTable:
            count2 = count2 + 1 #to count number of rows
            print('\n' + str(count2) + "  " + str(rows)) #displays row # and contents
        remove =input("Which task # do you want to delete?")
        del lstTable[int(remove)] #deletes desired row numner
        count2 = -1  # this resets the counter so you don't call an out of range index
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        file = open('ToDo.txt','w')
        for rows in lstTable:
            readline = rows.items()
            for key,value in readline:
                print(key +","+ value + "\n")
                file.write(key + ","+ value+"\n")
        file.close()
        continue
    elif (strChoice == '5'):
        break #and Exit the program

