import math
import pymongo

class Model:
  def __init__(self):
    self.receitasCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Receitas']
    self.ingredientesCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Ingredientes']
    self.usuariosCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Usuarios']
    self.formasCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Formas']

    self.userId = None

  def user_Register(self, userData):
    data = {
      "nome": userData[0],
      "email": userData[1],
      "senha": userData[2]
    }
    return self.usuariosCollection.insert_one(data)
  
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
  
  def ingredients_register(self, ingredientsData):
    data = {
      "usuario": self.userId,
      "nome": ingredientsData[0],
      "quantidade": ingredientsData[1],
      "unidade": ingredientsData[2]
    }
    return self.ingredientesCollection.insert_one(data)
  
  def pan_type(self, panData):
    if panData[0] == "circular":
      self.calculate_cylinder_volume(panData)
    else:
      self.calculate_rectangular_prism_volume(panData)

  def calculate_cylinder_volume(self, panData):
    volume = (math.pi * ((panData[1]/2) ** 2) * panData[2])
    self.calculate_useful_capacity(volume)
    
  def calculate_rectangular_prism_volume(self, length, width, height):
    volume = (length * width * height)
    self.calculate_useful_capacity(volume)
  
  def calculate_useful_capacity(self, volume):
    usefulCapacity = volume * 0.8
    
  def cake_pan_register(self, userId, panData):
    data = {
      "usuario": userId,
      "tipo": panData[0],
      "diametro": panData[1],
      "altura": panData[2],
      "volumeTotal": '',
      "capacidadeUtil": ''
    }
    return self.formasCollection.insert_one(data)

  def add_recipe(self):
    nova_receita = {
      "tipo": "redonda",
      "diametro": 20,
      "altura": 15
    }
    resultado = self.ingredientesCollection.insert_one(nova_receita)

  def get_recipe(self):
    recipeName = self.receitasCollection.find({}, {"_id": 0, "nome": 1})

    recipeList = [recipe["nome"] for recipe in recipeName]

    return recipeList
  
  def get_recipe_name(self, name):
    recipe = self.receitasCollection.find_one({"nome": name})

    return recipe["nome"]
  
  def get_recipe_ingredients(self, name):
    recipe = self.receitasCollection.find_one({"nome": name})

    return recipe["ingredientes"]
  
  def get_cake_pan(self):
    panName = self.receitasCollection.find({}, {"_id": 0, "forma": 1})

    panList = [pan["forma"] for pan in panName]

    return panList
  