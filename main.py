import flet as ft

def main(page: ft.Page):
    page.title = "Мое первое приложение на flet!"
    greeting_text = ft.Text('Hello world')
    name_input = ft.TextField(label="Введите имя: ")

    page.add(greeting_text, name_input)



ft.app(target=main, view=ft.WEB_BROWSER)