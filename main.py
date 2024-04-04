from functions.scrape_idnes import process_idnes
from functions.api_novinky import process_novinky_data
from functions.scrape_forum24 import process_forum24

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

sections_idnes = ['/zpravy/domaci', '/zpravy/zahranicni', '/ekonomika']
sections_forum24 = ['/domaci', '/zahranici']

process_novinky_data(headers=HEADERS)
print('Novinky update completed')
process_forum24(sections_forum24, headers=HEADERS)
print('Forum24 update completed')
process_idnes(sections_idnes, headers=HEADERS)
print('Idnes update completed')