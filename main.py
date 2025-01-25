import os

def main():
    print("Welcome to EZ Terminal File Viewer")

    print("\n(1) Move to Home Folder , (2) Exit\n")
    def chooseFunc():
        userInput = (input("Choose an Option: "))
        return userInput

    def moveHome():
        os.system('clear')
        print("EZ Terminal File Viewer:")
        home = os.environ.get("HOME")
        os.chdir(home)
        print("\nFiles / Folders:\n")
        dirList = os.listdir()
        for x in dirList:
            if os.path.isfile(x) == True:
                numv = dirList.index(x)
                dirList[numv] = "File: " + str(x)
            else:
                numv = dirList.index(x)
                dirList[numv] = "Folder: " + str(x)
        print(dirList)
    
    option = chooseFunc()
    
    while True:
     if int(option) == 1  or int(option) == 2:
         if int(option) == 2:
            os.system('clear')
            print("\nEZ Terminal File Viewer:\n")
            print("\nExiting.\n")
            exit()
         else:
            moveHome()
            return True



main()

# Change file