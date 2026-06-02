import requests
from bs4 import BeautifulSoup


URL = "https://www.htp.gov.in/road_rules.html"


def scrape_telangana_penalties():

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

    penalties = []

    tables = soup.find_all("table")

    for table in tables:

        rows = table.find_all("tr")

        for row in rows[1:]:

            cols = row.find_all(["td", "th"])

            if len(cols) < 3:
                continue

            violation = cols[0].get_text(
                " ",
                strip=True
            )

            section = cols[1].get_text(
                " ",
                strip=True
            )

            fine = cols[2].get_text(
                " ",
                strip=True
            )

            if not violation:
                continue

            penalties.append({

                "state":
                    "Telangana",

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