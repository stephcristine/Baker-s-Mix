

class Controller:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.recipe = None
    self.user = None

  def userRegister(self, userData):
    self.model.userRegister(userData)

  def signIn(self, userData):
    userLogin = self.model.filled(userData)
    if userLogin:
      self.user = userLogin['_id']
      self.view.page.go("/homePage")

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
