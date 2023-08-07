from openpyxl import Workbook
from openpyxl import load_workbook

def tag_generator(title:str, art1:str, art2:str):
    workbook = load_workbook(filename="D:\Dropbox\Youtube Uploads\Tag Generator.xlsx")
    first_sheet = workbook["808 Mafia"]

    first_sheet["J3"].value = title
    first_sheet["D3"].value = art1
    first_sheet["G3"].value = art2

    workbook.save(filename="D:\Dropbox\Youtube Uploads\Tag Generator.xlsx")
    return
