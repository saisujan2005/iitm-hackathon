import requests
from bs4 import BeautifulSoup

URL = (
    "https://shillongpolice.gov.in/traffic_rules.html"
)


def scrape_meghalaya_penalties():

    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    tables = soup.find_all("table")

    table = tables[1]

    penalties = []

    rows = table.find_all("tr")

    for row in rows[1:]:

        cols = row.find_all(["td", "th"])

        if len(cols) < 4:
            continue

        violation = cols[1].get_text(
            " ",
            strip=True
        )

        fine = cols[2].get_text(
            " ",
            strip=True
        )

        section = cols[3].get_text(
            " ",
            strip=True
        )

        penalties.append({

            "state":
                "Meghalaya",

            "violation":
                violation,

            "section":
                section,

            "fine_amount":
                fine,

            "source_url":
                URL
        })

    return penalties