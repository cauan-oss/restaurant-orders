import csv
from models.ingredient import Ingredient
from models.dish import Dish

DATA_PATH = "data/menu_base_data.csv"


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding="utf-8") as file:
            source = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = source
        self.header = header
        self.data = data
        self.dishes = self.loading()

    def loading(self):
        new_dict = dict()
        for item in self.data:
            if item[0] not in new_dict:
                new_instance = Dish(item[0], float(item[1]))
                new_dict[item[0]] = new_instance

            new_ingredient = Ingredient(item[2])
            new_dict[item[0]].add_ingredient_dependency(
                new_ingredient, int(item[3])
            )
        return set(new_dict.values())
