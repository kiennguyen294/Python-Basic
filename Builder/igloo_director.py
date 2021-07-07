from house_builder import HouseBuilder


class IglooDirector:

    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_building_type("Igloo") \
            .set_wall_material("Ice") \
            .set_number_doors(1) \
            .get_result()
