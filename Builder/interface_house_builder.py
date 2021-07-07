from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        "Building type"

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        "Build material"

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        "number of windows"

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        "Number of windows"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"
