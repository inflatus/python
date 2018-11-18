#!/usr/bin/env python3
# downloadXkcd.py - Downloads every single XKCD comic

import os

import bs4
import requests


def _is_image_valid(image_url):
    if "imgs.xkcd.com/comics" in image_url:
        return True
    else:
        return False


def get_image(soup):
    return 'http:' + soup.select('#comic img')[0].get('src')


def image_is_there(page):
    comicElem = page.select('#comic img')
    if comicElem == []:
        return False

    image_link = get_image(page)

    if _is_image_valid(image_link):
        return True

    return False


def download_image(url):
    print('Downloading image %s...' % (url))
    response = requests.get(url)
    response.raise_for_status()
    return response


def get_prev_url(page, number_only=False):
    prevLink = page.select('a[rel="prev"]')[0]

    if '#' in prevLink:  # comic #1 has a # as the prev identifier
        prevLink = '/#'
    new_url = 'http://xkcd.com' + prevLink.get('href')

    if number_only is True:
        cleaned_number = prevLink.get('href').strip("/")
        if "#" in cleaned_number:  # checking for comic #1 again
            return 1
        else:
            return int(cleaned_number) + 1

    return new_url


def save_image(c_url, image, page):
    filename = os.path.basename(c_url)
    filename = str(get_prev_url(page, number_only=True)) + " - " + filename
    imageFile = open(os.path.join('xkcd', filename), 'wb')
    for chunk in image.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()


def get_new_page(new_url):

    print('Downloading page %s...' % new_url)
    response = requests.get(new_url)
    response.raise_for_status()

    return bs4.BeautifulSoup(response.text)


def main(url):

    while not url.endswith('#'):
        soup = get_new_page(url)

        if image_is_there(soup):

            comicUrl = get_image(soup)

            image = download_image(comicUrl)

            # save the image to ./xkcd
            save_image(comicUrl, image, soup)

            url = get_prev_url(soup)
        else:
            print("Can't find image!")
            # skip this comic
            url = get_prev_url(soup)

    print('done.')

if __name__ == "__main__":
    url = 'http://xkcd.com'
    target_directory = 'xkcd'
    os.makedirs(target_directory, exist_ok=True)

    main(url)
