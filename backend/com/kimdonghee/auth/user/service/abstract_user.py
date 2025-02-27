from abc import ABCMeta, abstractmethod


class AbstractUser(metaclass=ABCMeta): #부모 클래스 = 추상 클래스 
    @abstractmethod
    def handle(self, **kwargs):
        pass