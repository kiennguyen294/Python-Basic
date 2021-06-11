from abc import ABCMeta, abstractmethod
from factory_a import FactoryA
from factory_b import FactoryB


class IAbstractFactory(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object(factory):
        """The static Abstract factory interface method"""


class AbstractFactory(IAbstractFactory):
    """The Abstract Factory Concrete class"""

    @staticmethod
    def create_object(factory):
        "Static get_factory method"
        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA().create_object(factory[1])
            if factory in ['bb', 'ba', 'bc']:
                return FactoryB().create_object(factory[1])
            raise Exception('No Factory Found')
        except Exception as _e:
            print(e)
        return None


def main():
    PRODUCT = AbstractFactory.create_object('ab')
    print(f"{PRODUCT}")
    PRODUCT = AbstractFactory.create_object('bc')
    print(f"{PRODUCT}")


if __name__ == '__main__':
    main()