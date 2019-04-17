import requests
from bs4 import BeautifulSoup


def create_soup(web_link):
    try:
        req = requests.get(web_link).text
    except Exception as req_err:
        print(req_err)

    try:
        soup = BeautifulSoup(req, "lxml")
    except Exception as soup_err:
        print(soup_err)

    return soup


def generate_link(page_number):
    new_link = "https://www.otomoto.pl/osobowe/?page=" + page_number
    return new_link


def number_of_all_subpages(soup):
    number_of_pages = soup.find_all("span", "page")[-1].text
    return number_of_pages


def generate_soup(page_number):
    site_link = generate_link(page_number)
    sub_page_soup = create_soup(site_link)
    return sub_page_soup


def get_number_of_sites(site_link):
    otomoto_soup = create_soup(site_link)
    number_of_sub_pages = number_of_all_subpages(otomoto_soup)
    return number_of_sub_pages


def get_prices(sub_site_number):
    sub_page_soup = generate_soup(str(sub_site_number))
    prices = sub_page_soup.find_all("span", "offer-price__number")
    return prices


def get_cars(sub_site_number):
    sub_page_soup = generate_soup(str(sub_site_number))
    cars = sub_page_soup.find_all("a", "offer-title__link")
    return cars


def get_car_info(sub_site_number):
    sub_page_soup = generate_soup(str(sub_site_number))
    info = sub_page_soup.find_all("li", "offer-item__params-item")
    year = []
    mileage = []
    cm3 = []
    engine = []

    for i in range(0, len(info)):
        num = i % 4
        if num == 0:
            year.append(info[i].text)
        elif num == 1:
            mileage.append(info[i].text)
        elif num == 2:
            cm3.append(info[i].text)
        elif num == 3:
            engine.append(info[i].text)

    inf = [year, mileage, cm3, engine]
    return inf


link = "https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on"

number_of_pages = get_number_of_sites(link)
# print(number_of_pages)

prices = get_prices(2)
# print(prices)

cars = get_cars(2)
# print(cars)

info = get_car_info(2)
# print(info)

cars_all = []

if (
        len(prices) == len(cars) and
        len(prices) == len(info[0]) and
        len(prices) == len(info[1]) and
        len(prices) == len(info[2]) and
        len(prices) == len(info[3])
    ):

    for i in range(len(prices)):

        try:
            car = [cars[i].text, prices[i].text, info[0][i], info[1][i], info[2][i], info[3][i]]
            cars_all.append(car)

        except Exception as err:
            print(len(prices))
            print(len(cars))
            print(len(info[0]))
            print(len(info[1]))
            print(len(info[2]))
            print(len(info[3]))

else:
    print("failure")
    print(len(prices))
    print(len(cars))
    print(len(info[0]))
    print(len(info[1]))
    print(len(info[2]))
    print(len(info[3]))

print(cars_all)




# print(info[0][1])
# print(info[1][2])
# print(info[2][3])
# print(info[3][4])


# print(len(prices))
# print(len(cars))
# print(len(info[0]))