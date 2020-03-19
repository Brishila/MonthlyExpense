import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook


class ExcelReport:
    def __init__(self, filename):
        self.filename = filename

    def create_report(self):
        workbook = self.filename

        df = pd.read_excel(workbook, sheet_name="Expense")

        typegroup = df.groupby(["Type"])
        df_expense = typegroup["Amount"].sum()
        df_reportdata = df.groupby(["Date", "Type"])["Amount"].sum()
        df_reportdata["Total"] = df_reportdata.sum()
        df_expense.plot.pie(
            y=df_expense.index,
            shadow=False,
            startangle=90,
            autopct="%1.1f%%",
            figsize=(3, 3),
        )
        plt.axis("equal")
        plt.tight_layout()
        plt.savefig("projection.png")
        my_png = openpyxl.drawing.image.Image("projection.png")

        with pd.ExcelWriter(workbook, engine="openpyxl", mode="a") as writer:
            wb = writer.book
            writer.sheets = dict((ws.title, ws) for ws in wb.worksheets)
            df_reportdata.to_excel(writer, "Projection")
            ws = wb["Projection"]
            ws.add_image(my_png, "N3")
            wb.save(workbook)

