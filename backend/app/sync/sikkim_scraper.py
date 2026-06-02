import requests
from bs4 import BeautifulSoup

URL = (
    "https://www.sikkim.gov.in/department/"
    "departmentmenudetails?url=Menu%3Dtransport-department%2Fpenalties"
)


def scrape_sikkim_penalties():

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

    rows = table.find_all("tr")

    penalties = []

    for row in rows[2:]:

        cols = row.find_all("td")

        if len(cols) < 4:
            continue

        section = cols[0].get_text(
            " ",
            strip=True
        )

        first = cols[1].get_text(
            " ",
            strip=True
        )

        second = cols[2].get_text(
            " ",
            strip=True
        )

        third = cols[3].get_text(
            " ",
            strip=True
        )

        penalties.append({

            "state":
                "Sikkim",

            "violation":
                f"Section {section} Offence",

            "section":
                section,

            "fine_amount":
                (
                    f"1st: {first} | "
                    f"2nd: {second} | "
                    f"3rd: {third}"
                ),

            "source_url":
                "https://www.sikkim.gov.in/departments/transport-department/penalties"
        })

    return penalties