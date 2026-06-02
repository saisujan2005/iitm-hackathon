import requests
from bs4 import BeautifulSoup
import re

URL = (
    "https://cot.gujarat.gov.in/penalty-structure.htm"
)


def scrape_gujarat_penalties():

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

    table = tables[0]

    penalties = []

    rows = table.find_all("tr")

    for row in rows[1:]:

        cols = row.find_all(["td", "th"])

        if len(cols) < 6:
            continue

        section = cols[2].get_text(
            " ",
            strip=True
        )

        violation = cols[3].get_text(
            " ",
            strip=True
        )

        violation = re.sub(
             r"\s+",
             " ",
             violation
        ).strip()

        first_fine = cols[4].get_text(
            " ",
            strip=True
        )

        second_fine = cols[5].get_text(
            " ",
            strip=True
        )

        fine_text = (
            f"First Offence: {first_fine}"
        )

        fine_text = re.sub(
          r"\s+",
          " ",
          fine_text
        ).strip()

        if second_fine:
            fine_text += (
                f" | Second Offence: {second_fine}"
            )

        penalties.append({

            "state":
                "Gujarat",

            "violation":
                violation,

            "section":
                section,

            "fine_amount":
                fine_text,

            "source_url":
                URL
        })

    return penalties