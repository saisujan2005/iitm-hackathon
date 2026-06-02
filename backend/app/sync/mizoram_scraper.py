import re
import requests
from bs4 import BeautifulSoup

URL = (
    "https://transport.mizoram.gov.in/page/penalties"
)


def scrape_mizoram_penalties():

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

    table = soup.find("table")

    if not table:
        print("No table found")
        return []

    penalties = []

    rows = table.find_all("tr")

    for row in rows:

        cols = row.find_all(["td", "th"])

        if len(cols) < 3:
            continue

        section = cols[0].get_text(
            " ",
            strip=True
        )

        violation = cols[1].get_text(
            " ",
            strip=True
        )

        fine = cols[2].get_text(
            " ",
            strip=True
        )

        # Skip table header
        if section.upper() == "SECTION":
            continue

        # Clean extra spaces
        section = re.sub(
            r"\s+",
            " ",
            section
        ).strip()

        violation = re.sub(
            r"\s+",
            " ",
            violation
        ).strip()

        fine = re.sub(
            r"\s+",
            " ",
            fine
        ).strip()

        # Replace broken rupee symbol
        fine = fine.replace("`", "₹")

        penalties.append({

            "state":
                "Mizoram",

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