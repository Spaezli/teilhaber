import requests
from bs4 import BeautifulSoup








def fetch_calendar_items(url):
    # Send HTTP request to the URL
    response = requests.get(url)
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the class 'CalendarItem'
    calendar_items = soup.find_all(class_='CalendarItem')

    # Print each item or return them
    for item in calendar_items:
        time_element = item.find('time')

        if time_element:
            datetime_attribute = time_element.get('datetime')
            #visible_date = first_time_element.text

        title_element = item.find(class_='CalendarItem__title')

        if title_element:
            title_text = title_element.text.strip()  # Strip to remove any extra whitespace
            print(f"Calendar Item - Title: {title_text}")

        subtitle_element = item.find(class_='CalendarItem__subtitle')

        if subtitle_element:
            subtitle_text = subtitle_element.text.strip()
            print(f"Calendar SubItem - Title: {subtitle_text}")

        tag_elements = item.find_all(class_='EventTag__link')

        if tag_elements:
            tags = [tag.text.strip() for tag in tag_elements]
            print(f"Calendar Item - Tags: {tags}")

        link_element = item.find('a', class_='CalendarItem__link')

        if link_element:
            href = 'https://www.karldergrosse.ch' + link_element['href']  # Extract the href attribute
            print(f"Calendar Item - Link: {href}")


    return calendar_items

url = "https://www.karldergrosse.ch/programm/kalender/?page=1&per_page=10"
fetch_calendar_items(url)
