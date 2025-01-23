import flet as ft

class UserPage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller

  def page_content(self):
    header = ft.Container(
        content=ft.Row(
            [
            ft.ElevatedButton(
            "Ingredientes", 
            style=ft.ButtonStyle(
            bgcolor="#3c3feb",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(30, 15, 30, 15),),
            on_click=lambda e: self.page.go("/ingredientsPage")),

            ft.ElevatedButton(
            "Formas", 
            style=ft.ButtonStyle(
            bgcolor="#3c3feb",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(30, 15, 30, 15),),
            on_click=lambda e: self.page.go("/cakePanPage")),

            ft.ElevatedButton(
            "Voltar", 
            style=ft.ButtonStyle(
            bgcolor="#3c3feb",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(30, 15, 30, 15),),
            on_click=lambda e: self.page.go("/homePage"))
            ],
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN, 
            expand=True,  
        ),
        bgcolor="#090033",  
        padding=ft.Padding(20, 40, 20, 40), 
      )
      
    title = ft.Text(
          "DADOS DO USUÁRIO",
          size=30,
          weight=ft.FontWeight.BOLD,
          color="white",
          text_align=ft.TextAlign.CENTER,
      )
    name = ft.TextField(
        label="Nome",
        label_style=ft.TextStyle(size=16, color="black"),
        filled=True,
        bgcolor="white",
        border_radius=20,
    )
    email = ft.TextField(
        label="E-mail",
        label_style=ft.TextStyle(size=16, color="black"),
        filled=True,
        bgcolor="white",
        border_radius=20,
    )
    editButton = ft.ElevatedButton(
        text="EDITAR",
        style=ft.ButtonStyle(
            bgcolor="#f1a20b",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(20, 20, 20, 20),
        ),
        on_click=lambda e: print("Cadastro realizado!"),
    )
    deleteButton = ft.ElevatedButton(
        text="DELETAR",
        style=ft.ButtonStyle(
            bgcolor="#de1111",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(20, 20, 20, 20),
        ),
        on_click=lambda e: print("Cadastro realizado!"),
    )

    body = ft.Container(
        content=ft.Column(
            [
                title,
                name,
                email,
                editButton,
                deleteButton
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=500,
        height=350,
        bgcolor="#8e66e8",
        border_radius=20,
        alignment=ft.alignment.center,
        padding=20,
    )

    return ft.Column(controls=[header, body])
  