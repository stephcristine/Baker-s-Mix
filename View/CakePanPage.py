import flet as ft

class CakePanPage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.page_setup()
    self.page_content()

  def page_setup(self):
    self.page.title = "Meus Ingredientes e Formas"
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
          on_click=lambda e: self.page.go("/userPage")),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
      ),
      padding=ft.Padding(20, 40, 20, 40),
      bgcolor="#090033",
    )

    cakePanTitle = ft.Text("MINHAS FORMAS", size=20, weight="bold", color="black")
    cakePanList = ft.Column(
      controls=[
        ft.Row(
          controls=[
            ft.Text("formato + tamanho", size=16, color="black"),
            ft.ElevatedButton(
              "EDITAR",
              style=ft.ButtonStyle(
              bgcolor="orange",
              color="black",
              shape=ft.RoundedRectangleBorder(radius=10),
              padding=ft.Padding(30, 15, 30, 15)),
              on_click=lambda e: print("Editar Ingrediente!"),
            ),
            ft.ElevatedButton(
              "EXCLUIR",
              style=ft.ButtonStyle(
              bgcolor="red",
              color="white",
              shape=ft.RoundedRectangleBorder(radius=10),
              padding=ft.Padding(30, 15, 30, 15)),
              on_click=lambda e: print("Excluir Ingrediente!"),
            ),
          ],
          alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        for _ in range(3)
      ],
      spacing=10,
    )
    addButton = ft.ElevatedButton(
      "ADICIONAR NOVA FORMA",
      style=ft.ButtonStyle(
      bgcolor="#6691e8",
      color="white",
      shape=ft.RoundedRectangleBorder(radius=10),
      padding=ft.Padding(30, 15, 30, 15)),
      on_click=lambda e: print("Adicionar Ingrediente!"),
    )

    return ft.Column([header, cakePanTitle, cakePanList, addButton ])
