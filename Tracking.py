__author__ = 'Steve'
class Observable(object):
    def __init__(self):
        super().__init__()
        self._observers = []

    def addObserver(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notifyObservers(self):
        for observer in self._observers:
            observer.updateObserver(self)

class Observer(object):
    def __init__(self):
        super().__init__()

    def updateObserver(self, observable):
        pass