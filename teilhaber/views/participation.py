import flet as ft

C_WIDTH = 500
C_HEIGHT = 500

C_LEFT_FROM = - C_WIDTH / 2
C_LEFT_TO = C_LEFT_FROM - (C_WIDTH / 4)
C_RIGHT_FROM = C_WIDTH / 2
C_RIGHT_TO = C_RIGHT_FROM + (C_WIDTH / 4)

def ParticipationView(page: ft.Page, search_data=[]):

    def event_swipe(e: ft.DragUpdateEvent):
        ref = e.control.content.content.controls[0].value
        e.control.left = max(C_LEFT_TO, min(C_RIGHT_TO, e.control.left + e.delta_x))
        if C_LEFT_TO <= e.control.left <= C_LEFT_FROM:
            e.control.content.bgcolor = "red"
            if e.control.left == C_LEFT_TO:
                st.controls.remove(e.control)
                print(ref)
        elif C_RIGHT_FROM <= e.control.left <= C_RIGHT_TO:
            e.control.content.bgcolor = "green200"
            if e.control.left == C_RIGHT_TO:
                st.controls.remove(e.control)
                print(ref)
        else:
            e.control.content.bgcolor = "blue200"
        page.update()

    st = ft.Stack()
    for sd in search_data:
        if not sd['Title']: continue
        #print(sd)
        st.controls.append(
            ft.GestureDetector(
                on_pan_update=event_swipe,
                top=10,
                left=10,
                right=10,
                content=ft.Container(
                    width=C_WIDTH, 
                    height=C_HEIGHT,
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

    return ft.Container(
            width=C_WIDTH + 20, 
            height=C_HEIGHT + 20,
            content=st
        )

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
