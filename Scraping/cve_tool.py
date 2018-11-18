# pulls current CVE list from
# the circl.lu API
# input is required to start the process
# the inputs are catered to my needs
# if need to add url's place them in the CIRCL_urls.py
# make sure they follow the naming convention of CIRCL.lu

import datetime
import json
import logging

import pandas as pd
import urllib.request
from CIRCL_urls import urls


def get_json(url_ending):
    """
    Pull JSON of Product vulnerabilities, parse it and return.

    :return: Dict; all CVE entries or latest returned from API.
    """
    logging.info('Starting JSON retrieval...')
    start = datetime.datetime.now()
    # getting the url
    f = urllib.request.urlopen('http://cve.circl.lu/api/' + url_ending)

    # decoding the text
    logging.info('Starting JSON decode. This may take a few minutes.')
    json_string = f.read().decode('utf-8')
    f.close()

    # parsing the information
    parsed_json = json.loads(json_string)

    end = datetime.datetime.now()
    logging.info(
        'JSON decode finished. Processing time: {} seconds.'.format((end-start).seconds)
    )

    return parsed_json


def format_for_spreadsheet(api_results):
    logging.info('Parsing records...')

    records = list()

    for record in api_results:
        cve = record.get('id', None)
        cwe = record.get('cwe', 'Unknown')
        summary = record.get('summary', 'Unknown')
        published = record.get('Published', 'Unknown')
        last_modified = record.get('last-modified', 'Unknown')
        records.append((cve, cwe, summary, published, last_modified))

    return records


def create_csv(records, url_ending):
    url_ending = url_ending.replace('/', '_')
    logging.info('Starting CSV export for {} CVEs...'.format(url_ending))
    df = pd.DataFrame(records, columns=('cve', 'cwe', 'summary', 'published', 'last_modified'))
    df.to_csv('{}_cve_report.csv'.format(url_ending), index=False, encoding='utf-8')
    logging.info('CSV export complete.')


def user_choose_dataset(urls):
    print(
        "This script is capable of generating CVE reports for {} sets. "
        "Which one would you like to use?".format(len(urls))
    )
    for count, name in enumerate(urls):
        print("Option {}: {}".format(count, name))

    while True:
        answer = input("Which number option would you like? ")
        try:
            float(answer)
        except ValueError:
            print("Sorry, I need a number.")
            continue
        answer = int(answer)
        if answer >= len(urls):
            print("Sorry, I don't have that many options. Try again?")
            continue
        if answer < 0:
            print("Don't be a smartass. Try again.")
            continue

        return urls[list(urls.keys())[answer]]


def main():
    url_ending = user_choose_dataset(urls)
    cve_data = get_json(url_ending)
    results = format_for_spreadsheet(cve_data)
    create_csv(results, url_ending)


if __name__ == '__main__':
    FORMAT = '[%(levelname)s] - [%(funcName)s] - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    main()
