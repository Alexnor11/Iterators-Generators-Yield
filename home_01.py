import json
import hashlib


class Countries:
    URL = 'https://en.wikipedia.org/wiki/'

    def __init__(self, file_path: str):
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            county_title = (title['name']['common'] for title in data)
            self.country_iter = iter(county_title)

    def __iter__(self):
        return self

    def get_link(self, country_title: str):
        country_title = country_title.replace(' ', '_')
        return f"{self.URL}{country_title}"

    def __next__(self):
        county_name = next(self.country_iter)
        return f'{county_name} - {self.get_link(county_name)}'


# возвращает md5 хеш каждой строки файла countries.txt:
def get_hash_lib(file_path: str):
    with open(file_path, 'rb') as f:
        for string in f:
            yield hashlib.md5(string).hexdigest()


if __name__ == '__main__':
    with open('countries.txt', 'w', encoding='utf-8') as file:
        for country_link in Countries('countries.json'):
            file.write(f'{country_link}\n')
            # print(country_link)

    for line in get_hash_lib('countries.txt'):
        print(line)
