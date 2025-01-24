import flet as ft

class SignupPage:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller

  def page_content(self):
    title = ft.Text(
      "CADASTRO",
      size=30,
      weight=ft.FontWeight.BOLD,
      color="white",
      text_align=ft.TextAlign.CENTER,
    )
    self.name = ft.TextField(
      label="Nome",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
    )
    self.email = ft.TextField(
      label="E-mail",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
    )
    self.password = ft.TextField(
      label="Senha",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      bgcolor="white",
      border_radius=20,
      password=True,
    )
    registerButton = ft.ElevatedButton(
      text="CADASTRAR",
      style=ft.ButtonStyle(
        bgcolor="#4A5CFF",
        color="white",
        shape=ft.RoundedRectangleBorder(radius=30),
        padding=ft.Padding(15, 15, 15, 15),
      ),
      on_click=lambda e: self.user_Register(),
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

  def user_Register(self):
    userData = (self.name.value, self.email.value, self.password.value)
    self.controller.user_Register(userData)
