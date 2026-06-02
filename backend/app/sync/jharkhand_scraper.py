import requests
from bs4 import BeautifulSoup

URL = (
    "https://echallan.jhpolice.gov.in/app/actsection"
)


def scrape_jharkhand_penalties():

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

    print(
        f"Found {len(tables)} tables"
    )

    penalties = []

    for table in tables:

        rows = table.find_all("tr")

        print(
            f"Table rows: {len(rows)}"
        )

        for row in rows[1:]:

            cols = row.find_all(["td", "th"])

            if len(cols) < 4:
                continue

            section = cols[1].get_text(
                " ",
                strip=True
            )

            violation = cols[2].get_text(
                " ",
                strip=True
            )

            fine = cols[3].get_text(
                " ",
                strip=True
            )

            penalties.append({

                "state":
                    "Jharkhand",

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