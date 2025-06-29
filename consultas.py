import flet as ft
import modelo as md
import importlib

def main(page: ft.Page):

    def regresar(e: ft.ControlEvent):
        page.clean()
        ma = importlib.import_module("main")
        ma.main(page)

    page.title = "Consultas"
    page.window.width = 800
    page.window.height = 600
    page.theme_mode = "light"
    page.scroll = True

    page.appbar = ft.AppBar(
        title=ft.Text("Listado de medicamentos UJAT"),
        leading=ft.Icon("receipt_long"),
        bgcolor="blue",
        center_title=True,
    )

    btn_regresar = ft.ElevatedButton(text="Regresar", icon="arrow_back", on_click=regresar)

    encabezado = [
        ft.DataColumn(ft.Text("Descripción", width=200)),
        ft.DataColumn(ft.Text("Presentación", width=200)),
        ft.DataColumn(ft.Text("Clasificación", width=200)),
        ft.DataColumn(ft.Text("Nivel de atencion", width=100)),
        ft.DataColumn(ft.Text("Sustancia activa", width=200))
    ]

    filas = []
    medicinas = md.Medicamento.select()
    for med in medicinas:
        fila = ft.DataRow([
            ft.DataCell(ft.Text(med.descripcion, weight="bold")),
            ft.DataCell(ft.Text(med.presentacion)),
            ft.DataCell(ft.Text(med.clasificacion, italic=True)),
            ft.DataCell(ft.Text(med.nivel_atencion)),
            ft.DataCell(ft.Text(med.descripcion, color="pink"))  # ¿Querías med.sustancia_activa?
        ])
        filas.append(fila)

    tbl_medicamentos = ft.DataTable(columns=encabezado, rows=filas)

    page.add(btn_regresar, tbl_medicamentos)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
