import flet as ft



def getEvents():
    dataRows = []
    dataRows.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                )
    )
    
    return dataRows


def DiscoverView(page: ft.Page, participationView):

    def goParticipate(e):
        #searchfield_control = page.views[0].controls[1].controls[0]
        page.session.set("query", tb1.value)
        page.go("/participate")


    img = ft.Image(
        src=f"./assets/teilhaber_logo.png",
        width=536,
        height=422,
        fit=ft.ImageFit.CONTAIN,
    )
    data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Title")),
                ft.DataColumn(ft.Text("Subtitle")),
                ft.DataColumn(ft.Text("Link"), numeric=True),
            ],
            rows=getEvents()
        )
    tb1 = ft.TextField(
        label="Search for Events",
        value=""
    )

    return ft.Column([
        img,
        tb1,
        ft.ElevatedButton("Select", on_click=goParticipate)
    ])

#def DiscoverView():
#    header_text = ft.Text("This is a header text above the table.", style=ft.TextStyle(size=16))
#
#    # Create the DataTable widget
#    data_table = ft.DataTable(
#        columns=[
#            ft.DataColumn(ft.Text("First name")),
#            ft.DataColumn(ft.Text("Last name")),
#            ft.DataColumn(ft.Text("Age"), numeric=True),
#        ],
#        rows=getEvents()
#    )
#
#    # Use Column to stack the Text and DataTable vertically
#    layout = ft.Column(children=[header_text, data_table])
#
#    return layout