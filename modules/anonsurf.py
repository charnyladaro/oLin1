import os
from sys import argv
from platform import system


def clearScr():
    if system() == "Linux":
        os.system("clear")
    if system() == "Windows":
        os.system("cls")


def anonsurf():
    print(
        """
        \033[32m[1]  \033[36mInstall Anonsurf
        \033[32m[2]  \033[36mStart Anonsurf
        \033[32m[3]  \033[36mUpdate AnonSurf
        \033[32m[99] \033[36mBack
    """
    )
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        ansurf()
    if choice == "2":
        clearScr()
        ansurf()
    if choice == "3":
        clearScr()
        ansurf()
    elif choice == "99":
        pass
    else:
        pass


# This is the Original code
def ansurf():
    print(
        "It automatically overwrites the RAM when\nthe system is shutting down and also change IP\n"
    )
    anc = input(
        "[1]\033[36mInstall \033[32m[2]\033[36mRun \033[32m[3]\033[36mStop \033[32m[99]\033[36mMain Menu >> \033[32m"
    )
    if anc == "1":
        # os.system("git clone https://github.com/Und3rf10w/kali-anonsurf.git")
        os.system(
            "cd kali-anonsurf && sudo ./installer.sh && cd .. && sudo rm -r kali-anonsurf"
        )
        print("\033[33m[+] Successfully Installed ...!!\033[32m")
    elif anc == "2":
        os.system("sudo anonsurf start")
    elif anc == "3":
        os.system("sudo anonsurf stop")
    elif anc == "99":
        anonsurf()
    else:
        pass


if __name__ == "__main__":
    anonsurf()
