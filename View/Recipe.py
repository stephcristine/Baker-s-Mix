import flet as ft

class RecipePage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.get_recipe_name()
    self.get_recipe_ingredients()
    self.get_cake_pan()
    self.page_setup()
    self.page_content()

  def page_setup(self):
    self.page.title = "Receitas"
    self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
    self.page.vertical_alignment = ft.MainAxisAlignment.START  
    self.page.scroll = "auto"
    self.page.bgcolor = "white" 
  
  def page_content(self):
    header = ft.Container(
      content=ft.Row(
        [
          ft.ElevatedButton(
          "VOLTAR", 
          width=120,
          style=ft.ButtonStyle(
          bgcolor="#3c3feb", 
          color="white",
          shape=ft.RoundedRectangleBorder(radius=10),
          padding=ft.Padding(30, 15, 30, 15),),
          on_click=lambda e: self.page.go("/recipeBook")),
        ],
        alignment=ft.MainAxisAlignment.END
      ),
      padding=ft.Padding(20, 40, 20, 40), 
      bgcolor="#090033"
    )

    title = ft.Text(self.recipeName, size=30, weight="bold", color="black", text_align="center")

    ingredients = ft.Column(
      controls=[ft.Row(
        controls=
        [
          ft.Checkbox(),
          ft.Text(f"{i['quantidade']} {i['unidade']} de {i['nome']}", size=18, color="black"),
        ]
        )
        for i in self.ingredients 
      ],
        spacing=10,
    )

    dropdown = ft.Dropdown(
      width=200,
      options=
      [
        ft.dropdown.Option(pan['tipo']) for pan in self.panType
      ] 
    )

    body = ft.Container(
      content=ft.Column(
        controls=[
          ft.Text("Ingredientes:", size=22, weight="bold", color="black"),
          ingredients,
          ft.Text("Escolha uma forma:", size=22, weight="bold", color="black"),
          dropdown,
        ],
          spacing=20,
        ),
        padding=20,
    )

    return ft.Column(controls=[header, title, body])

  def get_recipe_name(self):
    self.recipeName = self.controller.get_recipe_name()

  def get_recipe_ingredients(self):
    self.ingredients = self.controller.get_recipe_ingredients()

  def get_cake_pan(self):
    self.panType = self.controller.get_cake_pan()
