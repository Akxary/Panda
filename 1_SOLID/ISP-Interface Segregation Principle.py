import abc

class Machine(abc.ABC):
    # Методы следует разделить, чтобы наследники
    # не имели неопределённых методов
    @abc.abstractmethod
    def print(self, document):
        pass
    @abc.abstractmethod
    def fax(self, document):
        pass
    @abc.abstractmethod
    def scan(self, document):
        pass

class MultiPrinter(Machine):
    def print(self, document):
        pass # ok
    def fax(self, document):
        pass # ok
    def scan(self, document):
        pass # ok

class OldFashionedPrinter(Machine):
    def print(self, document):
        pass #ok
    def fax(self, document):
        """Not supported!!!"""
        raise NotImplementedError # ne ok
    def scan(self, document):
        raise NotImplementedError # ne ok
# Project this way
class Printer(abc.ABC):
    @abc.abstractmethod
    def print(self, document):
        pass
class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan(self, document):
        pass