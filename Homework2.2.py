#№1#
class Sauce:
  MAIN = "Mayoneize"

  def __init__(self, addition : str = None):
    self.addition = addition

  def show_my_sauce(self):
    if self.addition:
      print(f"Sauce is {self.addition}")
    else:
      print(str(Sauce.MAIN))

s_1 = Sauce()
s_2 = Sauce("Cheese")

s_1.show_my_sauce()
s_2.show_my_sauce()

#№3#
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f"Ингредиенты для {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}") 
    
    def cook(self):
        print(f"Сегодня мы готовим {self.name}") 
        print(f"Выполняем инструкцию по приготовлению блюда {self.name}")

# Example usage
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
spaghetti.print_ingredients()
spaghetti.cook()  
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
cake.print_ingredients()
cake.cook()