import Web_page_interface
import Excel_functions


link = "https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on"
all_pages = int(Web_page_interface.get_number_of_sites(link))
print(all_pages)

file_name= 'Otomoto_cars.xlsx'

workbook_1 = Excel_functions.create_workbook()
Excel_functions.add_header(workbook_1)


iteration = 0

for i in range(1, 1000):
    auta = Web_page_interface.get_cars_soup(i)
    print("Strona: " + str(i))

    for j in range (0, len(auta)):
        elo = Web_page_interface.list_parameters(auta[j])
        Excel_functions.insert_list(workbook_1, elo, iteration+2)
        Excel_functions.save_file(workbook_1, file_name)
        iteration += 1
