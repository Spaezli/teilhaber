import flet as ft

def ParticipationView(search_data=[]):

    def event_swipe(e: ft.DragUpdateEvent):
        ref = e.control.content.content.controls[0].value
        #print(ref)

    st = ft.Stack()
    for sd in search_data:
        if not sd['Title']: continue
        #print(sd)
        st.controls.append(
            ft.GestureDetector(
                on_pan_update=event_swipe,
                content=ft.Container(
                    width=500, 
                    height=500,
                    padding=10,
                    bgcolor="blue200",
                    content=ft.Column([
                        ft.Text(sd['Title'], size=25, weight="bold"),
                        ft.Text(sd['Subtitle'], size=15),
                        ft.Text(sd['Date'], size=10,),
                    ])
                )
            )
        )

    return st

def OldView():
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
