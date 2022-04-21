from threading import Thread

class Program:
  def __init__(self , name) -> None:
      Thread.__init__(self)
      self.name = name

  def run(self):
    for i in range(10000000):
      self.msgmsg = '%s is running' % \
        self.name
      print(self.msg)

def creation():
  for i in range(10000000):
    name = 'Thread 3%s' % (i + 1)
    thread =  Program(name)
    thread.start()

if __name__ == '__main__':
  main = Program()
  main.__init__()
  main.run()
  main.creation()
