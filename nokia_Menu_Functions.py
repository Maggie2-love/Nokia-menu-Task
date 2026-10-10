def main_menu():
    while True:
        print("\n========== NOKIA MENU ==========")
        print("1. Phone book")
        print("2. Messages")
        print("3. Chat")
        print("4. Call register")
        print("5. Tones")
        print("6. Settings")
        print("7. Call divert")
        print("8. Games")
        print("9. Calculator")
        print("10. Reminders")
        print("11. Clock")
        print("12. Profiles")
        print("13. SIM services")
        print("14. Services")
        print("15. Extras")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            phone_book()
        elif choice == "2":
            messages()
        elif choice == "3":
            chat()
        elif choice == "4":
            call_register()
        elif choice == "5":
            tones()
        elif choice == "6":
            settings()
        elif choice == "7":
            call_divert()
        elif choice == "8":
            games()
        elif choice == "9":
            calculator()
        elif choice == "10":
            reminders()
        elif choice == "11":
            clock()
        elif choice == "12":
            profiles()
        elif choice == "13":
            sim_services()
        elif choice == "14":
            services()
        elif choice == "15":
            extras()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


def phone_book():
    while True:
        print("\n===== PHONE BOOK =====")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b'card")
        print("8. Options")
        print("9. Speed dials")
        print("10. Voice tags")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Search")
        elif choice == "2":
            print("Service Nos.")
        elif choice == "3":
            print("Add name")
        elif choice == "4":
            print("Erase")
        elif choice == "5":
            print("Edit")
        elif choice == "6":
            print("Assign tone")
        elif choice == "7":
            print("Send b'card")
        elif choice == "8":
            phone_book_options()
        elif choice == "9":
            print("Speed dials")
        elif choice == "10":
            print("Voice tags")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def phone_book_options():
    while True:
        print("\n===== PHONE BOOK OPTIONS =====")
        print("1. Type of view")
        print("2. Memory status")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Type of view")
        elif choice == "2":
            print("Memory status")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def messages():
    while True:
        print("\n===== MESSAGES =====")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Write messages")
        elif choice == "2":
            print("Inbox")
        elif choice == "3":
            print("Outbox")
        elif choice == "4":
            print("Picture messages")
        elif choice == "5":
            print("Templates")
        elif choice == "6":
            print("Smileys")
        elif choice == "7":
            message_settings()
        elif choice == "8":
            print("Info service")
        elif choice == "9":
            print("Voice mailbox number")
        elif choice == "10":
            print("Service command editor")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def message_settings():
    while True:
        print("\n===== MESSAGE SETTINGS =====")
        print("1. Set 1")
        print("2. Common")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            message_set()
        elif choice == "2":
            common_settings()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def message_set():
    while True:
        print("\n===== SET 1 =====")
        print("1. Message centre number")
        print("2. Messages sent as")
        print("3. Message validity")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Message centre number")
        elif choice == "2":
            print("Messages sent as")
        elif choice == "3":
            print("Message validity")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def common_settings():
    while True:
        print("\n===== COMMON SETTINGS =====")
        print("1. Delivery reports")
        print("2. Reply via same centre")
        print("3. Character support")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Delivery reports")
        elif choice == "2":
            print("Reply via same centre")
        elif choice == "3":
            print("Character support")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def chat():
    while True:
        print("\n===== CHAT =====")
        print("1. Start chat")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Start chat")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def call_register():
    while True:
        print("\n===== CALL REGISTER =====")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call costs")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Missed calls")
        elif choice == "2":
            print("Received calls")
        elif choice == "3":
            print("Dialled numbers")
        elif choice == "4":
            print("Erase recent call lists")
        elif choice == "5":
            call_duration()
        elif choice == "6":
            call_costs()
        elif choice == "7":
            call_cost_settings()
        elif choice == "8":
            print("Prepaid credit")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def call_duration():
    while True:
        print("\n===== CALL DURATION =====")
        print("1. Last call duration")
        print("2. All calls duration")
        print("3. Received calls duration")
        print("4. Dialled calls duration")
        print("5. Clear timers")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Last call duration")
        elif choice == "2":
            print("All calls duration")
        elif choice == "3":
            print("Received calls duration")
        elif choice == "4":
            print("Dialled calls duration")
        elif choice == "5":
            print("Clear timers")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def call_costs():
    while True:
        print("\n===== CALL COSTS =====")
        print("1. Last call cost")
        print("2. All calls cost")
        print("3. Clear counters")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Last call cost")
        elif choice == "2":
            print("All calls cost")
        elif choice == "3":
            print("Clear counters")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def call_cost_settings():
    while True:
        print("\n===== CALL COST SETTINGS =====")
        print("1. Call cost limit")
        print("2. Show costs in")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Call cost limit")
        elif choice == "2":
            print("Show costs in")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def tones():
    while True:
        print("\n===== TONES =====")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Composer")
        print("5. Message alert tone")
        print("6. Keypad tones")
        print("7. Warning and game tones")
        print("8. Vibrating alert")
        print("9. Screen saver")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Ringing tone")
        elif choice == "2":
            print("Ringing volume")
        elif choice == "3":
            print("Incoming call alert")
        elif choice == "4":
            print("Composer")
        elif choice == "5":
            print("Message alert tone")
        elif choice == "6":
            print("Keypad tones")
        elif choice == "7":
            print("Warning and game tones")
        elif choice == "8":
            print("Vibrating alert")
        elif choice == "9":
            print("Screen saver")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def settings():
    while True:
        print("\n===== SETTINGS =====")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            call_settings()
        elif choice == "2":
            phone_settings()
        elif choice == "3":
            security_settings()
        elif choice == "4":
            print("Restore factory settings")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def call_settings():
    while True:
        print("\n===== CALL SETTINGS =====")
        print("1. Automatic redial")
        print("2. Speed dialling")
        print("3. Call waiting options")
        print("4. Own number sending")
        print("5. Phone line in use")
        print("6. Automatic answer")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Automatic redial")
        elif choice == "2":
            print("Speed dialling")
        elif choice == "3":
            print("Call waiting options")
        elif choice == "4":
            print("Own number sending")
        elif choice == "5":
            print("Phone line in use")
        elif choice == "6":
            print("Automatic answer")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def phone_settings():
    while True:
        print("\n===== PHONE SETTINGS =====")
        print("1. Language")
        print("2. Cell info display")
        print("3. Welcome note")
        print("4. Network selection")
        print("5. Lights")
        print("6. Confirm SIM service actions")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Language")
        elif choice == "2":
            print("Cell info display")
        elif choice == "3":
            print("Welcome note")
        elif choice == "4":
            print("Network selection")
        elif choice == "5":
            print("Lights")
        elif choice == "6":
            print("Confirm SIM service actions")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def security_settings():
    while True:
        print("\n===== SECURITY SETTINGS =====")
        print("1. PIN code request")
        print("2. Call barring service")
        print("3. Fixed dialling")
        print("4. Closed user group")
        print("5. Phone security")
        print("6. Change access codes")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("PIN code request")
        elif choice == "2":
            print("Call barring service")
        elif choice == "3":
            print("Fixed dialling")
        elif choice == "4":
            print("Closed user group")
        elif choice == "5":
            print("Phone security")
        elif choice == "6":
            print("Change access codes")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def call_divert():
    while True:
        print("\n===== CALL DIVERT =====")
        print("1. Divert all voice calls")
        print("2. Divert when busy")
        print("3. Divert when not answered")
        print("4. Divert when phone off")
        print("5. Cancel all diverts")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Divert all voice calls")
        elif choice == "2":
            print("Divert when busy")
        elif choice == "3":
            print("Divert when not answered")
        elif choice == "4":
            print("Divert when phone off")
        elif choice == "5":
            print("Cancel all diverts")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def games():
    while True:
        print("\n===== GAMES =====")
        print("1. Snake")
        print("2. Space Impact")
        print("3. Bantumi")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Snake")
        elif choice == "2":
            print("Space Impact")
        elif choice == "3":
            print("Bantumi")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def calculator():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "0":
            break

        elif choice == "1":
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            print("Answer:", first + second)

        elif choice == "2":
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            print("Answer:", first - second)

        elif choice == "3":
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            print("Answer:", first * second)

        elif choice == "4":
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            if second == 0:
                print("Cannot divide by zero")
            else:
                print("Answer:", first / second)

        else:
            print("Invalid choice")


def reminders():
    while True:
        print("\n===== REMINDERS =====")
        print("1. Add reminder")
        print("2. View reminders")
        print("3. Delete reminders")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Add reminder")
        elif choice == "2":
            print("View reminders")
        elif choice == "3":
            print("Delete reminders")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def clock():
    while True:
        print("\n===== CLOCK =====")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date setting")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Alarm clock")
        elif choice == "2":
            print("Clock settings")
        elif choice == "3":
            print("Date setting")
        elif choice == "4":
            print("Stopwatch")
        elif choice == "5":
            print("Countdown timer")
        elif choice == "6":
            print("Auto update of date and time")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def profiles():
    while True:
        print("\n===== PROFILES =====")
        print("1. General")
        print("2. Silent")
        print("3. Discreet")
        print("4. Loud")
        print("5. My style")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("General")
        elif choice == "2":
            print("Silent")
        elif choice == "3":
            print("Discreet")
        elif choice == "4":
            print("Loud")
        elif choice == "5":
            print("My style")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def sim_services():
    while True:
        print("\n===== SIM SERVICES =====")
        print("1. Network services")
        print("2. SIM information")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Network services")
        elif choice == "2":
            print("SIM information")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def services():
    while True:
        print("\n===== SERVICES =====")
        print("1. Home")
        print("2. Bookmarks")
        print("3. Service inbox")
        print("4. Settings")
        print("5. Go to address")
        print("6. Clear cache")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Home")
        elif choice == "2":
            print("Bookmarks")
        elif choice == "3":
            print("Service inbox")
        elif choice == "4":
            print("Settings")
        elif choice == "5":
            print("Go to address")
        elif choice == "6":
            print("Clear cache")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def extras():
    while True:
        print("\n===== EXTRAS =====")
        print("1. Calculator")
        print("2. Stopwatch")
        print("3. Countdown timer")
        print("4. Currency converter")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            print("Stopwatch")
        elif choice == "3":
            print("Countdown timer")
        elif choice == "4":
            print("Currency converter")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


main_menu()
