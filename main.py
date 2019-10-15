import os

my_net = '192.168.2.0/24'


def discover_IP_in_net():
    os.system('nmap -sS -O ' + my_net)


def Install_centos_packages():
    print()


def Install_ubuntu_packages():
    print()


def Install_jenkins():
    print()


def menu_text():
    print("Main Menu:".center(100))
    print("1.Discover all IP's in net".center(100))
    print("2.Install full packages centos".center(104))
    print("3.Install full packages ubuntu".center(104))
    print("4.Install jenkins M&S".center(96))
    print("5.Leave".center(82))


def main_menu():
    menu_text()
    choice = int(input())
    if choice == 1:
        discover_IP_in_net()
    elif choice == 2:
        Install_centos_packages()
    elif choice == 3:
        Install_ubuntu_packages()
    elif choice == 4:
        Install_jenkins()
    elif choice == 5:
        return


spaces = "-=========~~~~~~=========-".center(100)

print("\n" + spaces)
print("--Main Script Controller--".center(100))
print(spaces + "\n")

main_menu()

while True:
    answer = input("Are you sure you want to leave, or go back to the main menu?\n1 = Main Menu\n2 = Leave")

    if answer == "2":
        break
    elif answer == "1":
        main_menu()
    else:
        print("Invalid input, try again.")