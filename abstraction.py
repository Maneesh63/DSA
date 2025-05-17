from abc import ABC, abstractmethod

class BaseClass(ABC):

      @abstractmethod
      def test1(self):
          pass

class SubClass(BaseClass):

     def test1(self):
         print("IT WORKED")

     def test3(self):
         print("TO CHECK")


instance = SubClass()
instance.test1()