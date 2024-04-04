import requests
from bs4 import BeautifulSoup


from functions.database_interactions import add_entry, read_resource


def process_idnes(sections, headers):
    """Fetches and processes articles from specified sections on idnes.cz.

    Args:
        sections (list): A list of section names to process (e.g., 'ekonomika', 'domaci').
    """

    original_data = {line[3] for line in read_resource('idnes')}

    for section_main in sections:
        for page_num in range(1, 3):
            url = f'https://www.idnes.cz/{section_main}/{page_num}'
            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.content, "html.parser")
            articles = soup.findAll('a', class_="art-link")

            article_links = [
                article.get('href') for article in articles if
                    article.get('href').startswith('https://www.idnes.cz/') and
                    article.get('href') not in original_data and
                    determine_section(article.get('href'))
            ]
            process_articles(article_links, original_data, headers)


def process_articles(article_links, original_data, headers):
    """Processes a list of article links, extracting data and adding new entries to the database.

    Args:
        article_links (list): A list of article URLs.
        original_data (set): A set of existing URLs to avoid duplicates.
    """

    for link in article_links:
        section = determine_section(link)
        if section is None:
            continue

        article_data = extract_article_data(link, headers)
        if article_data is None:
            continue

        original_data.add(article_data['Url'])
        add_entry(article_data, 'idnes')


def determine_section(link):
    """Determines the section of an idnes.cz article based on its URL.

    Args:
        link (str): The URL of the article.

    Returns:
        str: The section name (e.g., 'ekonomika', 'zahranicni') or None if the section cannot be determined.
    """

    if link.split('/')[3] == 'ekonomika':
        section = 'ekonomika'

    elif link.split('/')[4] in ['domaci', 'zahranicni']:
        section = link.split('/')[4]
    else:
        section = None

    return section


def extract_article_data(link, headers):
    """Extracts relevant data (title, perex, date, section) from an idnes.cz article.

    Args:
        link (str): The URL of the article.

    Returns:
        dict: A dictionary containing the extracted data with keys 'Title', 'Section', 'Perex', 'Url', and 'Date'.
              Returns None if the article is premium or data extraction fails.
    """

    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    if soup.find('p', class_="fsm"):  # Premium article
        return None

    try:
        title = soup.find('h1', itemprop="name headline").text
        perex = soup.find('div', class_="opener").text.strip()
        date = soup.find('span', class_="time-date")['content']
        if determine_section(link):
            return {
                'Title': title,
                'Section': determine_section(link),
                'Perex': perex,
                'Url': link,
                'Date': date
            }
    except AttributeError:
        return None
