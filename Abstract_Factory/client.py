"Abstract Factory Use Case Example Code"
from furniture_factory import FurnitureFactory
from collections import Counter


def main():
    FURNITURE = FurnitureFactory.get_furniture("SmallChair")
    print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")

    FURNITURE = FurnitureFactory.get_furniture("MediumTable")
    print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")


if __name__ == '__main__':
    main()
