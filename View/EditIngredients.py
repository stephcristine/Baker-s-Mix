import flet as ft

class EditIngredients:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.get_user_edit_ingredient()

  def page_content(self):
    title = ft.Text(
      "CADASTRO DE INGREDIENTES",
      size=30,
      weight=ft.FontWeight.BOLD,
      color="white",
      text_align=ft.TextAlign.CENTER,
    )
    self.name = ft.TextField(
      label="Nome do ingrediente",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=5,
      value= self.ingredient['nome']
    )
    self.amount = ft.TextField(
      label="Quantidade",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=5,
      value= self.ingredient['quantidade']
    )
    self.unit = ft.Dropdown(
        label="Selecione a unidade do produto",
        bgcolor="#ffffff",
        value= self.ingredient['unidade'],
        options=[
          ft.dropdown.Option("Quilos"),
          ft.dropdown.Option("Gramas"),
          ft.dropdown.Option("Litros"),
          ft.dropdown.Option("Unidade"),
        ],
    )
    editButton = ft.ElevatedButton(
      text="EDITAR",
      style=ft.ButtonStyle(
        bgcolor="#6691e8",
        color="white",
        shape=ft.RoundedRectangleBorder(radius=30),
        padding=ft.Padding(15, 15, 15, 15),
      ),
      on_click=lambda e: self.edit_user_ingredient(),
    )

    container = ft.Container(
      content=ft.Column(
        [
          title,
          self.name,
          self.amount,
          self.unit,
          editButton,
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

  def get_user_edit_ingredient(self):
    self.ingredient = self.controller.get_user_edit_ingredient()

  def edit_user_ingredient(self):
    editIngredient = (self.name.value, self.amount.value, self.unit.value)
    self.controller.edit_user_ingredient(editIngredient)
    self.page.go('/ingredientsPage')
