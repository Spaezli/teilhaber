import requests
from bs4 import BeautifulSoup
import csv

def clean_string(input_string):
    # Replace all semicolons with colons to avoid delimiter conflict in CSV
    input_string = input_string.replace(';', ':')
    # Remove leading and trailing spaces, tabs, newline, and Zero Width Spaces
    return input_string.strip(' \t\n\r\u200B')


def fetch_calendar_items_to_csv(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    calendar_items = soup.find_all(class_='CalendarItem')
    data_to_write = []

    for item in calendar_items:
        time_element = item.find('time')
        datetime_attribute = clean_string(time_element.get('datetime')) if time_element else ''

        title_element = item.find(class_='CalendarItem__title')
        title_text = clean_string(title_element.text) if title_element else ''

        subtitle_element = item.find(class_='CalendarItem__subtitle')
        subtitle_text = clean_string(subtitle_element.text) if subtitle_element else ''

        tag_elements = item.find_all(class_='EventTag__link')
        tags = ', '.join(clean_string(tag.text) for tag in tag_elements)

        link_element = item.find('a', class_='CalendarItem__link')
        href = 'https://www.karldergrosse.ch' + clean_string(link_element['href']) if link_element else ''

        data_to_write.append((datetime_attribute, title_text, subtitle_text, tags, href))

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')  # Specify delimiter as semicolon
        writer.writerow(['Datetime', 'Title', 'Subtitle', 'Tags', 'Link'])
        writer.writerows(data_to_write)

url = "https://www.karldergrosse.ch/programm/kalender/?page=1&per_page=10"
filename = "karldergrosse_events.csv"
fetch_calendar_items_to_csv(url, filename)
