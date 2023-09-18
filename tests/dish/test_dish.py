from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish_1 = Dish("Carne de Panela", 10.0)
    dish_2 = Dish("Arroz com Milho", 50.0)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Carne de Panela", "10.0")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Carne de Panela", 0)

    assert dish_1.name == "Carne de Panela"
    assert dish_2.name == "Arroz com Milho"

    assert dish_1.price == 10.0
    assert dish_2.price == 50.0

    assert hash(dish_1) == hash("Dish('Carne de Panela', R$10.00)")
    assert hash(dish_2) == hash("Dish('Arroz com Milho', R$50.00)")

    assert dish_1 != dish_2
    assert dish_1 == dish_1
    assert dish_1.__eq__(dish_1) is True
    assert dish_1.__eq__(dish_2) is False

    assert repr(dish_1) == "Dish('Carne de Panela', R$10.00)"
    assert repr(dish_2) == "Dish('Arroz com Milho', R$50.00)"

    dish_1.add_ingredient_dependency(Ingredient("ovo"), 2)
    dish_1.add_ingredient_dependency(Ingredient("bacon"), 1)
    dish_1.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)

    dish_2.add_ingredient_dependency(Ingredient("farinha"), 2)
    dish_2.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    dish_2.add_ingredient_dependency(Ingredient("presunto"), 1)

    assert dish_1.recipe == {
        Ingredient("ovo"): 2,
        Ingredient("bacon"): 1,
        Ingredient("queijo mussarela"): 1,
    }

    assert dish_2.recipe == {
        Ingredient("farinha"): 2,
        Ingredient("queijo mussarela"): 1,
        Ingredient("presunto"): 1,
    }

    assert dish_1.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
    }

    assert dish_2.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish_1.get_ingredients() == {
        Ingredient("ovo"),
        Ingredient("bacon"),
        Ingredient("queijo mussarela"),
    }

    assert dish_2.get_ingredients() == {
        Ingredient("farinha"),
        Ingredient("queijo mussarela"),
        Ingredient("presunto"),
    }
