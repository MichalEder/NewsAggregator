import requests
from functions.database_interactions import add_entry, read_resource


def process_novinky_data(headers):
    """Fetches data from Novinky.cz API, processes it, and adds new entries to the database."""

    url = 'https://api-web.novinky.cz/v1/timelines'
    response = requests.get(url, headers=headers)
    content = response.json()
    original_data = {line[1] for line in read_resource('novinky')}

    try:
        for timeline in content['_items']:
            for document in timeline['documents']['_items']:
                title = document['title']
                perex = document['perex']
                uid = document['uid']
                slug = document['slug']
                section = slug.split('-')[0]
                date = document['dateOfPublication']
                url = f'https://www.novinky.cz/clanek/{slug}-{uid}'

                data_local = {
                    'Title': title,
                    'Section': section,
                    'Perex': perex,
                    'url': url,
                    'Date': date
                }

                if (data_local['Title'] not in original_data and
                        data_local['Section'] in ['zahranicni', 'domaci', 'krimi', 'ekonomika']):
                    original_data.add(data_local['Title'])
                    add_entry(data_local, 'novinky')

    except IndexError:
        pass

