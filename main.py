import flet as ft
from Controller import Controller
from Model import Model

from View.HomePage import HomePage
from View.RecipeBook import RecipeBook
from View.Recipe import RecipePage
from View.Login import LoginPage
from View.SignupPage import SignupPage
from View.UserPage import UserPage
from View.IngredientsPage import IngredientsPage
from View.CakePanPage import CakePanPage
from View.IngredientRegister import IngredientRegister
from View.CakePanRegister import CakePanRegister
from View.EditUser import EditUser
from View.EditIngredients import EditIngredients
from View.EditCakePan import EditCakePan

class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        self.model = Model()
        self.controller = Controller(self, self.model)

        self.routes = {
            "/login": LoginPage,
            "/homePage": HomePage,
            "/recipePage": RecipePage,
            "/recipeBook": RecipeBook,
            "/signupPage": SignupPage,
            "/userPage": UserPage,
            "/ingredientsPage": IngredientsPage,
            "/cakePanPage": CakePanPage,
            "/ingredientRegister": IngredientRegister,
            "/cakePanRegister": CakePanRegister,
            "/editUser": EditUser,
            "/editIngredients": EditIngredients,
            "/editCakePan": EditCakePan,
        }
        self.page.on_route_change = self.route_change
        self.page.go("/login") 

    def route_change(self, route):
        self.page.controls.clear()

        pageRoute = self.routes.get(self.page.route)

        page = pageRoute(self.page, self.controller)

        self.page.controls.append(page.page_content())

        self.page.update() 

def main(page: ft.Page):
    Main(page)

ft.app(target=main)
