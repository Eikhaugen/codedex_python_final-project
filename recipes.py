class Recipes:
    def __init__(self, title, ingredients, steps):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps

recipes_list = [
Recipes("Toast", ["Bread", "Cheese", "Ham"], ["Step 1: Add cheese and ham between two slices of bread.", "Step 2: Toast.", "Step 3: ???", "Step 4: Satisfy Your cravings."]),
Recipes("Cereal", ["Cereal", "Milk"], ["Step 1: Add milk to bowl.","Step 2: Add cereal to bowl.", "Step 3: Realize what you just did.", "Step 4: Cry in a corner."]),
Recipes("Noodles", ["Noodles", "Water"], ["Step 1: Boil water.", "Step 2: Add noodles to pot and boil, for what will seem an eternity.", "Step 3: Add flavour packet to pot and stir.", "Step 4: Pour noodles into a bowl and enjoy!"])
]