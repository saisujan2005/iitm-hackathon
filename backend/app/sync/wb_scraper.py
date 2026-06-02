import requests
from bs4 import BeautifulSoup

URL = (
    "https://www.wbtrafficpolice.com/offences-and-penalties.php"
)


def scrape_wb_penalties():

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

            if len(cols) < 6:
                continue

            violation = cols[1].get_text(
                " ",
                strip=True
            )

            violation_section = cols[2].get_text(
                " ",
                strip=True
            )

            penal_section = cols[3].get_text(
                " ",
                strip=True
            )

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

            if second_fine:
                fine_text += (
                    f" | Second Offence: {second_fine}"
                )

            penalties.append({

                "state":
                    "West Bengal",

                "violation":
                    violation,

                "section":
                    penal_section,

                "fine_amount":
                    fine_text,

                "source_url":
                    URL
            })

    return penalties