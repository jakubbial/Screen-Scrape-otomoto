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
            year.append(info[i].text.replace(" ", ""))
        elif num == 1:
            mileage.append(info[i].text)
        elif num == 2:
            cm3.append(info[i].text)
        elif num == 3:
            engine.append(info[i].text)

    inf = [year, mileage, cm3, engine]
    return inf




def list_cars(site_nr):

    prices = get_prices(site_nr)
    # print(prices)

    cars = get_cars(site_nr)
    # print(cars)

    info = get_car_info(site_nr)
    # print(info)

    cars_all = []

    file = open("auta.txt", "a")

    if (
            len(prices) == len(cars) and
            len(prices) == len(info[0]) and
            len(prices) == len(info[1]) and
            len(prices) == len(info[2]) and
            len(prices) == len(info[3])
    ):

        delimeter = ";"

        for i in range(len(prices)):

            try:
                car = [cars[i].text.replace(" ", "").replace("\n", ""), prices[i].text.replace(" ", "").replace("\n", ""), info[0][i].replace("\n", ""), info[1][i].replace("\n", ""), info[2][i].replace("\n", ""), info[3][i].replace("\n", "")]
                cars_all.append(car)
                file.write(car[0] + delimeter +car[1] + delimeter +car[2] + delimeter +car[3] + delimeter +car[4] + delimeter +car[5] + "\n")
            except Exception as err:
                print("EXCEPTION:", err)
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

    #print(cars_all[0])

    file.close()
    return cars_all


def get_cars_soup(sub_site_number):
    sub_page_soup = generate_soup(str(sub_site_number))
    cars_on_si = sub_page_soup.find_all("article", "adListingItem")
    return cars_on_si


def list_parameters(car_soup):
    adv_params = []

    name = car_soup.find_all("a", "offer-title__link")
    name = name[0].text.replace(" ", "")
    name = name.replace("\n", "")
    adv_params.append(name)

    price = car_soup.find_all("span", "offer-price__number")
    price = price[0].text.replace("                    PLN", "")
    price = price.replace("\n", "")
    price = price.replace(" ", "")
    adv_params.append(price)

    params = car_soup.find_all("li", "offer-item__params-item")

    try:
        year = params[0].text.replace("\n", "")
        adv_params.append(year)
    except:
        adv_params.append("No year")

    try:
        mileage = params[1].text.replace("\n", "")
        adv_params.append(mileage)
    except:
        adv_params.append("No mileage")

    try:
        engine_cap = params[2].text.replace("\n", "")
        adv_params.append(engine_cap)
    except:
        adv_params.append("No engine cap")

    try:
        fuel = params[3].text.replace("\n", "")
        adv_params.append(fuel)
    except:
        adv_params.append("No fuel")

    return adv_params


link = "https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on"
all_pages = int(get_number_of_sites(link))

all_cars = []

for i in range(1, all_pages):
    auta = get_cars_soup(i)

    for j in range (0, len(auta)):
        all_cars.append(list_parameters(auta[j]))

    print(len(all_cars))

