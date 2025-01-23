import math
import pymongo

class Model:
  def __init__(self):
    self.receitasCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Receitas']
    self.ingredientesCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Ingredientes']
    self.UsuariosCollection = pymongo.MongoClient('localhost', 27017)['BakersMix']['Usuarios']

  def userRegister(self, userData):
    userData = {
      "nome": userData[0],
      "email": userData[1],
      "senha": userData[2]
    }
    return self.UsuariosCollection.insert_one(userData)
  
  def filled(self, userData):
    if userData[0] != '' and userData[1] != '':
      return self.signIn(userData)
    else:
      return False
    
  def signIn(self, userData):
    loginData = {
      "nome": userData[0],
      "senha": userData[1]
    }
    return self.UsuariosCollection.find_one(loginData)

  def calculate_cylinder_volume(self, diameter, height):
    volume = (math.pi * ((diameter/2) ** 2) * height)
    return print(round(volume, 2))

  def calculate_rectangular_prism_volume(self, length, width, height):
    volume = (length * width * height)
    return print(volume) 
  
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
  

teste = Model()
teste.get_cake_pan()
