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


def DiscoverView():

    data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Title")),
                ft.DataColumn(ft.Text("Subtitle")),
                ft.DataColumn(ft.Text("Link"), numeric=True),
            ],
            rows=getEvents()
        )
    tb1 = ft.TextField(label="Search for Events")


    return data_table

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