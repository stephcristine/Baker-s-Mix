import flet as ft

class IngredientRegister:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller

  def page_content(self):
    title = ft.Text(
      "CADASTRO DE INGREDIENTES",
      size=30,
      weight=ft.FontWeight.BOLD,
      color="white",
      text_align=ft.TextAlign.CENTER,
    )
    self.ingredient = ft.TextField(
      label="Nome do ingrediente",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
    )
    self.amount = ft.TextField(
      label="Quantidade",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
    )
    self.unit = ft.Dropdown(
        label="Selecione a unidade do produto",
        options=[
            ft.dropdown.Option("Quilos"),
            ft.dropdown.Option("Gramas"),
            ft.dropdown.Option("Litros"),
            ft.dropdown.Option("Unidade"),
        ],
    ),
    registerButton = ft.ElevatedButton(
      text="CADASTRAR",
      style=ft.ButtonStyle(
        bgcolor="#6691e8",
        color="white",
        shape=ft.RoundedRectangleBorder(radius=30),
        padding=ft.Padding(15, 15, 15, 15),
      ),
      on_click=lambda e: self.register(),
    )

    container = ft.Container(
      content=ft.Column(
        [
          title,
          self.ingredient,
          self.amount,
          self.unit,
          registerButton,
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      ),
      width=400,
      height=400,
      bgcolor="#85d4ff",
      border_radius=20,
      alignment=ft.alignment.center,
      padding=20,
    )

    return ft.Column(controls=[container])

  def register(self):
    userData = (self.ingredient.value, self.amount.value, self.unit.value)
    self.controller.register(userData)
    print(self.unit)
