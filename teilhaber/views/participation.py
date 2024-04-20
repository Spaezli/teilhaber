import flet as ft


def ParticipationView():
    return ft.Card(
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
