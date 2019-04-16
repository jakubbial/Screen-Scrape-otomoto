import requests
from bs4 import BeautifulSoup


def create_soup(web_link):
    req = requests.get(Link).text
    soup = BeautifulSoup(req, "lxml")
    return soup


def number_of_all_subpages(soup):
    number_of_pages = soup.find_all("span", "page")[-1].text
    return number_of_pages


def generate_link(page_number):
    link = "https://www.otomoto.pl/osobowe/?page=" + page_number
    return link


Link = "https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on"
otomoto_soup = create_soup(Link)
number_of_sub_pages = number_of_all_subpages(otomoto_soup)


print(generate_link(number_of_sub_pages))
print(number_of_sub_pages)
