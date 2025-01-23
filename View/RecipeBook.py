import flet as ft

class RecipeBook:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.get_recipe()

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
          on_click=lambda e: self.page.go("/homePage")),
        ],
        alignment=ft.MainAxisAlignment.END
      ),
      padding=ft.Padding(20, 40, 20, 40), 
      bgcolor="#090033"
    )

    title = ft.Text(
      "RECEITAS",
      size=30,
      weight=ft.FontWeight.BOLD,
      color="black",
      text_align=ft.TextAlign.CENTER,)

    recipes =ft.Container(
      content=ft.Row(
        [
          ft.ElevatedButton(
            text = self.recipeName[i],
            on_click= lambda e, recipe=self.recipeName[i]: self.go_to_recipe(recipe),  
            bgcolor="#6668e8",
            color="white",
            width=200,
            height=100,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),)
          ) for i in range(len(self.recipeName))
        ], 
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
        expand=True,
      ),
      padding=ft.Padding(20, 200, 20, 40),
    )

    return ft.Column(controls=[header, title, recipes])

  def get_recipe(self):
    self.recipeName = self.controller.get_recipe()
    return self.recipeName 
  
  def go_to_recipe(self, recipe):
    self.controller.set_recipe_name(recipe)
    self.page.go("/recipePage")
