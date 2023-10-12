import random
import flet as ft
import math
from lista_enlazada import ListaEnlazada


def main(page: ft.Page):
    numeros_aleatorios = [random.randint(1, 100) for _ in range(40)]

    lista_pares = ListaEnlazada()
    lista_impares = ListaEnlazada()

    for numero in numeros_aleatorios:
        if numero % 2 == 0:
            lista_pares.agregar_elemento(numero)
        else:
            lista_impares.agregar_elemento(numero)

    columna_par = ft.Column(scroll=ft.ScrollMode.ALWAYS)
    columna_impar = ft.Column(scroll=ft.ScrollMode.ALWAYS)
    pares = lista_pares.get_lista()
    impares = lista_impares.get_lista()
    for i in range(len(pares)):
        if i % 5 == 0:
            columna_par.controls.append(ft.Row())

        columna_par.controls[math.trunc(i/5)].controls.append(ft.Container(ft.Text(pares[i], size=15), width=20, height=20, alignment=ft.alignment.center))

    for i in range(len(impares)):
        if i % 5 == 0:
            columna_impar.controls.append(ft.Row())

        columna_impar.controls[math.trunc(i/5)].controls.append(ft.Container(ft.Text(impares[i], size=15), width=20, height=20, alignment=ft.alignment.center))

    container = ft.Container(ft.Row([
        ft.Column([ft.Text("Números pares", weight="bold", size=25), ft.Container(columna_par, margin=ft.margin.only(bottom=25))]),
        ft.Column([ft.Text("Números impares", weight="bold", size=25), ft.Container(columna_impar, margin=ft.margin.only(bottom=25))])
    ], alignment="center", spacing=20, height=400)
    )

    page.add(
        container
    )

ft.app(main)