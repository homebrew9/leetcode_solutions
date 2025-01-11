#
# Couldn't make it work!
#
from threading import Thread

class Foo:
    def __init__(self):
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

def printFirst():
    print('first')

def printSecond():
    print('second')

def printThird():
    print('third')

f = Foo()

f.third(printThird)
f.second(printSecond)
f.first(printFirst)


threads = list()

x = Thread(target=f.third, args=printThird)
threads.append(x)

x = Thread(target=f.second, args=printSecond)
threads.append(x)

x = Thread(target=f.first, args=printFirst)
threads.append(x)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()




# ===============================================

#  from threading import Semaphore
#  
#  class Foo:
#      def __init__(self):
#          self.two = Semaphore(0)
#          self.three = Semaphore(0)
#  
#      def first(self, printFirst):
#          printFirst()
#          self.two.release()
#  
#      def second(self, printSecond):
#          with self.two:
#              printSecond()
#              self.three.release()
#  
#      def third(self, printThird):
#          with self.three:
#              printThird()
#  

# ===============================================

