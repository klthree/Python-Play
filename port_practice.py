import random

answer_key = {'http': 80, 'https': 443, 'ssh': 22, 'telnet': 23, 'ftp': (20, 21),
                'tftp': 69, 'sftp': (989, 990), 'smtp': 25, 'pop3': 110, 'imap': 143, 
                'rdp': 3389, 'ldap': 389, 'ntp': 123, 'dns': 53, 'dhcp': (67, 68),
                'netbios': (135, 136, 137, 138, 139), 'ipsec': (50, 51), 'nntp': 119,
                'snmp': (161, 162)}

protocol_list = list(answer_key)
print(protocol_list)

choice = input("Practice port numbers? ")

if choice == 'y':
    print("Enter 'q' to quit")
    while choice != 'q' or choice != 'Q':
        protocol = random.choice(protocol_list)
        options = [answer_key[protocol]]
        
        while len(options) < 4:
            next = random.choice(protocol_list)
            if next != protocol:
                options.append(answer_key[next])
        
        random.shuffle(options)    
        answer = options.index(answer_key[protocol]) + 1
        msg = f"{protocol} operates on port {options[answer - 1]}"

        print()
        print(f"Which port(s) does {protocol} work on?")
        
        for i in range(len(options)):
            print("{0}. {1}".format(i + 1, options[i]))
        
        while choice != 'q' or int(choice) < 1 or int(choice) > len(options):
            choice = input("Enter the number corresponding to the correct answer ")
            print(int(choice))

        if choice == 'q':
            print("Goodbye!")
            break
        elif choice > len(options) + 1:
            print("Invalid selection")
        elif choice == answer:
            print(f"Success! {msg}")
        else:
            print(f"Wrong! {msg}")

