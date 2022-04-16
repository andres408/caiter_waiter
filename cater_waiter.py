'''Program to caiter service in exercism web site'''
from sets_categories_data import (VEGAN, VEGETARIAN, KETO, PALEO, OMNIVORE, ALCOHOLS, SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    '''
    param dish_name: str
    param dish_ingredients: list
    return: tuple of (dish_name, dish ingredients set)
    '''
    clean =(dish_name,set(dish_ingredients))
    return clean

if __name__ == '__main__':
    print(clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']))

from sets_categories_data import ALCOHOLS

def check_drinks(drink_name, drink_ingredients):
     """
    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")
    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

     #for items in drink_ingredients:
     if ALCOHOLS.isdisjoint(drink_ingredients):
         return f'{drink_name} Cocktail'
     return f'{drink_name} Mocktail'
if __name__=='__main__':
    print(check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']))
    print(check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda']))

def categorize_dish(dish_name, dish_ingredients):
    """
     :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """
    category = {'VEGAN':VEGAN,
               'VEGETARIAN':VEGETARIAN,
               'KETO':KETO,
               'PALEO':PALEO,
               'OMNIVORE':OMNIVORE}
    for key,value in category.items():
        if set(dish_ingredients)<=(value):
           return f'{dish_name}: {key}'
   
   
if __name__=='__main__':
    print(categorize_dish('Sticky Lemon Tofu', ['tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar']))
    print('Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', ['shrimp', 'bacon', 'avocado', 'chickpeas', 'fresh tortillas', 'sea salt', 'guajillo chile', 'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion'])
    print(categorize_dish('dish 1',['almonds','chives','limes']))
    print(categorize_dish('dish 2',['clams','prawns', 'white wine vinegar']))



def tag_special_ingredients(dish):
    """
    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
   
    allergens = (dish[0], SPECIAL_INGREDIENTS.intersection(dish[1]))
    return allergens

if __name__=='__main__':
    print(tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'])))
    print(tag_special_ingredients(('Arugula and Roasted Pork Salad', ['pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts', 'balsamic vinegar', 'onions', 'black pepper'])))


def compile_ingredients(dishes):
    """
    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    """
    total_ingredients = set()
    for ingredients in dishes:
        total_ingredients = total_ingredients.union(ingredients)
    return total_ingredients

if __name__=='__main__':
    print(compile_ingredients(dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]))

def separate_appetizers(dishes,appetizers):
    """
    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    dishes =    ['Avocado Deviled Eggs',
                 'Flank Steak with Chimichurri and Asparagus',
                 'Kingfish Lettuce Cups',
                 'Grilled Flank Steak with Caesar Salad',
                 'Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
                 'Barley Risotto','Kingfish Lettuce Cups']
          
    appetizers = ['Kingfish Lettuce Cups',
                  'Avocado Deviled Eggs',
                  'Satay Steak Skewers',
                  'Dahi Puri with Black Chickpeas',
                  'Avocado Deviled Eggs','Asparagus Puffs',
                  'Asparagus Puffs']
    return set(dishes).symmetric_difference(appetizers)

if __name__=='__main__':
    print(separate_appetizers(dishes=['Avocado Deviled Eggs',
                 'Flank Steak with Chimichurri and Asparagus',
                 'Kingfish Lettuce Cups',
                 'Grilled Flank Steak with Caesar Salad',
                 'Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
                                      'Barley Risotto','Kingfish Lettuce Cups'],appetizers=['Kingfish Lettuce Cups',
                  'Avocado Deviled Eggs',
                  'Satay Steak Skewers',
                  'Dahi Puri with Black Chickpeas',
                  'Avocado Deviled Eggs','Asparagus Puffs',
                  'Asparagus Puffs']))


from sets_categories_data import example_dishes,EXAMPLE_INTERSECTION

def singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION):
    singleton=set()
    for dish in example_dishes:
        singleton |= dish - EXAMPLE_INTERSECTION
    return singleton 

if __name__=='__main__':
    print(singleton_ingredients(example_dishes,EXAMPLE_INTERSECTION))
    

