import argparse
import sys

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ANIME_PATH = Path.home() / 'Documents' / 'Main' / 'Аниме'

SEASON_DATA = '''
<details><summary>{} сезон; {}</summary>
<a href="{}">Ссыль</a>
</details>
'''

DATA = '''Не смотрел'''

TITLE_XPATH = "//h1[contains(@itemprop, 'name')]"
VIEW_LIST_BUTTON_XPATH = "//div[contains(@id, 'view-list-button')]"
VIEW_LIST_BORDERED_XPATH = "//div[contains(@class, 'view-list bordered')]"

YUMMYANIME_CATALOG_ITEM_LINK = 'https://old.yummyani.me/catalog/item/'


def create_file(file_name: str) -> Path:
    anime_file = ANIME_PATH / f'{file_name}.md'
    anime_file.touch(exist_ok=True)
    return anime_file


class AnimeSeason:
    title: str
    link: str


class AnimeElement:
    title: str
    seasons: list[AnimeSeason] = []

    def write_to_file(self):
        anime_file = create_file(self.title)
        data = DATA

        for idx, season in enumerate(self.seasons, start=1):
            data += SEASON_DATA.format(idx, season.title, season.link)

        anime_file.write_text(data, encoding='utf-8')


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Add anime to obsidian')
    parser.add_argument('-l', '--link', type=str, help='Link to anime main page from site https://old.yummyani.me')
    return parser.parse_args(sys.argv[1:])


def main():
    args = parse_arguments()
    if not hasattr(args, 'link') or not args.link.startswith(YUMMYANIME_CATALOG_ITEM_LINK):
        print(
            "You don't set a link, or set a wrong link (which one don't start with https://old.yummyani.me/catalog/item/)")
        exit()

    anime_element = AnimeElement()

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    print('Successfully created chrome webdriver')
    driver.get(args.link)
    anime_element.title = driver.find_element(By.XPATH, TITLE_XPATH).text
    view_list_button = driver.find_element(By.XPATH, VIEW_LIST_BUTTON_XPATH)
    driver.execute_script("arguments[0].click();", view_list_button)
    view_list_bordered = driver.find_element(By.XPATH, VIEW_LIST_BORDERED_XPATH)
    print('Successfully find all elements on the page')
    for el in view_list_bordered.find_elements(By.TAG_NAME, 'a'):
        anime_season = AnimeSeason()
        anime_season.title = el.text
        anime_season.link = el.get_attribute('href')
        anime_element.seasons.append(anime_season)

    anime_element.write_to_file()
    print(f'Successfully added {anime_element.title} anime to obsidian')


if __name__ == '__main__':
    main()
