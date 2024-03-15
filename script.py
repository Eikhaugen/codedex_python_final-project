from recipes import recipes_list

def welcome():
    print("Welcome to this scuffed cookbook")
    print("Here are the available recipes:")
    for i, recipe in enumerate(recipes_list):
        print(f'{i + 1}, {recipe.title}')

    while True:
        try:
            selected_recipe = int(input("Please select a recipe by number: ")) - 1
            if 0 <= selected_recipe < len(recipes_list):
                display_recipe(selected_recipe)
                if not display_another_recipe():
                    break
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_recipe(selected_recipe):
    print("\n" + "="*30)
    print(recipes_list[selected_recipe].title)
    print("="*30 + "\n")
    print("Ingredients:")
    for ingredient in recipes_list[selected_recipe].ingredients:
        print(ingredient)
    print("\nSteps:")
    for step in recipes_list[selected_recipe].steps:
        print(step)
    print("="*30)

def display_another_recipe():
    while True:
        choice = input("\nDo you want to display another recipe or list all recipes again? (y/n): ").strip().lower()
        if choice == 'y' or choice == 'yes':
            list_recipes()
            return True
        elif choice == 'n' or choice == 'no':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def list_recipes():
    print("\n" + "="*30)
    print("Here are the available recipes:")
    for i, recipe in enumerate(recipes_list):
        print(f'{i + 1}, {recipe.title}')
    print("="*30)

welcome()
