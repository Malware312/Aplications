from random import randint ; from os import system ;from time import sleep

class Game:

    def clear(c):
        c = ''
        if c == '':
            system('clear')
        if c == '':
            system('cls')

    def color(self):
        self.blue = '\033[1;96m'
        self.red = '\033[1;31m'
        self.end = '\033[m'

    def layout(self):
        global line
        line = self.blue + '~~' * 25 + self.end 
        msg = 'Bem-Vindo'
        msg2 = 'Jogo de adivinhaçao'

        print(line)
        print(msg.center(50))
        print(msg2.center(50))
        print(line)

        print('Option\n1 - Start\n2 - Exit')

    def option(self):
        try:
            print(line)
            self.op = int(input('Informe a opçao que deseja utilizar:\n'))
            print(line)

            if self.op > 2:
                main.clear()
                main.color()
                main.layout()
                main.option()

            elif self.op < 1:
                main.clear()
                main.color()    
                main.layout()
                main.option()

        except:
            main.clear()
            main.color()
            main.layout()
            main.option()

        if self.op == 1:
            computer = randint(0 , 10)
            cont = 0
            jogadas = 4
            
            while True:
                try:
                    player = int(input('Consegue adivinhar qual foi o numero gerado?\n'))
                except:
                    main.clear()
                    main.color()
                    main.layout()
                    main.option()

                if player == computer:
                    print(self.blue + 'Parabens voce venceu!!!' + self.end)
                    print(line)
                    self.continuar = str(input('Deseja continuar (S/N)\n')).lower().strip()
                    print(line)

                    if self.continuar == 's':
                        main.clear()
                        main.color()
                        main.layout()
                        main.option()
                    
                    else:
                        print(line)
                        print(self.red + 'Programa finalizado com exito!!!' + self.end)
                        print(line)
                        exit()
                elif player > computer:
                    print(line)
                    print(self.blue + 'Dimunua mais o numero!!!' + self.end)
                    print(line)

                elif player < computer:
                    print(line)
                    print(self.blue + 'Aumente mais o numero!!!' + self.end)
                    print(line)
        else:
            print(line)
            print(self.red + 'Programa finalizado com exito!!!' + self.end)
            print(line)
            exit()


if __name__ == '__main__':
    main = Game()
    main.clear()
    main.color()
    main.layout()
    main.option()