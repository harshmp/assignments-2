from pymongo import MongoClient
client = MongoClient()

import sys, threading, time

db = client.diningPhilosophers
collection = db.diningPhilosophersCollection

doc0 = {
"number": 0, "name": "A", "thought": "abc"
}
doc1 = {
"number": 1, "name": "B", "thought": "def"
}
doc2 = {
"number": 2, "name": "C", "thought": "ghi"
}
doc3 = {
"number": 3, "name": "D", "thought": "jkl"
}
doc4 = {
"number": 4, "name": "E", "thought": "mno"
}

doc_id = collection.insert_one(doc0)
doc_id = collection.insert_one(doc1)
doc_id = collection.insert_one(doc2)
doc_id = collection.insert_one(doc3)
doc_id = collection.insert_one(doc4)

class Semaphore(object):
    def __init__(self, initialAmountOfChopsticks):
        self.lock = threading.Condition(threading.Lock())
        self.chopsticksAvailable = initialAmountOfChopsticks

    def up(self):
        with self.lock:
            self.chopsticksAvailable += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.chopsticksAvailable == 0:
                self.lock.wait()
            self.chopsticksAvailable -= 1

class ChopStick(object):
    def __init__(self, chopStickId):
        self.chopStickId = chopStickId
        self.philosopherId = -1
        self.lock = threading.Condition(threading.Lock())
        self.chopStickTaken = False

    def take(self, philosopherId):
        with self.lock:
            while self.chopStickTaken == True:
                self.lock.wait()
            self.philosopherId = philosopherId
            self.chopStickTaken = True
            sys.stdout.write("p[%s] took c[%s]\n" % (philosopherId, self.chopStickId))
            self.lock.notifyAll()

    def drop(self, philosopherId):
        with self.lock:
            while self.chopStickTaken == False:
                self.lock.wait()
            self.philosopherId = -1
            self.chopStickTaken = False
            doc = collection.find_one({"number": philosopherId})
            sys.stdout.write("p[%s] dropped c[%s] and thought - %s\n" %(philosopherId, self.chopStickId, doc["thought"]))
            self.lock.notifyAll()

class Philosopher(threading.Thread):
    def __init__(self, philosopherId, leftChopStick, rightChopStick, butler):
        threading.Thread.__init__(self)
        self.philosopherId = philosopherId
        self.leftChopStick = leftChopStick
        self.rightChopStick = rightChopStick
        self.butler = butler

    def run(self):
        for i in range(20):
            self.butler.down()
            time.sleep(0.1)
            self.leftChopStick.take(self.philosopherId)
            time.sleep(0.1)
            self.rightChopStick.take(self.philosopherId)
            time.sleep(0.1)
            self.rightChopStick.drop(self.philosopherId)
            self.leftChopStick.drop(self.philosopherId)
            self.butler.up()
            sys.stdout.write("p[%s] finished thinking and eating.\n" % self.philosopherId)

def main():
    n = 5
    butler = Semaphore(n - 1)
    c = [ChopStick(i) for i in range(n)]
    p = [Philosopher(i, c[i], c[(i+1)%n], butler) for i in range(n)]

    for i in range(n):
        p[i].start()

if __name__ == "__main__":
    main()
