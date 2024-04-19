import flet as ft


def main(page: ft.Page):
    page.title = "Teilhaber"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Soliparty feministischer Streik"),
                            subtitle=ft.Text(
                                "KAFF Kulturlokal, Frauenfeld"
                            ),
                        ),
                        ft.Row(
                            [
                                ft.TextButton("Participate"), 
                                ft.TextButton("Recommend"),
                                ft.TextButton("Next")
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=600,
                padding=10,
            )
        )
    )



ft.app(main)
