# ========== Functions ==========

# If the file does not exist, it creates a new file
def CreateFile():
    file = open("to_do_list.txt", "a")
    file.close()
    
# It counts the number of lines in the file and return with it
def CountFileLines():
    file = open("to_do_list.txt", "r")
    NumOfLines = len(file.readlines())                  
    file.close()
    return NumOfLines

# Makes the list of the items
def ListItems():
    file = open("to_do_list.txt", "r")              # Open the file in 'read' mode
    Content = file.read()                           # Copy the file content in a variable
    print("You saved the following to-do items:")
    print(Content)
    file.close()        

# Adds new items to the file
def AddItems(numofilnes):
    file = open("to_do_list.txt", "a")              # Open the file in 'append' mode        
    NewContent = input("Add an item: ")
    file.write(str(numofilnes+1) + ". " + "[ ] " + str(NewContent) + "\n")      # Writes the line to the file
    file.close()
    print("Item added.")
    file.close()

# Marks the items with 'x'
def MarkItems():
    file = open("to_do_list.txt", "r+")
    Lines = file.readlines()
    file.close()
    MarkedLine = len(Lines) + 1                             # It necessary to step into the while loop
    while MarkedLine > len(Lines) or MarkedLine < 1:        # If the index bigger, then the number of lines...
        MarkedLine = int(input("Which one you want to mark as completed: "))
        if MarkedLine > len(Lines) or MarkedLine <1:
            print("There is no such index!")
    String = list(Lines[MarkedLine-1])                      # Makes a list from the string for the operations
    String[4] = "x"                                         # Put an 'x' to the marker place
    Lines[MarkedLine-1] = "".join(String)                   # Joins the characters to a string
    file = open("to_do_list.txt", "w")
    for i in range(len(Lines)):
        file.write(Lines[i])                                # Writes the lines to the file
    file.close()

# Unmarks the items
def UnMarkItems():    
    file = open("to_do_list.txt", "r")
    Lines = file.readlines()
    file.close()
    MarkedLine = len(Lines) + 1                             # It necessary to step into the while loop
    while MarkedLine > len(Lines) or MarkedLine < 1:        # If the index bigger, then the number of lines...
        MarkedLine = int(input("Which one you want to unmark as not completed: "))
        if MarkedLine > len(Lines) or MarkedLine <1:
            print("There is no such index!")
    String = list(Lines[MarkedLine-1])                      # Makes a list from the string for the operations
    String[4] = " "                                         # Remove the 'x' from the marker place
    Lines[MarkedLine-1] = "".join(String)                   # Joins the characters to a string
    file = open("to_do_list.txt", "w")
    for i in range(len(Lines)):
        file.write(Lines[i])                                # Writes the lines to the file
    file.close()

# Unmarks all items
def ArchiveItems():
    print("All completed tasks got deleted.")
    file = open("to_do_list.txt", "r+")
    Lines = file.readlines()
    file.close()
    for i in range(len(Lines)):
        String = list(Lines[i])
        String[4] = " "
        Lines[i] = "".join(String)
    file = open("to_do_list.txt", "w")
    for i in range(len(Lines)):
        file.write(Lines[i])
    file.close()

# Handle the input commands
def InputCommand():
    CreateFile()
    while True:
        NumOfLines = CountFileLines()
        Command = input("Please specify a command [list, add, mark, unmark, archive, exit]: ")
        if Command == "list" or Command == "List":
            ListItems()
        elif Command == "add" or Command == "Add":
            AddItems(NumOfLines)
        elif Command == "mark" or Command == "Mark":
            ListItems()
            MarkItems()
        elif Command == "unmark" or Command == "Unmark":
            ListItems()
            UnMarkItems()
        elif Command == "archive" or Command == "Archive":
            ArchiveItems()
        elif Command == "exit" or Command == "Exit":
            quit()
        else:
            print("Unknown command!")


# ========== Main ==========

InputCommand()
