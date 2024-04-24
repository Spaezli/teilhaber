import flet as ft

from views.participation import ParticipationView
from views.discover import DiscoverView

PROJECT_INFO_URL = "https://bd.hack4socialgood.ch/project/89"
PARTICIPATION_FORM_URL = "https://baserow.io/form/8ab5fi-zc5jGh6mzVbhXyg9-_RzDbRylWk6tUK6OVWs"

def main(page: ft.Page):
    page.title = "Teilhaber"
    page.window_width = 480
    page.window_height = 720
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    participationView = ParticipationView(page)

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Discover"), bgcolor=ft.colors.AMBER_200),
                        DiscoverView(page, participationView),
                        page.navigation_bar,
                    ],
                )
            )
        elif page.route == "/participate":
            page.views.append(
                ft.View(
                    "/participate",
                    [
                        ft.AppBar(title=ft.Text("Participate"), bgcolor=ft.colors.CYAN_ACCENT_400),
                        participationView,
                        ft.ElevatedButton("Evaluate Participation", on_click=lambda _: page.launch_url(
                            PARTICIPATION_FORM_URL, web_window_name='baserow'
                        )),
                        page.navigation_bar,
                    ],
                )
            )
        elif page.route == "/about":
            page.views.append(
                ft.View(
                    "/about",
                    [
                        ft.AppBar(title=ft.Text("About"), bgcolor=ft.colors.GREEN_ACCENT_400),
                        ft.Text("This project was developed at Hack4SocialGood 2024"),
                        ft.ElevatedButton("Read more", on_click=lambda _: page.launch_url(
                            PROJECT_INFO_URL, web_window_name='_blank'
                        )),
                        ft.Image(
                            src=f"./teilhaber/assets/IMG_20240419_19491901.jpg",
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        page.navigation_bar,
                    ],
                )
            )
        elif page.route == "/evaluate":
            page.views.append(
                ft.View(
                    "/evaluate",
                    [
                        ft.AppBar(title=ft.Text("Evaluate"), bgcolor=ft.colors.GREEN_ACCENT_400),
                        ft.Text("(In the future, the form can be embedded here)"),
                        ft.WebView(
                            PARTICIPATION_FORM_URL,
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
            page.go("/about")

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Discover"),
                ft.NavigationDestination(icon=ft.icons.CAMPAIGN, label="Participate"),
                ft.NavigationDestination(icon=ft.icons.BOOKMARK, label="About"),
            ],
            on_change=nav_change
        )
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
