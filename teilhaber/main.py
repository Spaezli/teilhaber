import flet as ft

from views.participation import ParticipationView
from remote import get_data


def main(page: ft.Page):
    page.title = "Teilhaber"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Discover"), bgcolor=ft.colors.AMBER_200),
                    ft.ElevatedButton("Select", on_click=lambda _: page.go("/participate")),
                    page.navigation_bar,
                ],
            )
        )
        if page.route == "/participate":
            page.views.append(
                ft.View(
                    "/participate",
                    [
                        ft.AppBar(title=ft.Text("Participate"), bgcolor=ft.colors.CYAN_ACCENT_400),
                        ParticipationView(),
                        ft.ElevatedButton("Evaluate", on_click=lambda _: page.go("/evaluate")),
                        page.navigation_bar,
                    ],
                )
            )
        if page.route == "/evaluate":
            page.views.append(
                ft.View(
                    "/evaluate",
                    [
                        ft.AppBar(title=ft.Text("Evaluate"), bgcolor=ft.colors.GREEN_ACCENT_400),
                        ft.WebView(
                            "https://baserow.io/form/8ab5fi-zc5jGh6mzVbhXyg9-_RzDbRylWk6tUK6OVWs",
                            expand=True,
                            on_web_resource_error=lambda e: print("Page error:", e.data),
                        ),
                        page.navigation_bar,
                    ],
                )
            )
        page.update()

    def nav_change(e):
        goto = int(e.data)
        if goto == 0:
            page.go("/")
        if goto == 1:
            page.go("/participate")
        if goto == 2:
            page.go("/evaluate")

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Discover"),
                ft.NavigationDestination(icon=ft.icons.CAMPAIGN, label="Participate"),
                ft.NavigationDestination(icon=ft.icons.BOOKMARK, label="Evaluate"),
            ],
            on_change=nav_change
        )
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)