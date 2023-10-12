import flet as ft
from datetime import datetime
import random
from supermercado import SuperMercado
from producto import Producto
class PageView:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.supermercado = SuperMercado()
        self.msg = ft.Text(size=15, weight="bold")
        self.index = 0
        self.input_delete = ft.TextField(label="Índice del producto a eliminar")
        self.container = ft.Container()
        self.matriz_text = []
        self.input_minus_one = ft.TextField(label="Índice del producto para descontar", text_align="right", width=250)

    def generar_nombre_producto(self, num_producto):
        return f"producto{num_producto}"

    def generar_producto(self, num_producto):
        nombre = self.generar_nombre_producto(num_producto)
        cantidad = random.randint(1, 50)
        precio = round(random.uniform(10.0, 200.0), 2)
        return Producto(nombre, cantidad, precio)

    def home_page(self):
        self.msg.value = ""
        self.input_delete.value = ""
        container = ft.Container(ft.Column([
                    ft.Text("¡Bienvenido al Supermercado Mazorca!", size=35, weight="bold"),
                    ft.Text(f"Día {datetime.now().date().day} del mes {datetime.now().date().month} de {datetime.now().date().year}", size=20)
                ], 
                alignment=ft.MainAxisAlignment.SPACE_AROUND, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            alignment=ft.alignment.top_center
        )

        return container
    
    def handle_add(self, e):
        self.index += 1
        producto = self.generar_producto(self.index)
        self.msg.value = self.supermercado.agregar_producto(producto)
        self.container.content = self.print_available()
        self.page.update()

    def add_product_page(self):
        self.container.content = self.print_available()
        container = ft.Container(
            ft.Column([
                ft.ElevatedButton("Escanear producto", on_click=self.handle_add),
                self.msg,
                self.container
            ])
        )

        return container
    
    def print_available(self):
        matriz = self.supermercado.mostrar_productos_disponibles()
        if matriz:
            columna = ft.Column(spacing=7, scroll=ft.ScrollMode.ALWAYS, height=500, width=500)
            for i in range(len(matriz)):
                columna.controls.append(ft.Text(f"{i+1}.- {matriz[i]}", size=15))
            return columna
        else: return ft.Text("No hay productos que mostrar", size=35, weight="bold")

    def available_product_page(self):
        container = ft.Container(
                self.print_available()
        )

        return container
    
    def print_recalled(self):
        matriz = self.supermercado.mostrar_productos_retirados()
        if matriz:
            columna = ft.Column(spacing=7, scroll=ft.ScrollMode.ALWAYS, height=500, width=500)
            for product in matriz:
                columna.controls.append(ft.Text(product, size=15))
            return columna
        else: return ft.Text("No hay productos que mostrar", size=35, weight="bold")

    def recalled_product_page(self):
        container = ft.Container(
            self.print_recalled()
        )

        return container
    
    def print_count(self):
        matriz = self.supermercado.mostrar_productos_disponibles()
        self.matriz_text = []
        if matriz:
            columna = ft.Column(spacing=7, scroll=ft.ScrollMode.ALWAYS, height=500, width=500)
            for i in range(len(matriz)):
                self.matriz_text.append(ft.Text(f"{i+1}.- {matriz[i]}", size=15))
                columna.controls.append(ft.Row([
                    self.matriz_text[i],
                ]))
            return columna
        else: return ft.Text("No hay productos que mostrar", size=35, weight="bold")
    
    def handle_delete(self, e):
        cadena = self.input_delete.value
        if cadena.isdigit():
            self.msg.value = self.supermercado.retirar_producto(int(cadena)-1)
            self.container.content = self.print_count()
        else:
            self.msg.value = "Ingresa solo números enteros"
        self.page.update()

    def handle_minus_one(self, e):
        indice = self.input_minus_one.value
        if indice.isdigit():
            self.supermercado.retirar_uno(int(indice)-1)
            self.container.content = self.print_count()
        else:
            self.msg.value = "Ingresa solo números enteros"
        self.page.update()
    
    def delete_product_page(self):
        self.container.content = self.print_count()
        container = ft.Container(
            ft.Column([
                self.input_delete,
                ft.ElevatedButton("Eliminar", on_click=self.handle_delete),
                ft.Row([
                    ft.Container(ft.IconButton(ft.icons.REMOVE, on_click=self.handle_minus_one), border=ft.border.all(4,"white"), margin=ft.margin.only(10)), self.input_minus_one
                ]),
                self.msg,
                self.container
            ])
        )

        return container