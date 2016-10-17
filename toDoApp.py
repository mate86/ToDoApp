# ========== Functions ==========

def CreateFile():
    try:
        file = open("to_do_list.txt", "a")              # If the file does not exist, it creates a new file
        file.close()
    except:
        file.close()

def CountFileLines():
    file = open("to_do_list.txt", "r")
    NumOfLines = len(file.readlines())                  # Count the number of lines in the file
    file.close()
    return NumOfLines

def ListItems():
    try:
        file = open("to_do_list.txt", "r")              # Open the file in 'read' mode
        Content = file.read()        
        print("You saved the following to-do items:")
        print(Content)
        file.close()        
    except:
        file.close()

def AddItems(numofilnes):
    try:
        file = open("to_do_list.txt", "a")              # Open the file in 'append' mode        
        NewContent = input("Add an item: ")
        file.write(str(numofilnes+1) + ". " + "[ ] " + str(NewContent) + "\n")
        file.close()
        print("Item added.")
        file.close()
    except:
        file.close()

#def MarkItems():


#def ArchiveItems():


def InputCommand():
    CreateFile()
    #Command = input("Please specify a command [list, add, mark, archive]: ")
    while True:
        NumOfLines = CountFileLines()
        Command = input("Please specify a command [list, add, mark, archive]: ")
        if Command == "list" or Command == "List":
            ListItems()
        elif Command == "add" or Command == "Add":
            AddItems(NumOfLines)
        elif Command == "mark" or Command == "Mark":
            MarkItems()
        elif Command == "archive" or Command == "Archive":
            ArchiveItems()
        else:
            break


# ========== Main ==========

InputCommand()
