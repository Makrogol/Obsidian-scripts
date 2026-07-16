from pathlib import Path
from anime_parsers_ru import KodikParser

ANIME_DIR_PATH = Path.home() / 'Documents' / 'Main' / 'Аниме'
TOKEN = '56a768d08f43091901c44b54fe970049'


def get_count_seasons(anime_path: str) -> int:
    count_seasons = 0
    with open(anime_path) as anime_file:
        for line in anime_file.readlines():
            if '<summary>' in line:
                count_seasons += 1
    return count_seasons


def main():
    # for anime in list(ANIME_DIR_PATH.iterdir()):
    #     count_seasons = get_count_seasons(str(anime))
    #     title = anime.stem


    parser = KodikParser(token=TOKEN)
    print('\n'.join([el['title'] for el in
                     parser.search(title="Dark Gathering 2nd Season", limit=None, include_material_data=True, anime_status=None,
                                   strict=True,
                                   only_anime=True)]))


# [0]['material_data']['duration']
if __name__ == '__main__':
    main()
