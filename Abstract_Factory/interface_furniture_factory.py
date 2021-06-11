from abc import ABCMeta, abstractmethod


class IFurnitureFactory(metaclass=ABCMeta):
    """Abstract Furniture Factory Interface"""

    @staticmethod
    @abstractmethod
    def get_funirture(furniture):
        """The static Abstract factory interface method"""
