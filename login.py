from os import system ; from colorama import init ; from time import sleep ; import stdiomask ; import sys

init(autoreset=True)

class color:
    RED = '\033[1;31m'
    BLUE =  '\033[1;96m'
    END = '\033[m'
    
def clear():
    global clear
    clen = ''
    if clen == '':
        system('clear')
    if clen == '':
        system('cls')
    return (clen)

def info_user():
    global login , password
    print(color.BLUE + '~~' * 25 + color.END)
    login = str(input('Informe seu nome: '))

    print(color.BLUE + '~~' * 25 + color.END)
    
    password = stdiomask.getpass(prompt='Senha: ' , mask='*')
    print(color.BLUE + '~~' * 25 + color.END)

    if login  == password:
        print(color.RED + 'O nome tem que ser diferente da senha!!!' + color.END)

    elif password == login:
        print(color.RED + 'A senha tem que ser diferente da senha!!!' + color.END)
    
    else:
        print(color.BLUE + 'Login efetuado com sucesso.' + color.END)
        criar_planilha()

    return (login , password)

def layout(line=color.BLUE + '~~' * 25 + color.END, msg='System login'):
    print(line)
    print(msg.center(50))
    print(line)

    print(color.BLUE + '''Options

1 - Cadastrar
2 - Exit
''' + color.END)
    print(line)

def main():

    try:
        option = int(input('Deseja utilizar qual opçao?\n'))

        if option < 1:
            print(color.RED + 'Error. Passe informaçoes validas!!!' + color.END)
            sleep(0.8)
            clear()
            layout()
            main()

        elif option > 2:
            print(color.RED + 'Error. Passe informaçoes validas!!!' + color.END)
            sleep(0.8)
            clear()
            layout()
            main()

    except:
        print(color.RED + 'Error. Passe informaçoes validas!!!' + color.END)
        sleep(0.8)
        clear()
        layout()
        main()

    
    if option == 1:
        info_user()
        sleep(0.8)
        clear()
        layout()
        main()

    elif option == 2:
        print(color.RED + '~~' * 25 + color.END)
        print(color.RED + 'Programa finalizado com exito!!!' + color.END)
        print(color.RED + '~~' * 25 + color.END)
        sys.exit()

def criar_planilha():
    with open('Login_users.txt' , 'a+') as f:
        f.write(f'{login} {password}\n')

clear()
layout()
main()