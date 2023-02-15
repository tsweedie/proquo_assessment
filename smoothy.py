import argparse
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class DataClassSmoothy:
    name: str
    fruits: list
    total_vitamin_c: float
    total_weight_grams: int
    total_citrus_percentage: float
    top_two_flavour_strength: list


class Fruit(ABC):
    def __init__(self, name: str, grams: int):
        self.name = name.lower()
        self.grams = grams

    @abstractmethod
    def is_citrus(self) -> bool:
        """

        :return:
        """
        pass

    @abstractmethod
    def flavour_strength(self) -> float:
        pass

    @abstractmethod
    def vitamin_c(self) -> float:
        pass

    def value_per_grams(self, value) -> float:
        return round(value * (self.grams / 100), 2)


class Apple(Fruit):
    def is_citrus(self) -> bool:
        return False

    def flavour_strength(self) -> float:
        return self.value_per_grams(50)

    def vitamin_c(self) -> float:
        return self.value_per_grams(75)


class Banana(Fruit):
    def is_citrus(self) -> bool:
        return False

    def flavour_strength(self) -> float:
        return self.value_per_grams(40)

    def vitamin_c(self) -> float:
        return self.value_per_grams(85)


class Orange(Fruit):
    def is_citrus(self) -> bool:
        return True

    def flavour_strength(self) -> float:
        return self.value_per_grams(70)

    def vitamin_c(self) -> float:
        return self.value_per_grams(150)


class Strawberry(Fruit):
    def is_citrus(self) -> bool:
        return False

    def flavour_strength(self) -> float:
        return self.value_per_grams(50)

    def vitamin_c(self) -> float:
        return self.value_per_grams(90)


class Lemon(Fruit):
    def is_citrus(self) -> bool:
        return True

    def flavour_strength(self) -> float:
        return self.value_per_grams(90)

    def vitamin_c(self) -> float:
        return self.value_per_grams(130)


def fruit_factory(name: str, grams: int) -> Fruit:
    """

    :return:
    """
    if name.lower() == 'apple':
        return Apple(name, grams)
    elif name.lower() == 'banana':
        return Banana(name, grams)
    elif name.lower() == 'orange':
        return Orange(name, grams)
    elif name.lower() == 'strawberry':
        return Strawberry(name, grams)
    elif name.lower() == 'lemon':
        return Lemon(name, grams)
    else:
        raise NotImplementedError


def parse_ingredients(ingredients: list) -> dict:
    """

    :return:
    """
    ingredients_dict = {}
    for i in ingredients:
        name = i[0]
        grams = int(i[1])
        if ingredients_dict.get(name) is not None:
            ingredients_dict[name] += grams
        else:
            ingredients_dict[name] = grams

    return ingredients_dict


def recipe(ingredients: list, smoothie_name: str) -> DataClassSmoothy:
    """

    :return:
    """
    ingredients_dict = parse_ingredients(ingredients)

    smoothy = DataClassSmoothy(
        name=smoothie_name,
        fruits=[],
        total_vitamin_c=0,
        total_weight_grams=0,
        total_citrus_percentage=0,
        top_two_flavour_strength=[],
    )

    citrus_grams = 0
    flavour_strength = {}
    for name, grams in ingredients_dict.items():

        try:
            fruit = fruit_factory(name, grams)
        except NotImplementedError:
            print("%s fruit doesn't exist" % name)
            continue

        flavour_strength[name] = fruit.flavour_strength()
        smoothy.total_vitamin_c += fruit.vitamin_c()
        smoothy.fruits.append(name)
        smoothy.total_weight_grams += grams

        if fruit.is_citrus():
            citrus_grams += grams

    if len(flavour_strength) > 2:
        smoothy.top_two_flavour_strength = sorted(flavour_strength)[:2]
    else:
        smoothy.top_two_flavour_strength = list(flavour_strength.keys())

    smoothy.total_citrus_percentage = round((citrus_grams/smoothy.total_weight_grams) * 100, 2)

    return smoothy


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True, help='give your smoothie a awesome name')
    parser.add_argument('--fruit', required=True, action='append', nargs=2, help='add various fruits to the smoothie')
    args = parser.parse_args()

    smoothy = recipe(args.fruit, args.name)

    print('==================================================')
    print('Breakdown for %s Smoothy'% smoothy.name)
    print('==================================================')
    print('List of all fruits used: ', smoothy.fruits)
    print('Total vitamin C: ', smoothy.total_vitamin_c)
    print('Total weight in grams: ', smoothy.total_weight_grams)
    print('Total citrus percentage: ', smoothy.total_citrus_percentage)
    print('Top two flavours (strength): ', smoothy.top_two_flavour_strength)
    print('==================================================')

# python smoothy.py --name "Strawberry Blaze" --fruit strawberry 200 --fruit banana 100 --fruit apple 50
# python smoothy.py --name "Citrus Infusion" --fruit orange 100 --fruit apple 75 --fruit lemon 100 --fruit orange 50
