import math
import pymongo

class Model:
  def __init__(self):
    self.receitasCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Receitas']
    self.ingredientesCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Ingredientes']
    self.usuariosCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Usuarios']
    self.formasCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Formas']
    self.conversaoCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Conversao']

    self.userId = None
    self.userIngredientId = None
    self.userCakePan = None

# Funções relacionas aos dados de cadastro do usuário
  def user_Register(self, userData):
    data = {
      "nome": userData[0],
      "email": userData[1],
      "senha": userData[2]
    }

    return self.usuariosCollection.insert_one(data)
  
  def get_user(self):
    return self.usuariosCollection.find_one({'_id': self.userId})

  def edit_user_verification(self, newData):
    update = {}

    if newData[0] != '':
      update['nome'] = newData[0]
    if newData[1] != '':
      update['email'] = newData[1]
    if newData[2] != '':
      update['senha'] = newData[2]

    if update:
      self.edit_user(update) 

  def edit_user(self, newData):
    self.usuariosCollection.update_one({"_id": self.userId}, {"$set": newData})

  def delete_user(self):
    pass

  def filled(self, userData):
    if userData[0] != '' and userData[1] != '':
      return self.signIn(userData)
    else:
      return False
    
  def signIn(self, userData):
    data = {
      "nome": userData[0],
      "senha": userData[1]
    }
    user = self.usuariosCollection.find_one(data)
    self.set_user_id(user)

    return user
  
  def set_user_id(self, id):
    self.userId = id['_id']
  
# Funções relacionadas ao dados de ingredientes e formas do usuário
  def ingredients_register(self, ingredientsData):
    data = {
      "usuario": self.userId,
      "nome": ingredientsData[0],
      "quantidade": ingredientsData[1],
      "unidade": ingredientsData[2]
    }

    return self.ingredientesCollection.insert_one(data)

  def cake_pan_register(self, volumeData):
    data = {
      "usuario": self.userId,
      "tipo": self.panData[0],
      "diametro": self.panData[1],
      "altura": self.panData[2],
      "volumeTotal": volumeData[0],
      "capacidadeUtil": volumeData[1]
    }

    return self.formasCollection.insert_one(data)

  def set_user_ingredient_id(self, editIngredient):
    self.userIngredientId = editIngredient['_id']

  def set_user_cake_pan_id(self, cakePan):
    self.userCakePan = cakePan['_id']

  def get_user_ingredients(self):
    ingredientsList = list(self.ingredientesCollection.find({"usuario": self.userId}))

    return ingredientsList

  def get_user_edit_ingredient(self):
    return self.ingredientesCollection.find_one({"_id": self.userIngredientId})

  def get_user_cake_pan(self):
    panList = list(self.formasCollection.find({"usuario": self.userId}))
    return panList

  def get_user_edit_cake_pan(self):
    return self.formasCollection.find_one({"_id": self.userCakePan})

  def edit_user_ingredient_verification(self, newIngredient):
    update = {}

    if newIngredient[0] != '':
      update['nome'] = newIngredient[0]
    if newIngredient[1] != '':
      update['quantidade'] = newIngredient[1]
    if newIngredient[2] != '':
      update['unidade'] = newIngredient[2]

    if update:
      self.edit_user_ingredient(update) 

  def edit_user_ingredient(self, newIngredient):
    self.ingredientesCollection.update_one({"_id": self.userIngredientId}, {"$set": newIngredient})

  def edit_user_cake_pan(self, newCakePan):
    self.formasCollection.update_one({"_id": self.userCakePan}, {"$set": newCakePan})

  def delete_user_ingredient(self):
    self.ingredientesCollection.delete_one({"_id": self.userIngredientId})
    self.userIngredientId = None

  def delete_user_cake_pan(self):
    self.formasCollection.delete_one({"_id": self.userCakePan})
    self.userCakePan = None

  def convert_pan_data(self, panData):
    self.panData = list(panData)

    if self.panData[0] == 'circular':
      for i in range(1, 3):
        self.panData[i] = float(self.panData[i])
      self.calculate_cylinder_volume()
    else:
      for i in range(2,5):
        self.panData[i] = float(self.panData[i])
      self.calculate_rectangular_prism_volume()

  def calculate_cylinder_volume(self):
    volume = (math.pi * ((self.panData[1]/2) ** 2) * self.panData[2])
    self.calculate_useful_capacity(volume)
    
  def calculate_rectangular_prism_volume(self):
    volume = (self.panData[3] * self.panData[4] * self.panData[2])
    self.calculate_useful_capacity(volume)
  
  def calculate_useful_capacity(self, volume):
    usefulCapacity = volume * 0.8
    volumeData = (volume, usefulCapacity)
    self.cake_pan_register(volumeData)
   
# Funções relacionadas a busca das receitas e ingredientes do aplicativo
  def get_recipe(self):
    recipeName = self.receitasCollection.find({}, {"_id": 0, "nome": 1})
    recipeList = [recipe["nome"] for recipe in recipeName]

    return recipeList
  
  def get_recipe_name(self, name):
    return self.receitasCollection.find_one({"nome": name})
  
  def get_recipe_ingredients(self, name):
    recipe = self.receitasCollection.find_one({"nome": name})

    return recipe["ingredientes"]
  
  def get_ingredients_conversion(self):
    return list(self.conversaoCollection.find({}, {"_id": 0, "categoria": 1, "ingrediente": 1}))

  def compare_recipe_with_conversion(self, recipeName):
    recipe = self.get_recipe_name(recipeName)
    conversionData = self.get_ingredients_conversion()

    comparisonResult = []

    for recipeIngredient in recipe['ingredientes']:
      ingredientName = recipeIngredient['nome']
      matchCategory = None
      for category in conversionData:
        if ingredientName in category['ingrediente']:
          matchCategory = category['categoria']
          break
      if matchCategory:
        comparisonResult.append({
          "ingrediente": ingredientName,
          "categoria": matchCategory
        })
      else:
        comparisonResult.append({
          "ingrediente": ingredientName,
          "categoria": None
        })

    self.convert_ingredients(comparisonResult)
  
  def convert_ingredients(self,comparisonResult):
    for i in comparisonResult:
      pass
