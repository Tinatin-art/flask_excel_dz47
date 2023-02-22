from flask import Flask, render_template
from openpyxl import load_workbook

app = Flask(__name__)

@app.route('/')
def download():
    book = load_workbook("excel.xlsx")
    sheet = book.active

    return render_template("index.html", sheet=sheet)