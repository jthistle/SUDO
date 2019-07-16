#!/usr/bin/env python3

# Installer for SUDO
# jthistle on GitHub, GPL licensed

import shutil, os

def main():
     
    # Change this to your rc file if you are using a different shell or have you rc in a different location
    RCFILE = os.path.expanduser("~/.bashrc")

    # Make a backup
    shutil.copyfile(RCFILE, RCFILE + ".old")

    newcontents = False

    # Tests for being able to open files needed
    try:
        open(RCFILE, "r")
    except Exception as e:
        print("Error when opening rc file: {}".format(e))
        return

    try:
        open("./SUDO", "r")
    except Exception as e:
        print("Error when opening programme code: {}".format(e))
        return

    # Check for old installations
    with open(RCFILE, "r") as rc:
        contents = rc.read() 
        start = contents.find("# SUDO - shout at bash") 
        end = contents.find("# end SUDO")        
        
        foundStart = start != -1
        foundEnd = end != -1

        if foundStart and not foundEnd:
            print("You have an older installation of SUDO. Please manually remove old version from your rc file to be able to install the new version.")
        elif not foundStart and not foundEnd:
            print("No current installation found.")
            newcontents = contents
        elif foundStart and foundEnd:
            print("Found current installation, removing...")
        
            newcontents = contents[:start] + contents[end+len("# end SUDO"):]

    if newcontents:
        newcontents = newcontents.strip()

    # Add in new SUDO code
    if newcontents:
        programmeCode = ""
        with open("./SUDO", "r") as codeFile:
            programmeCode = codeFile.read()
        
        if programmeCode != "":
            with open(RCFILE, "w") as rc:
                newcontents += "\n\n" + programmeCode + "\n"
                rc.write(newcontents)
                print("Successfully wrote new rc file.")
                print("\nNow run:    source {} \n".format(RCFILE))
        else:
            print("Couldn't read SUDO code")
    else:
        print("Finishing without installing.")


if __name__ == "__main__":
    main()
