from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 1
def test_ingredient():
    ing_1 = Ingredient("carne")
    ing_2 = Ingredient("frango")
    ing_3 = Ingredient("carne")
    assert ing_1.name == "carne"
    assert ing_1.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert ing_1.__eq__(ing_2) is False
    assert ing_1.__eq__(ing_3) is True
    assert repr(ing_1) == "Ingredient('carne')"
    assert hash(ing_1) == hash(ing_3)
    assert hash(ing_1) != hash(ing_2)
