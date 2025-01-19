import threading

class FooBar:
    def __init__(self, n):
        self.n = n
    def printFoo(self):
        print('foo')
    def printBar(self):
        print('bar')
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            #print('foo', end='')
    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            #print('bar', end='')

class FooBar1:
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.bar_lock.acquire()
    def printFoo(self):
        print('foo')
    def printBar(self):
        print('bar')
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()
    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()

# Main section
if __name__ == '__main__':
    fb = FooBar(5)
    threads = list()
    for i in range(2):
        if i == 0:
            t = threading.Thread(target=fb.foo(fb.printFoo))
        else:
            t = threading.Thread(target=fb.bar(fb.printBar))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print('===============================') 
    fb1 = FooBar1(5)
    threads1 = list()
    for i in range(2):
        if i == 0:
            t1 = threading.Thread(target=fb1.foo(fb1.printFoo))
        else:
            t1 = threading.Thread(target=fb1.bar(fb1.printBar))
        t1.start()
        threads1.append(t1)
    for thread in threads1:
        thread.join()


# fb = FooBar(5)
# fb.foo(fb.printFoo)
# fb.bar(fb.printBar)
# 
# 
# # =========================================
# 
# from threading import Lock
# 
# class FooBar:
#     def __init__(self, n):
#         self.n = n
#         self.foo_lock = Lock()
#         self.bar_lock = Lock()
#         self.bar_lock.acquire()
#     def printFoo(self):
#         print('foo')
#     def printBar(self):
#         print('bar')
#     def foo(self, printFoo: 'Callable[[], None]') -> None:
#         for i in range(self.n):
#             self.foo_lock.acquire()
#             # printFoo() outputs "foo". Do not change or remove this line.
#             printFoo()
#             self.bar_lock.release()
#     def bar(self, printBar: 'Callable[[], None]') -> None:
#         for i in range(self.n):
#             self.bar_lock.acquire()
#             # printBar() outputs "bar". Do not change or remove this line.
#             printBar()
#             self.foo_lock.release()
# 
# 
# fb = FooBar(5)
# fb.foo(fb.printFoo)
# fb.bar(fb.printBar)
# 
# 
# 
# 
# 
