import flet as ft

class RecipePage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.get_recipe_name()
    self.get_recipe_ingredients()
    self.get_user_cake_pan()
    self.page_setup()

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
              padding=ft.Padding(30, 15, 30, 15),
            ),
            on_click=lambda e: self.page.go("/recipeBook")
          ),
        ],
        alignment=ft.MainAxisAlignment.END
      ),
      padding=ft.Padding(20, 40, 20, 40), 
      bgcolor="#090033"
    )

    title = ft.Text(self.recipeName['nome'], size=30, weight="bold", color="black", text_align="center")

    self.message = ft.Text(
      value="",
      size=16,
      color="red",
      weight="bold"
    )

    ingredients = ft.Column(
      controls=[
        ft.Row(
          controls=[
            ft.Checkbox(),
            ft.Text(f"{i['quantidade']} {i['unidade']} de {i['nome']}", size=18, color="black"),
          ]
        )
        for i in self.ingredients
      ],
      spacing=10,
    )

    dropdown_row = ft.Row(
      controls=[
        ft.Dropdown(
          width=200,
          options=[
            ft.dropdown.Option(f"{pan['tipo']} {pan['diametro']} X {pan['altura']}") 
            for pan in self.panType
          ]
        ),
        ft.ElevatedButton(
          "Modificar unidade para xícaras",
          style=ft.ButtonStyle(
            bgcolor="#6691e8",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(20, 10, 20, 10),
          ),
          on_click=lambda e: self.modify_to_cups()
        ),
        ft.ElevatedButton(
          "Receita finalizada",
          style=ft.ButtonStyle(
            bgcolor="#32CD32",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(20, 10, 20, 10),
          ),
          on_click=lambda e: self.finish_recipe()
        ),
      ],
      spacing=10,
    )

    body = ft.Container(
      content=ft.Column(
        controls=[
          ft.Text("Ingredientes:", size=22, weight="bold", color="black"),
          ingredients,
          self.message,
          ft.Text("Escolha uma forma:", size=22, weight="bold", color="black"),
          dropdown_row,
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

  def get_user_cake_pan(self):
    self.panType = self.controller.get_user_cake_pan()

  def modify_to_cups(self):
    self.message.value = "Unidades modificadas para xícaras!"
    self.controller.compare_recipe_with_conversion()
    self.page.update()

  def finish_recipe(self):
    self.message.value = "Receita finalizada com sucesso!"
    self.page.update()
