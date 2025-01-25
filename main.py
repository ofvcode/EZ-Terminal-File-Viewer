import os

def main():
    print("Welcome to EZ Terminal File Viewer")

    print("\n(1) Move to Home Folder , (2) Exit")
    def chooseFunc():
        userInput = (input("\nChoose an Option: "))
        return userInput


    def reformat():
        dirList = os.listdir()
        dirListFormatted = dirList.copy()
        for x in dirListFormatted:
            if os.path.isfile(x) == True:
                numv = dirListFormatted.index(x)
                dirListFormatted[numv] = "File: " + str(x)
            else:
                numv = dirListFormatted.index(x)
                dirListFormatted[numv] = "Folder: " + str(x)
        return dirListFormatted

    def moveHome():
        os.system('clear')
        print("EZ Terminal File Viewer:")
        home = os.environ.get("HOME")
        os.chdir(home)
        print("\nFiles / Folders:\n")
        dirList = os.listdir()
        dirListFormatted = dirList.copy()
        dirListFormatted = reformat()

        print(dirListFormatted)
        print("\n(1) Move to Specific Directory , (2) Move out of folder, (3) Exit")
        userInput = chooseFunc()
        while True:
          if int(userInput) == 1  or int(userInput) == 2 or int(userInput) == 3:
             if int(userInput) == 3:
                  os.system('clear')
                  print("\nEZ Terminal File Viewer:")
                  print("\nExiting.")
                  exit()
             elif int(userInput) == 1:
                 os.system('clear')
                 print("EZ Terminal File Viewer:\n")
                 print("Move into which folder?:\n")
                 os.chdir("..")
                 print(reformat())
                 userInput = chooseFunc()
                 moveInto(userInput)
                 return True               
             else:
                 os.system('clear')
                 print("EZ Terminal File Viewer:")
                 print("Move into which folder?:\n")
                 print(dirListFormatted)
                 userInput = chooseFunc()
                 moveInto(userInput)
                 return True
        
         



        
    

    def moveInto(location):
        dir = location
        os.chdir(location)
        print(f'You have moved into {dir}')
        dirList = os.listdir()
        dirListFormatted = dirList.copy()
        dirListFormatted = reformat()
        os.system('clear')
        print("EZ Terminal File Viewer:")
        print("\nMove into which folder?:\n")
        print(str(dirListFormatted) + "\n")
        userOp = chooseFunc()
        moveInto(userOp)

 


###########################################################################################


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