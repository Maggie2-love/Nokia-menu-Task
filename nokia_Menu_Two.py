main_menu_choice = -1

while main_menu_choice != 0:

    print("\nMENU")
    print("1. Phone book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call divert")
    print("8. Music")
    print("9. Games")
    print("10. Calculator")
    print("11. Reminders")
    print("12. Clock")
    print("13. Profiles")
    print("14. Services")
    print("15. SIM services")
    print("0. Exit")

    main_menu_choice = int(input("Select: "))

    # PHONE BOOK
    if main_menu_choice == 1:

        phone_book_choice = -1

        while phone_book_choice != 0:

            print("\nPHONE BOOK")
            print("1. Search")
            print("2. Service Nos.")
            print("3. Add name")
            print("4. Erase")
            print("5. Edit")
            print("6. Copy")
            print("7. Assign tone")
            print("8. Send b'card")
            print("9. Options")
            print("10. Speed dials")
            print("11. Voice tags")
            print("0. Back")

            phone_book_choice = int(input("Select: "))

            if phone_book_choice == 1:
                print("Search")

            elif phone_book_choice == 2:
                print("Service Nos.")

            elif phone_book_choice == 3:
                print("Add name")

            elif phone_book_choice == 4:
                print("Erase")

            elif phone_book_choice == 5:
                print("Edit")

            elif phone_book_choice == 6:
                print("Copy")

            elif phone_book_choice == 7:
                print("Assign tone")

            elif phone_book_choice == 8:
                print("Send b'card")

            elif phone_book_choice == 9:

                option_choice = -1

                while option_choice != 0:

                    print("\nOPTIONS")
                    print("1. Memory in use")
                    print("2. Type of view")
                    print("3. Memory status")
                    print("0. Back")

                    option_choice = int(input("Select: "))

                    if option_choice == 1:
                        print("Memory in use")

                    elif option_choice == 2:
                        print("Type of view")

                    elif option_choice == 3:
                        print("Memory status")

                    elif option_choice == 0:
                        pass

                    else:
                        print("Invalid option")

            elif phone_book_choice == 10:
                print("Speed dials")

            elif phone_book_choice == 11:
                print("Voice tags")

            elif phone_book_choice == 0:
                pass

            else:
                print("Invalid option")


    # MESSAGES
    elif main_menu_choice == 2:

        messages_choice = -1

        while messages_choice != 0:

            print("\nMESSAGES")
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
            print("0. Back")

            messages_choice = int(input("Select: "))

            if messages_choice == 1:

                print("\nWRITE MESSAGES")
                message = input("Write your message: ")
                print("Message:", message)

            elif messages_choice == 2:
                print("Inbox")

            elif messages_choice == 3:
                print("Outbox")

            elif messages_choice == 4:
                print("Picture messages")

            elif messages_choice == 5:
                print("Templates")

            elif messages_choice == 6:
                print("Smileys")

            elif messages_choice == 7:

                message_settings_choice = -1

                while message_settings_choice != 0:

                    print("\nMESSAGE SETTINGS")
                    print("1. Set 1")
                    print("2. Common")
                    print("0. Back")

                    message_settings_choice = int(input("Select: "))

                    if message_settings_choice == 1:

                        set_choice = -1

                        while set_choice != 0:

                            print("\nSET 1")
                            print("1. Message centre number")
                            print("2. Messages sent as")
                            print("3. Message validity")
                            print("0. Back")

                            set_choice = int(input("Select: "))

                            if set_choice == 1:
                                print("Message centre number")

                            elif set_choice == 2:
                                print("Messages sent as")

                            elif set_choice == 3:
                                print("Message validity")

                            elif set_choice == 0:
                                pass

                            else:
                                print("Invalid option")


                    elif message_settings_choice == 2:

                        common_choice = -1

                        while common_choice != 0:

                            print("\nCOMMON")
                            print("1. Delivery reports")
                            print("2. Reply via same centre")
                            print("3. Character support")
                            print("0. Back")

                            common_choice = int(input("Select: "))

                            if common_choice == 1:
                                print("Delivery reports")

                            elif common_choice == 2:
                                print("Reply via same centre")

                            elif common_choice == 3:
                                print("Character support")

                            elif common_choice == 0:
                                pass

                            else:
                                print("Invalid option")

                    elif message_settings_choice == 0:
                        pass

                    else:
                        print("Invalid option")


            elif messages_choice == 8:
                print("Info service")

            elif messages_choice == 9:
                print("Voice mailbox number")

            elif messages_choice == 10:
                print("Service command editor")

            elif messages_choice == 0:
                pass

            else:
                print("Invalid option")


    # CHAT
    elif main_menu_choice == 3:
        print("\nCHAT")


    # CALL REGISTER
    elif main_menu_choice == 4:

        call_register_choice = -1

        while call_register_choice != 0:

            print("\nCALL REGISTER")
            print("1. Missed calls")
            print("2. Received calls")
            print("3. Dialled numbers")
            print("4. Erase recent call lists")
            print("5. Show call duration")
            print("6. Show call costs")
            print("7. Call cost settings")
            print("8. Prepaid credit")
            print("0. Back")

            call_register_choice = int(input("Select: "))

            if call_register_choice == 1:
                print("Missed calls")

            elif call_register_choice == 2:
                print("Received calls")

            elif call_register_choice == 3:
                print("Dialled numbers")

            elif call_register_choice == 4:
                print("Erase recent call lists")

            elif call_register_choice == 5:

                duration_choice = -1

                while duration_choice != 0:

                    print("\nSHOW CALL DURATION")
                    print("1. Last call duration")
                    print("2. All calls' duration")
                    print("3. Received calls' duration")
                    print("4. Dialled calls' duration")
                    print("5. Clear timers")
                    print("0. Back")

                    duration_choice = int(input("Select: "))

                    if duration_choice == 1:
                        print("Last call duration")

                    elif duration_choice == 2:
                        print("All calls' duration")

                    elif duration_choice == 3:
                        print("Received calls' duration")

                    elif duration_choice == 4:
                        print("Dialled calls' duration")

                    elif duration_choice == 5:
                        print("Clear timers")

                    elif duration_choice == 0:
                        pass

                    else:
                        print("Invalid option")


            elif call_register_choice == 6:

                cost_choice = -1

                while cost_choice != 0:

                    print("\nSHOW CALL COSTS")
                    print("1. Last call cost")
                    print("2. All calls' cost")
                    print("3. Clear counters")
                    print("0. Back")

                    cost_choice = int(input("Select: "))

                    if cost_choice == 1:
                        print("Last call cost")

                    elif cost_choice == 2:
                        print("All calls' cost")

                    elif cost_choice == 3:
                        print("Clear counters")

                    elif cost_choice == 0:
                        pass

                    else:
                        print("Invalid option")


            elif call_register_choice == 7:

                cost_settings_choice = -1

                while cost_settings_choice != 0:

                    print("\nCALL COST SETTINGS")
                    print("1. Call cost limit")
                    print("2. Show costs in")
                    print("0. Back")

                    cost_settings_choice = int(input("Select: "))

                    if cost_settings_choice == 1:
                        print("Call cost limit")

                    elif cost_settings_choice == 2:
                        print("Show costs in")

                    elif cost_settings_choice == 0:
                        pass

                    else:
                        print("Invalid option")


            elif call_register_choice == 8:
                print("Prepaid credit")

            elif call_register_choice == 0:
                pass

            else:
                print("Invalid option")


    # TONES
    elif main_menu_choice == 5:

        tones_choice = -1

        while tones_choice != 0:

            print("\nTONES")
            print("1. Ringing tone")
            print("2. Ringing volume")
            print("3. Incoming call alert")
            print("4. Message alert tone")
            print("5. Keypad tones")
            print("6. Warning tones")
            print("7. Vibrating alert")
            print("8. Screen saver")
            print("0. Back")

            tones_choice = int(input("Select: "))

            if tones_choice == 1:
                print("Ringing tone")

            elif tones_choice == 2:
                print("Ringing volume")

            elif tones_choice == 3:
                print("Incoming call alert")

            elif tones_choice == 4:
                print("Message alert tone")

            elif tones_choice == 5:
                print("Keypad tones")

            elif tones_choice == 6:
                print("Warning tones")

            elif tones_choice == 7:
                print("Vibrating alert")

            elif tones_choice == 8:
                print("Screen saver")

            elif tones_choice == 0:
                pass

            else:
                print("Invalid option")


    # SETTINGS
    elif main_menu_choice == 6:

        settings_choice = -1

        while settings_choice != 0:

            print("\nSETTINGS")
            print("1. Call settings")
            print("2. Phone settings")
            print("3. Security settings")
            print("4. Restore factory settings")
            print("0. Back")

            settings_choice = int(input("Select: "))

            if settings_choice == 1:

                call_settings_choice = -1

                while call_settings_choice != 0:

                    print("\nCALL SETTINGS")
                    print("1. Automatic redial")
                    print("2. Speed dialling")
                    print("3. Call waiting options")
                    print("4. Own number sending")
                    print("5. Phone line in use")
                    print("6. Automatic answer")
                    print("0. Back")

                    call_settings_choice = int(input("Select: "))

                    if call_settings_choice == 1:
                        print("Automatic redial")

                    elif call_settings_choice == 2:
                        print("Speed dialling")

                    elif call_settings_choice == 3:
                        print("Call waiting options")

                    elif call_settings_choice == 4:
                        print("Own number sending")

                    elif call_settings_choice == 5:
                        print("Phone line in use")

                    elif call_settings_choice == 6:
                        print("Automatic answer")

                    elif call_settings_choice == 0:
                        pass

                    else:
                        print("Invalid option")


            elif settings_choice == 2:

                phone_settings_choice = -1

                while phone_settings_choice != 0:

                    print("\nPHONE SETTINGS")
                    print("1. Language")
                    print("2. Cell info display")
                    print("3. Welcome note")
                    print("4. Network selection")
                    print("5. Confirm SIM service actions")
                    print("0. Back")

                    phone_settings_choice = int(input("Select: "))

                    if phone_settings_choice == 1:
                        print("Language")

                    elif phone_settings_choice == 2:
                        print("Cell info display")

                    elif phone_settings_choice == 3:
                        print("Welcome note")

                    elif phone_settings_choice == 4:
                        print("Network selection")

                    elif phone_settings_choice == 5:
                        print("Confirm SIM service actions")

                    elif phone_settings_choice == 0:
                        pass

                    else:
                        print("Invalid option")


            elif settings_choice == 3:

                security_choice = -1

                while security_choice != 0:

                    print("\nSECURITY SETTINGS")
                    print("1. PIN code request")
                    print("2. Call barring service")
                    print("3. Fixed dialling")
                    print("4. Closed user group")
                    print("5. Security level")
                    print("6. Change access codes")
                    print("0. Back")

                    security_choice = int(input("Select: "))

                    if security_choice == 1:
                        print("PIN code request")

                    elif security_choice == 2:
                        print("Call barring service")

                    elif security_choice == 3:
                        print("Fixed dialling")

                    elif security_choice == 4:
                        print("Closed user group")

                    elif security_choice == 5:
                        print("Security level")

                    elif security_choice == 6:
                        print("Change access codes")

                    elif security_choice == 0:
                        pass

                    else:
                        print("Invalid option")


            elif settings_choice == 4:
                print("Restore factory settings")

            elif settings_choice == 0:
                pass

            else:
                print("Invalid option")


    # CALL DIVERT
    elif main_menu_choice == 7:
        print("\nCALL DIVERT")


    # MUSIC
    elif main_menu_choice == 8:

        music_choice = -1

        while music_choice != 0:

            print("\nMUSIC")
            print("1. Music player")
            print("2. Radio")
            print("3. Recorder")
            print("4. Track list")
            print("0. Back")

            music_choice = int(input("Select: "))

            if music_choice == 1:
                print("Music player")

            elif music_choice == 2:
                print("Radio")

            elif music_choice == 3:
                print("Recorder")

            elif music_choice == 4:
                print("Track list")

            elif music_choice == 0:
                pass

            else:
                print("Invalid option")


    # GAMES
    elif main_menu_choice == 9:
        print("\nGAMES")


    # CALCULATOR
    elif main_menu_choice == 10:
        print("\nCALCULATOR")


    # REMINDERS
    elif main_menu_choice == 11:
        print("\nREMINDERS")


    # CLOCK
    elif main_menu_choice == 12:

        clock_choice = -1

        while clock_choice != 0:

            print("\nCLOCK")
            print("1. Alarm clock")
            print("2. Clock settings")
            print("3. Date setting")
            print("4. Stopwatch")
            print("5. Countdown timer")
            print("6. Auto update of date and time")
            print("0. Back")

            clock_choice = int(input("Select: "))

            if clock_choice == 1:
                print("Alarm clock")

            elif clock_choice == 2:
                print("Clock settings")

            elif clock_choice == 3:
                print("Date setting")

            elif clock_choice == 4:
                print("Stopwatch")

            elif clock_choice == 5:
                print("Countdown timer")

            elif clock_choice == 6:
                print("Auto update of date and time")

            elif clock_choice == 0:
                pass

            else:
                print("Invalid option")


    # PROFILES
    elif main_menu_choice == 13:
        print("\nPROFILES")


    # SERVICES
    elif main_menu_choice == 14:
        print("\nSERVICES")


    # SIM SERVICES
    elif main_menu_choice == 15:
        print("\nSIM SERVICES")


    elif main_menu_choice == 0:
        print("Exiting...")


    else:
        print("Invalid option")
