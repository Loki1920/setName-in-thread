#setName in thread

from threading import Thread ,current_thread

def disp():
  print("default child thread:",current_thread().getName())
  current_thread().setName('Tony')
  print("new child Thread Name:",current_thread().getName())

t = Thread(target=disp)
t.start()

print("default thread name:",current_thread().getName())
current_thread().setName("lucky")
print("new main Thread Name:",current_thread().getName())