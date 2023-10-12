import flet as ft
from page_view import PageView

def main(page: ft.Page):

    def route_change(e):
        inicio_boton = ft.ElevatedButton(text="Regresar al inicio", on_click=lambda _: page.go("/"))
        navegacion_botones = ft.Container(
            ft.Row([
                ft.ElevatedButton(text="Agregar productos", on_click=lambda _: page.go("/add")),
                ft.ElevatedButton(text="Retirar un producto", on_click=lambda _: page.go("/delete")),
                ft.ElevatedButton(text="Productos disponibles", on_click=lambda _: page.go("/products/available")),
                ft.ElevatedButton(text="Productos retirados", on_click=lambda _: page.go("/products/recalled"))
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            alignment=ft.alignment.top_left,
            )
        
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Supermercado"),
                            center_title=False,
                            bgcolor=ft.colors.INDIGO_800,
                        ),
                        page_view.home_page(),
                        navegacion_botones
                    ],
                )
            )
        if page.route == "/add":
            page.views.append(
                ft.View(
                    "/add",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Supermercado"),
                            center_title=False,
                            bgcolor=ft.colors.INDIGO_800,
                        ),
                        inicio_boton,
                        page_view.add_product_page(),
                    ],
                )
            )
        if page.route == "/delete":
            page.views.append(
                ft.View(
                    "/delete",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Supermercado"),
                            center_title=False,
                            bgcolor=ft.colors.INDIGO_800,
                        ),
                        inicio_boton,
                        page_view.delete_product_page(),
                    ],
                )
            )
        if page.route == "/products/available":
            page.views.append(
                ft.View(
                    "/products/available",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Supermercado"),
                            center_title=False,
                            bgcolor=ft.colors.INDIGO_800,
                        ),
                        inicio_boton,
                        page_view.available_product_page(),
                    ],
                )
            )
        if page.route == "/products/recalled":
            page.views.append(
                ft.View(
                    "/products/recalled",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Supermercado"),
                            center_title=False,
                            bgcolor=ft.colors.INDIGO_800,
                        ),
                        inicio_boton,
                        page_view.recalled_product_page()
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page_view = PageView(page)
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)