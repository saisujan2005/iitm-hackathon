# app/sync/delhi_scraper.py

import re
import requests


URL = "https://traffic.delhipolice.gov.in/traffic-offences"


def fetch_delhi_penalties():

    html = requests.get(URL).text

    rows = re.findall(
        r"<tr>(.*?)</tr>",
        html,
        flags=re.DOTALL
    )

    records = []

    for row in rows:

        cols = re.findall(
            r"<td.*?>(.*?)</td>",
            row,
            flags=re.DOTALL
        )

        if len(cols) != 5:
            continue

        clean = []

        for col in cols:

            text = re.sub(
                r"<.*?>",
                "",
                col
            )

            text = (
                text.replace("&nbsp;", " ")
                .strip()
            )

            clean.append(text)

        records.append({
            "state": "Delhi",
            "violation": clean[1],
            "section": clean[2],
            "fine_amount": clean[3]
        })

    return records