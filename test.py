from flet import *
import flet as ft

def main(page: ft.Page):

    appbar = AppBar(
        title=Text("TESTE APP WEB FLET", size=30, color="white"),
        bgcolor="blue"
        )
    
    content_1 = Container(
        content= Column([
            Text("Hello From Flet", size=40)
        ])
    )

    page.add(appbar, content_1)

ft.app(target=main)