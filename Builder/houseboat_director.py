from house_builder import HouseBuilder


class HouseBoatDirector:
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("House Boat")\
            .set_number_doors(6)\
            .set_number_windows(8)\
            .set_wall_material("Wood")\
            .get_result()