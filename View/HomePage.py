import flet as ft

class HomePage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller

  def page_content(self):
    header = ft.Container(
      content=ft.Row(
        [
          ft.Text(
            "Baker's Mix",
            size=20,
            weight=ft.FontWeight.BOLD,
            color="white", 
          ),
          ft.ElevatedButton(
            "USUÁRIO", 
            bgcolor="#3c3feb", 
            color="white", 
            width=120, 
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),), 
            on_click=lambda e: self.page.go("/userPage")),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
        expand=True,  
      ),
      bgcolor="#090033",  
      padding=ft.Padding(20, 40, 20, 40),      
    )

    body = ft.Container(
      content=ft.Row(
        [
          ft.ElevatedButton(
            text="Receitas",
            on_click=lambda e: self.page.go("/recipeBook"),
            bgcolor="#8e66e8",
            color="white",
            width=200,
            height=100,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),)
          ),
          ft.ElevatedButton(
            text="Calculadora",
            on_click=lambda e: print("calculadora"),
            bgcolor="#8e66e8",
            color="white",
            width=200,
            height=100,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),)
          ),   
        ],
          alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
          expand=True,  
        ),   
          padding=ft.Padding(20, 200, 20, 40),
    )

    return ft.Column(controls=[header, body])
