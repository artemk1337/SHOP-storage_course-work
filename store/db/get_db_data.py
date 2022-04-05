from bs4 import BeautifulSoup
import collections
import requests
import random
import bs4
import re


def load_page(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


class HeadphonesWeb:
    HEADPHONES = collections.namedtuple("Headphones",
                                        ["image", "name", "year", "sound", "commute", "sports", "office",
                                         "wireless_gaming", "wired_gaming", "phone_cals", "color", "price"])

    @staticmethod
    def _find_table(soup: bs4.BeautifulSoup) -> bs4.element.Tag:
        return soup.find(
            ["div", "table_tool-body is-showing-filters"]) \
            .find(["div", "table_tool-table"]) \
            .find(["div", "simple_table is-first-column-sticky"]) \
            .find(["div", "simple_table-body e-scrollable_content"]) \
            .find(["table", "simple_table-table"]
                  )

    @staticmethod
    def _preapare_headphones_data(headphone_info_list: list) -> dict:
        """

        :param headphone_info_list:
        :return:
        """

        headphone_data = {}
        for idx, value in enumerate(headphone_info_list):
            match idx:
                case 0:
                    headphone_data["image"] = value.find(["img"])["src"]
                    headphone_data["name"] = value \
                        .find(["div", "table_cell_product"]) \
                        .find('a', ["div", "table_cell_product-link"]) \
                        .find(["div", "table_cell_product-details"]) \
                        .find(["div", "table_cell_product-name"]).text
                case 1:
                    headphone_data["year"] = int(value.find(["span", "score_box-value"]).text[:-1])
                case 2:
                    headphone_data["sound"] = float(value.find(["span", "score_box-value"]).text)
                case 3:
                    headphone_data["commute|travel"] = float(value.find(["span"]).text)
                case 4:
                    headphone_data["sport|fitness"] = float(
                        value.find(["span", "score_box-value"]).text)
                case 5:
                    headphone_data["office"] = float(value.find(["span", "score_box-value"]).text)
                case 6:
                    headphone_data["wireless gaming"] = float(
                        value.find(["span", "score_box-value"]).text)
                case 7:
                    headphone_data["wired gaming"] = float(
                        value.find(["span", "score_box-value"]).text)
                case 8:
                    headphone_data["Phone calls"] = float(
                        value.find(["span", "score_box-value"]).text)
                case 9:
                    headphone_data["color"] = value.find(["span", "score_box-value"]).text
                case 10:
                    headphone_data["price"] = random.randint(50, random.randint(400, 1000))
                case _:
                    pass
        return headphone_data

    @classmethod
    def parse_page(cls, url=None, filename=None):
        """
        Parse shop web-page.
        :param url: link shop table
        :param filename: or file with page
        :return: None
        """

        page = requests.get(url) if url else load_page(filename)  # "https://www.rtings.com/headphones/tools/table"

        soup = BeautifulSoup(page, 'html.parser')

        table = cls._find_table(soup)

        tbody = table.find_all(["tbody"])[0]

        headphones_for_db = [cls.HEADPHONES(*cls._preapare_headphones_data([name for name in headphone]).values())
                             for headphone in tbody if isinstance(headphone, bs4.element.Tag)]

        print(f"Total amount of headphones: {len(headphones_for_db)}")


if __name__ == "__main__":
    HeadphonesWeb.parse_page(filename='page.xml')
