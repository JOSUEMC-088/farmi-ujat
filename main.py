import flet as ft


def main(page: ft.Page):
    page.title = "Farmi-UJAT"
    page.theme_mode = ft.colors.WHITE
    page.theme_mode = ft
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT",size=30),
        center_title=True,
        
    )

    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication", color="green", size=60),
                    ft.Text("Interacciones Medicamentosas", color="black", text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            padding=10,
            alignment=ft.alignment.center,
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor="orange100",
        width=200,
        height=150
    )



    btn_nuevo_medicamento = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("LOCAL_HOSPITAL_OUTLINED", color="Purple", size=60),
                    ft.Text("Alta Medicamento", color="black", text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            padding=10,
            alignment=ft.alignment.center,
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "green")
        ),
        bgcolor="green100",
        width=200,
        height=150
    )

    btn_lista_medicamento= ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("LIST_ALT", color="brown", size=60,),
                    ft.Text("Lista Medicamento", color="black", text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            padding=10,
            alignment=ft.alignment.center,
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "blue")
        ),
        bgcolor="blue100",
        width=200,
        height=150
    )



    page.add(ft.Divider(color=ft.colors.BLACK))


    page.add(
        ft.Row(
            controls=[
                btn_interacciones,
                btn_nuevo_medicamento,
                btn_lista_medicamento
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centra los botones horizontalmente
        )
    )
    
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)