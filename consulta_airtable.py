import flet as ft
import nube as nb
import importlib  # Necesario para importar dinámicamente

def main(page: ft.Page):
    def regresar(e: ft.ControlEvent):
        page.clean()
        # Importación dinámica para evitar circularidad
        ma = importlib.import_module("main")
        ma.main(page)  # Llama a la función main de main.py

    # --- Configuración de la página ---
    page.title = "Interacciones Medicamentosas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = True
    page.appbar = ft.AppBar(
        title=ft.Text("Interacciones Medicamentosas - UJAT"),
        leading=ft.Icon(name="SCIENCE", color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        center_title=True,
    )

    # --- Conexión a base de datos ---
    nb.farmacia_ujat.connect()

    # --- Tabla de datos ---
    encabezado = [
        ft.DataColumn(ft.Text("Medicamento", weight="bold")),
        ft.DataColumn(ft.Text("Interacciones", weight="bold"))
    ]

    filas = []
    datos = nb.Receta.select()
    for d in datos:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(d.medicamento)),
                    ft.DataCell(ft.Text(d.interacciones))
                ]
            )
        )

    tabla = ft.DataTable(
        columns=encabezado,
        rows=filas,
        border=ft.border.all(1, ft.colors.GREY_400),
        border_radius=10,
        horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_300),
        vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_300),
    )

    # --- Botón de regreso ---
    btn_regresar = ft.ElevatedButton(
        text="Regresar al Menú Principal",
        icon=ft.icons.ARROW_BACK,
        on_click=regresar,
        style=ft.ButtonStyle(
            padding=20,
            bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE
        )
    )

    # --- Diseño final ---
    page.add(
        ft.Container(
            content=tabla,
            margin=ft.margin.all(20),
            padding=ft.padding.all(10),
        ),
        ft.Row(
            [btn_regresar],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # --- Cerrar conexión ---
    nb.farmacia_ujat.close()

if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        port=8505
    )
