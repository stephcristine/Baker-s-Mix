import flet as ft

class CakePanPage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.get_user_cake_pan()

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
            ft.Text(f"{pan['tipo']}  {pan['diametro']} X {pan['altura']}", size=16, color="black"),
            ft.ElevatedButton(
              "EDITAR",
              style=ft.ButtonStyle(
              bgcolor="orange",
              color="black",
              shape=ft.RoundedRectangleBorder(radius=10),
              padding=ft.Padding(30, 15, 30, 15)),
              on_click=lambda e, editCakePan=self.panList[i]: self.set_user_cake_pan_id(editCakePan),
            ),
            ft.ElevatedButton(
              "EXCLUIR",
              style=ft.ButtonStyle(
              bgcolor="red",
              color="white",
              shape=ft.RoundedRectangleBorder(radius=10),
              padding=ft.Padding(30, 15, 30, 15)),
              on_click=lambda e, deleteCakePan=self.panList[i]: self.delete_user_cake_pan(deleteCakePan), 
            ),
          ],
          alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        for i, pan in enumerate(self.panList)
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
      on_click=lambda e: self.page.go("/cakePanRegister"),
    )

    return ft.Column([header, cakePanTitle, cakePanList, addButton ])
  
  def get_user_cake_pan(self):
    self.panList =self.controller.get_user_cake_pan()

  def set_user_cake_pan_id(self, editCakePan):
    self.controller.set_user_cake_pan_id(editCakePan)
    self.page.go("/editCakePan")

  def delete_user_cake_pan(self, deleteCakePan):
    self.controller.set_user_cake_pan_id(deleteCakePan)
    self.controller.delete_user_cake_pan()
