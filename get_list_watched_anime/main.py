from pathlib import Path

ANIME_DIR_PATH = Path.home() / 'Documents' / 'Main' / 'Аниме'
NOT_WATCHED = 'Не смотрел'


def main():
    list_watched_anime: list[str] = []
    for anime in list(ANIME_DIR_PATH.iterdir()):
        with open(str(anime), 'r', encoding='utf-8') as file:
            status_list = file.readline().strip().split(' ')
            if len(status_list) > 1 and ' '.join(status_list[:2]) == NOT_WATCHED:
                continue

            list_watched_anime.append(anime.stem)

    print('Общее количество просмотренных тайтлов: ' + str(len(list_watched_anime)))
    print('\n'.join(list_watched_anime))


if __name__ == '__main__':
    main()
