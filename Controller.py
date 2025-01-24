

class Controller:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.recipe = None

  def user_Register(self, userData):
    self.model.user_Register(userData)

  def signIn(self, userData):
    userLogin = self.model.filled(userData)
    if userLogin:
      self.view.page.go("/homePage")

  def ingredients_register(self, ingredientsData):
    return self.model.ingredients_register(ingredientsData)
  
  def cake_pan_register(self, panData):
    self.model.pan_type(panData)

  def get_recipe(self):
    print(self.user)
    return self.model.get_recipe()
  
  def get_recipe_name(self):
    return self.model.get_recipe_name(self.recipe)
  
  def get_recipe_ingredients(self):
    return self.model.get_recipe_ingredients(self.recipe)
  
  def get_cake_pan(self):
    return self.model.get_cake_pan()
  
  def set_recipe_name(self, recipe):
    self.recipe = recipe
