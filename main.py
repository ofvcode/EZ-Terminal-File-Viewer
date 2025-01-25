import os

def menuOptions():
    while True:
      print("\n* Move into Directory (1)")
      print("* Move out Directory (2)")
      print("* Exit Program (3)\n")
      return chooseOption()
      
def optionOne(location):
    # Moves to directory chosen
    os.chdir(location)


def directoryFormat():
    # Formats Files and Folders and prints it
    dir_list = os.listdir(os.getcwd())
    remadeList = dir_list.copy()
    filesOnly = []
    foldersOnly = []
    


    for fileorFolder in remadeList:
        if os.path.isfile(fileorFolder) == True:
            #Appends files to a file specific list
            numv = remadeList.index(fileorFolder)
            remadeList[numv] = "File: " + str(fileorFolder)
            filesOnly.append(fileorFolder)
        else:
            #Appends folders to a folder specific list
            numv = remadeList.index(fileorFolder)
            remadeList[numv] = "Folder: " + str(fileorFolder)
            foldersOnly.append(fileorFolder)
    print("Files: ")
    print(f"{filesOnly}")
    print("Folders: ")
    print(f"{foldersOnly}")




    


def chooseOption():
    userInput = input("Choose an option: ")
    return userInput

def chooseFolder():
    userInput = input("Choose a folder to move into: ")
    return userInput



def refreshScreen():
    os.system("clear")
    print("EZ Terminal File Viewer")

def ShowLocation():
    cwd = os.getcwd() 
    print(f"Current working directory: {cwd} \n") 



def Startup():
    print("You are currently in:")

def mainMenu():
    refreshScreen()
    ShowLocation()
    directoryFormat()
    menuOptions()

####################################################################

mainMenu()