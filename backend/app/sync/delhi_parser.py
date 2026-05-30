from bs4 import BeautifulSoup


def parse_delhi_table(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    table = soup.find("table")

    rows = table.find_all("tr")

    penalties = []

    for row in rows:

        cols = [
            c.get_text(strip=True)
            for c in row.find_all(["td", "th"])
        ]

        if len(cols) < 5:
            continue

        if cols[1] == "Offence Name":
            continue

        try:

            penalties.append({
                "state": "Delhi",
                "violation": cols[1],
                "section": cols[2],
                "fine_amount": cols[3],
                "source_url": "https://traffic.delhipolice.gov.in/traffic-offences",
            })

        except Exception:
            continue

    return penalties