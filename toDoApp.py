# ========== Functions ==========

def ListItems():
    try:
        file = open("to_do_list.txt", "r")          # Open the file in 'append' mode
        Content = file.read()
        print("You saved the following to-do items:")
        print(Content)
        file.close()        
    except:
        file.close()

def AddItems():
    try:
        file = open("to_do_list.txt", "a")          # Open the file in 'append' mode
        file.write(input("Add an item: "))
        file.close()
        print("Item added.")       
    except:
        file.close()

def MarkItems():

def ArchiveItems():


def InputCommand():
    Command = input("Please specify a command [list, add, mark, archive]: ")
    if Command == "list" or "List":
        ListItems()
    elif Command == "add" or "Add":
        AddItems()
    elif Command == "mark" or "Mark":
        MarkItems()
    elif Command == "archive" or "Archive":
        ArchiveItems()
    else:
        print("Invalid command!")
    return Command


# ========== Main ==========

InputCommand()