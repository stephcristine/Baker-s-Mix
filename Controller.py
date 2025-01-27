

class Controller:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.recipe = None

# Funções relacionas aos dados de cadastro do usuário
  def user_Register(self, userData):
    self.model.user_Register(userData)

  def get_user(self):
    return self.model.get_user()

  def edit_user(self, newData):
    return self.model.edit_user_verification(newData)

  def delete_user(self):
    self.model.delete_user()

  def signIn(self, userData):
    userLogin = self.model.filled(userData)
    if userLogin:
      self.view.page.go("/homePage")

# Funções relacionadas ao dados de ingredientes e formas do usuário
  def ingredients_register(self, ingredientsData):
    return self.model.ingredients_register(ingredientsData)

  def cake_pan_register(self, panData):
    self.model.convert_pan_data(panData)

  def set_user_ingredient_id(self, ingredient):
    self.model.set_user_ingredient_id(ingredient)

  def set_user_cake_pan_id(self, cakePan):
    self.model.set_user_cake_pan_id(cakePan)

  def get_user_ingredients(self):
    return self.model.get_user_ingredients()

  def get_user_cake_pan(self):
    return self.model.get_user_cake_pan()

  def get_user_edit_ingredient(self):
    return self.model.get_user_edit_ingredient()
  
  def get_user_edit_cake_pan(self):
    return self.model.get_user_edit_cake_pan()

  def edit_user_ingredient(self, newIngredient):
    return self.model.edit_user_ingredient_verification(newIngredient)

  def edit_user_cake_pan(self, newCakePan):
    self.model.edit_user_cake_pan(newCakePan)

  def delete_user_ingredient(self):
    self.model.delete_user_ingredient()

  def delete_user_cake_pan(self):
    self.model.delete_user_cake_pan()

# Funções relacionadas as receitas e ingredientes do aplicativo
  def get_recipe(self):
    return self.model.get_recipe()
  
  def get_recipe_name(self):
    return self.model.get_recipe_name(self.recipe)
  
  def get_recipe_ingredients(self):
    return self.model.get_recipe_ingredients(self.recipe)
  
  def set_recipe_name(self, recipe):
    self.recipe = recipe

  def compare_recipe_with_conversion(self):
    self.model.compare_recipe_with_conversion(self.recipe)
