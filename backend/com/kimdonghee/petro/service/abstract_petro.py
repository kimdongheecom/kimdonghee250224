


from abc import ABCMeta, abstractmethod


class AbstractPetro(metaclass=ABCMeta):
    
    @abstractmethod
    def handle(self, **kwargs):
        pass