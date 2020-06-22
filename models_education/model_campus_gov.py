import requests
from bs4 import BeautifulSoup
from app_properties import headers


def get_campus_courses(query):
    title = ''
    link = ''
    duration = ''
    description = ''
    courses_list = []
    try:
        response = requests.get(f'https://campus.gov.il/?s={query}', headers=headers)
        response = response.text
        data = BeautifulSoup(response, 'lxml')
        courses = data.find_all('div', class_='more-courses-item-inner course-item-courses')
        for c in courses:

            # Databox:
            details = c.find('a', class_='course-details-more-courses course-details link-more-courses')
            # >> Title
            try:
                title = details.find('h5').text
            except:
                title = ''
            # >> Duration
            try:
                duration = details.find('div', class_='duration-single-course duration--more-courses')
                duration = duration.text.replace('|', '-')
            except:
                duration = ''
            # >> Course URL
            try:
                link = details['href']
            except:
                link = ''
            # >> Course description
            try:
                description = details.find('p', class_='org-course-front').text
            except:
                description = ''
            # Building class.
            courses_list.append({
                'title': title,
                'link': link,
                'description': description
            })
    except:
        return False

    return courses_list
