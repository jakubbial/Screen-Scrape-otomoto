import requests
from bs4 import BeautifulSoup


def create_soup(web_link):
    req = requests.get(web_link).text
    soup = BeautifulSoup(req, "lxml")
    return soup


def number_of_all_subpages(soup):
    number_of_pages = soup.find_all("span", "page")[-1].text
    return number_of_pages


def generate_link(page_number):
    link = "https://www.otomoto.pl/osobowe/?page=" + page_number
    return link


def print_price(sub_site_number):
    sub_page_link = generate_link(sub_site_number)
    sub_page_soup = create_soup(sub_page_link)
    prices = sub_page_soup.find_all("span", "offer-price__number")

    for car in prices:
        print(car.text)


link = "https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on"
otomoto_soup = create_soup(link)
number_of_sub_pages = number_of_all_subpages(otomoto_soup)

print(number_of_sub_pages)

for i in range(1, int(number_of_sub_pages)):
    print_price(str(i))

