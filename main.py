import os

def menuOptions():
    while True:
      print("\n* Move into Directory (1)")
      print("* Move out Directory (2)")
      print("* Folder Operation (3)")
      print("* Exit Program (4)\n")
      optionChecker(chooseOption())


def optionChecker(optionChosen):
    if int(optionChosen) == 1:
        chosenFolder = chooseFolder()
        optionOne(chosenFolder)
        menuScreen()

    elif int(optionChosen) == 2:
        optionTwo()
        menuScreen()
    elif int(optionChosen) == 3:
        fileOperateScreen()
    else:
         exitProgram()


def exitProgram():
        refreshScreen()
        print("\nExiting..\n")
        exit()


def folderOptionChecker(optionChosen):
    if int(optionChosen) == 1:
        makeFolder(askDirectoryName(int(optionChosen)))
        menuScreen()
    elif int(optionChosen) == 2:
        removeFolder(askDirectoryName(int(optionChosen)))
        menuScreen()
    elif int(optionChosen) == 3:
        removeFile(askDirectoryName(int(optionChosen)))
        menuScreen()
    elif int(optionChosen) == 4:
        menuScreen()
    else:
        exitProgram()


        


def optionOne(location):
    # Moves to directory chosen
    os.chdir(location)

def optionTwo():
     # Moves back a directory
     os.chdir("..")


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




def makeFolder(folderName):
    os.mkdir(folderName)

def removeFolder(folderName):
     os.rmdir(folderName)

def removeFile(fileName):
    os.remove(fileName)

def folderOperators():
    while True:
      print("\n* Make Directory (1)")
      print("* Remove Directory (2)")
      print("* Remove File (3)")
      print("* Go Back (4)")
      print("* Exit Program (5)\n")
      folderOptionChecker(chooseOption()) 
        

    


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


def askDirectoryName(optionChosen):
    if optionChosen == 1:
         userInput = input("Give a name for newly created folder: ")
         return userInput
    elif optionChosen == 2:
          userInput = input("What is the folder you want to remove: ")
          return userInput
    elif optionChosen == 3:
          userInput = input("What is the file you want to remove: ")
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

def fileOperateScreen():
    refreshScreen()
    ShowLocation()
    directoryFormat()
    folderOperators()


def menuScreen():
    refreshScreen()
    ShowLocation()
    directoryFormat()
    menuOptions()



####################################################################

menuScreen()