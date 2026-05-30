import requests

from app.sync.delhi_parser import (
    parse_delhi_table
)

URL = (
    "https://traffic.delhipolice.gov.in/"
    "traffic-offences"
)


def scrape_delhi():

    response = requests.get(URL)

    return parse_delhi_table(
        response.text
    )


if __name__ == "__main__":

    records = scrape_delhi()

    print(
        f"Found {len(records)} records"
    )

    for item in records[:10]:
        print(item)