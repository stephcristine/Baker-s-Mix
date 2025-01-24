import flet as ft

class CakePanRegister:
  def __init__(self, page, controller):
    self.page = page
    self.controller = controller

  def page_content(self):
    title = ft.Text(
      "CADASTRO DE FORMAS",
      size=30,
      weight=ft.FontWeight.BOLD,
      color="white",
      text_align=ft.TextAlign.CENTER,
    )
    self.type = ft.Dropdown(
      label="Selecione o tipo da forma",
      bgcolor="#ffffff",
      options=[
        ft.dropdown.Option("circular"),
        ft.dropdown.Option("retangular"),
      ],
      on_change=self.show_fields
    )
    self.diameter = ft.TextField(
      label="Diâmetro da forma (cm)",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      visible=False,
      bgcolor="white",
      border_radius=5,
    )
    self.height = ft.TextField(
      label="Altura da forma (cm)",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      visible=False,
      bgcolor="white",
      border_radius=5,
    )

    self.length = ft.TextField(
      label="Comprimento da forma (cm)",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      visible=False,
      bgcolor="white",
      border_radius=5,
    )
    self.width = ft.TextField(
      label="Largura da forma (cm)",
      label_style=ft.TextStyle(size=16, color="black"),
      filled=True,
      visible=False,
      bgcolor="white",
      border_radius=5,
    )

    self.registerButton = ft.ElevatedButton(
      text="CADASTRAR",
      style=ft.ButtonStyle(
        bgcolor="#6691e8",
        color="white",
        shape=ft.RoundedRectangleBorder(radius=30),
        padding=ft.Padding(15, 15, 15, 15),
      ),
      on_click=lambda e: self.cake_pan_register(),
      visible=False
    )

    container = ft.Container(
      content=ft.Column(
        [
          title,
          self.type,
          self.diameter,
          self.height,
          self.length,
          self.width,
          self.registerButton,
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      ),
      width=400,
      height=400,
      bgcolor="#85d4ff",
      border_radius=20,
      alignment=ft.alignment.center,
      padding=20,
    )

    return ft.Column(controls=[container])

  def show_fields(self, e):
    selected_type = self.type.value
        
    if selected_type == "circular":
      self.diameter.visible = True
      self.height.visible = True
      self.length.visible = False
      self.width.visible = False
    elif selected_type == "retangular":
      self.diameter.visible = False
      self.height.visible = True
      self.length.visible = True
      self.width.visible = True
    else:
      self.diameter.visible = False
      self.height.visible = False
      self.length.visible = False
      self.width.visible = False

    self.registerButton.visible = True if selected_type else False

    self.page.update()

  def cake_pan_register(self):
    panData = (self.type.value, self.diameter.value, self.height.value, self.length.value, self.width.value)
    print(panData)
