import requests
from bs4 import BeautifulSoup
from functions.database_interactions import add_entry, read_resource
import datetime


def transform_date(date_str):
    """Helper function to transform a date string into same format as other sites"""
    date_format = "%d. %m. %Y"

    try:
        datetime_obj = datetime.datetime.strptime(date_str, date_format)
        new_format = "%Y-%m-%d"
        result = datetime_obj.strftime(new_format)
        return result
    except ValueError:
        print("Invalid date format. Please use dd. mm. YYYY")


def process_forum24(sections):
    """Scrapes a sections of Forum24 for articles, processes them, and adds new entries to the database.
    Args:
        sections(list): List of sections that should be processed

    """

    original_data = set([line[5] for line in read_resource('forum24')])
    for section_main in sections:
        for page_num in range(1, 4):
            url = f'https://www.forum24.cz/rubrika{section_main}?stranka={page_num}'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            articles = soup.findAll('article', class_="block py-6 group")
            article_urls = [article.findChild('a')['href'] for article in articles if
                            article.findChild('a')['href'] not in original_data]

            for article_link in article_urls:
                try:
                    article_response = requests.get(article_link)
                    article_soup = BeautifulSoup(article_response.content, "html.parser")

                    title = article_soup.find('h1',
                                              class_="text-2xl md:text-[2.5rem] mb-2 md:mb-0 leading-tight font-extrabold font-fira-sans").text.strip()
                    perex = article_soup.find('strong').text.strip()
                    section = article_soup.find('span', class_="text-brand-blue/70").text.strip().lower()
                    date_div = article_soup.find('div',
                                                 class_="flex items-center space-x-2 text-[.65rem] font-semibold text-slate-500/80 uppercase leading-none")
                    date = transform_date(date_div.select('span')[1].get_text(strip=True).strip())

                    data = {
                        'Title': title,
                        'Section': section,
                        'Perex': perex,
                        'Url': article_link,
                        'Date': date
                    }

                    original_data.add(data['Url'])
                    add_entry(data, 'forum24')
                except AttributeError:
                    continue


if __name__ == "__main__":
    sections = ['/domaci', '/zahranici']
    process_forum24(sections)
