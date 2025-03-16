import sys
from subprocess import Popen, PIPE

history_list =["(Go Back)"]

def loggingTemplate(command, message):
    log_proc = Popen(['python3', 'log.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
    log_proc.stdin.write(command + '\n')
    log_proc.stdin.write(message + '\n')
    log_proc.stdin.flush()
    log_proc.wait()

def printHistory():
    print("---------------------------")
    print("          History          ")
    print("---------------------------")
    for index, value in enumerate(history_list):
        print(f"{index}: {value}")
    print("---------------------------")


running = True
password_set = False
password = ''

def printTemplate():
    print("---------------------------\n")
    print("password - set the password for encryption/decryption")
    print("encrypt  - encrypt a string")
    print("decrypt  - decrypt a string")
    print("history  - show history")
    print("quit     - quit program\n")
    print("---------------------------")

def passwordCommand():
    global password
    password_set = False
    loggingTemplate('SET_PASSWORD', 'Setting Passkey...')
    while (password_set == False):
        password_prompt = input("Do you want to use history (Y/N): ")
        if (password_prompt.upper() == 'Y'):
            printHistory()
            password_select_num = input("Select Password: ")
            while (int(password_select_num) > (len(history_list) - 1)):
                print("Please enter a valid password")
                password_select_num = input("Select Password: ")
            if (history_list[int(password_select_num)] == '(Go Back)'):
                continue
            else:
                password = history_list[int(password_select_num)]
                password_set = True
                continue
        else:
            password = input("Enter password: ")
            password_set = True
            continue
    loggingTemplate('SET_PASSWORD', 'Password Successfully Set!')

def encryptCommand():
    global password
    encrypt_set = False
    encrypt_string = ''
    while (encrypt_set == False):
        if len(history_list) == 1:
            encrypt_string = input("Enter String to ENCRYPT: ")
            history_list.insert(0, encrypt_string)
            encrypt_set = True
            continue
        while len(history_list) > 1:
            encrypt_prompt = input("Do you want to use history (Y/N): ")
            if (encrypt_prompt.upper() == 'Y'):
                printHistory()
                encrypt_select_num = input("Select String to ENCRYPT: ")
                while (int(encrypt_select_num) > (len(history_list) - 1)):
                    print("Please enter a valid String to ENCRYPT")
                    encrypt_select_num = input("Select String to ENCRYPT: ")
                if (history_list[int(encrypt_select_num)] == '(Go Back)'):
                    continue
                else:
                    encrypt_string = history_list[int(encrypt_select_num)]
                    encrypt_set = True
                    break
            else:
                encrypt_string = input("Enter String to ENCRYPT: ")
                history_list.insert(0, encrypt_string)
                encrypt_set = True
                break
    loggingTemplate('ENCRYPT', 'Encrypt String: ' + encrypt_string)
    if password == '':
        print("Password NOT set!")
        loggingTemplate('ENCRYPT', 'ERROR: Password NOT set!')
        return
    encrypt_proc = Popen(['python3', 'encrypt.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
    encrypt_proc.stdin.write(password + '\n')
    encrypt_proc.stdin.write('encrypt' + '\n')
    encrypt_proc.stdin.write(encrypt_string + '\n')
    encrypt_proc.stdin.flush()
    encrypt_proc.wait()
    encrypted_word = encrypt_proc.stdout.readline().strip()
    history_list.insert(0, encrypted_word)
    print("Result: " + encrypted_word)
    loggingTemplate('ENCRYPT', 'Success: ' + encrypted_word )

def decryptCommand():
    global password
    decrypt_set = False
    decrypt_string = ''
    while (decrypt_set == False):
        if len(history_list) == 1:
            decrypt_string = input("Enter String to DECRYPT: ")
            history_list.insert(0, decrypt_string)
            decrypt_set = True
            continue
        while len(history_list) > 1:
            decrypt_prompt = input("Do you want to use history (Y/N): ")
            if (decrypt_prompt.upper() == 'Y'):
                printHistory()
                decrypt_select_num = input("Select String to DECRYPT: ")
                while (int(decrypt_select_num) > (len(history_list) - 1)):
                    print("Please enter a valid String to DECRYPT")
                    decrypt_select_num = input("Select String to DECRYPT: ")
                if (history_list[int(decrypt_select_num)] == '(Go Back)'):
                    continue
                else:
                    decrypt_string = history_list[int(decrypt_select_num)]
                    decrypt_set = True
                    break
            else:
                decrypt_string = input("Enter String to DECRYPT: ")
                history_list.insert(0, decrypt_string)
                decrypt_set = True
                break
    loggingTemplate('DECRYPT', 'Decrypt String: ' + decrypt_string)
    if password == '':
        print("Password NOT set!")
        loggingTemplate('DECRYPT', 'ERROR: Password NOT set!')
        return
    encrypt_proc = Popen(['python3', 'encrypt.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
    encrypt_proc.stdin.write(password + '\n')
    encrypt_proc.stdin.write('decrypt' + '\n')
    encrypt_proc.stdin.write(decrypt_string + '\n')
    encrypt_proc.stdin.flush()
    encrypt_proc.wait()
    decrypted_word = encrypt_proc.stdout.readline().strip()
    history_list.insert(0, decrypted_word)
    print("Result: " + decrypted_word)
    loggingTemplate('DECRYPT', 'Success: ' + decrypted_word)

log_proc = Popen(['python3', 'log.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
log_proc.stdin.write('start' + '\n')
log_proc.stdin.write('Logging Started' + '\n')
log_proc.stdin.flush()
log_proc.wait()

while running:
    printTemplate()
    command = input("Enter command: ")
    if(command == 'password'):
        passwordCommand()
    if(command == 'encrypt'):
        encryptCommand()
    if(command == 'decrypt'):
        decryptCommand()
    if(command == 'history'):
        printHistory()
        loggingTemplate('HISTORY', 'History Checked')
        continue
    if(command == 'quit'):
        loggingTemplate('STOP', 'Logging Stopped')
        running = False
        continue

print("Program Terminated!")



