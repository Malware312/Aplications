from os import system as s ; from platform import system

class Program:
  def clear(self):
    self.os = system()
    if self.os == ' w indow': s('clear')
    else: s('cls')
  
  def color(self):
    self.blue = '\033[1;96m'
    self.red = '\033[1;31m'
    self.black = '\033[1;30m'
    self.end = '\033[m'

  def layout(self , line = '~~' * 25 , msg='Program'):
    self.x = self.blue + line + self.end
    self.y = msg.center(50)
    print(self.x , '\n' , self.y , '\n' , self.x , sep='')

    print('Opçoes\n1 - Start \n2 - Exit')

    try:
      c = Program()
      self.op = int(input('Test\n'))

      if self.op > 2:
        main.clear()
        main.color()
        main.layout()

      elif self.op < 1:
        main.clear()
        main.color()
        main.layout()

    except:
      print('Error')
      main.clear()
      main.color()
      main.layout()

    if self.op == 1:
      print('1')
    
    elif self.op == 2:
      print('2')

if __name__ == '__main__':  
  main = Program()
  main.clear()
  main.color()
  main.layout()