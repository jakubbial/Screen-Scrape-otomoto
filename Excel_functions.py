from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def create_workbook():
    wb = Workbook()
    return wb


def add_header(workbook):
    header = ["Marka", "Cena", "Rocznik", "Przebieg", "Pojemność", "Silnik"]
    alphabet = ["A", "B", "C", "D", "E", "F", "G"]

    sheet1 = workbook.active
    sheet1.title = "Cars"

    for i in range(0, len(header)):
        sheet1[alphabet[i]+"1"] = header[i]


def save_file(workbook, filename):
    workbook.save(filename=filename)


def insert_list(workbook, list, row_nr):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    sheet1 = workbook.active

    for i in range(0, len(list)):
        sheet1[alphabet[i]+str(row_nr)] = list[i]


# file_name= 'Otomoto_cars.xlsx'
#
# workbook_1 = create_workbook()
# add_header(workbook_1)
# save_file(workbook_1, file_name)



