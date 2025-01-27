import flet as ft

class IngredientsPage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.get_user_ingredients()
 
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
          on_click=lambda e: self.page.go("/userPage")),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
      ),
      padding=ft.Padding(20, 40, 20, 40),
      bgcolor="#090033",
    )

    ingredientsTitle = ft.Text("MEUS INGREDIENTES", size=20, weight="bold", color="black")
    ingredientsList = ft.Column(
      controls=[
        ft.Row(
          controls=[
            ft.Text(f"{ingredient['nome']}  {ingredient['quantidade']} {ingredient['unidade']}", size=16, color="black"),
            ft.ElevatedButton(
              "EDITAR",
              style=ft.ButtonStyle(
              bgcolor="orange",
              color="black",
              shape=ft.RoundedRectangleBorder(radius=10),
              padding=ft.Padding(30, 15, 30, 15)),
              on_click=lambda e, editIngredient=self.ingredients[i]: self.set_user_ingredient_id(editIngredient), 
            ),
            ft.ElevatedButton(
              "EXCLUIR",
              style=ft.ButtonStyle(
              bgcolor="red",
              color="white",
              shape=ft.RoundedRectangleBorder(radius=10),
              padding=ft.Padding(30, 15, 30, 15)),
              on_click=lambda e, deleteIngredient=self.ingredients[i]: self.delete_user_ingredient(deleteIngredient), 
            ),
          ],
          alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
          
        )
        for i, ingredient in enumerate(self.ingredients)
      ],
      spacing=10,
    )
    addButton = ft.ElevatedButton(
      "ADICIONAR NOVO INGREDIENTE",
      width=200,
      style=ft.ButtonStyle(
      bgcolor="#6691e8",
      color="white",
      shape=ft.RoundedRectangleBorder(radius=10),
      padding=ft.Padding(30, 15, 30, 15)),
      on_click=lambda e: self.page.go("/ingredientRegister"),
    )

    return ft.Column([header, ingredientsTitle, ingredientsList, addButton ])
  
  def get_user_ingredients(self):
    self.ingredients = self.controller.get_user_ingredients()

  def set_user_ingredient_id(self, editIngredient):
    self.controller.set_user_ingredient_id(editIngredient)
    self.page.go("/editIngredients")

  def delete_user_ingredient(self, deleteIngredient):
    self.controller.set_user_ingredient_id(deleteIngredient)
    self.controller.delete_user_ingredient()
