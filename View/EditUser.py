import flet as ft

class EditUser:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller
    self.get_user()

  def page_content(self):
    title = ft.Text(
      "EDITAR USUÁRIO",
      size=30,
      weight=ft.FontWeight.BOLD,
      color="white",
      text_align=ft.TextAlign.CENTER,
    )
    self.name = ft.TextField(
      label= self.user['nome'],
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
    )
    self.email = ft.TextField(
      label= self.user['email'],
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
    )
    self.password = ft.TextField(
      label= self.user['senha'],
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
      password=True,
    )
    registerButton = ft.ElevatedButton(
      text="EDITAR",
      style=ft.ButtonStyle(
        bgcolor="#4A5CFF",
        color="white",
        shape=ft.RoundedRectangleBorder(radius=30),
        padding=ft.Padding(15, 15, 15, 15),
      ),
      on_click=lambda e: self.edit_user(),
    )

    container = ft.Container(
      content=ft.Column(
        [
          title,
          self.name,
          self.email,
          self.password,
          registerButton,
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      ),
      width=400,
      height=400,
      bgcolor="#C2C9FF",
      border_radius=20,
      alignment=ft.alignment.center,
      padding=20,
    )

    return ft.Column(controls=[container])
  
  def get_user(self):
    self.user = self.controller.get_user()

  def edit_user(self):
    newData = (self.name.value, self.email.value, self.password.value)
    self.controller.edit_user(newData)
    self.page.go("/userPage")
