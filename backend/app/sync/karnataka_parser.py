import re


def extract_penalties(text):

    penalties = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    i = 0

    while i < len(lines):

        if lines[i].isdigit():

            try:

                violation = lines[i + 1]
                section = lines[i + 2]

                fine = lines[i + 3]

                penalties.append(
                    {
                        "state": "Karnataka",
                        "violation": violation,
                        "section": section,
                        "fine_amount": fine,
                        "source_url":
                                     "https://vijayanagarapolice.karnataka.gov.in/storage/pdf-files/traffic%20rules%20%20and%20fines%20e.pdf",

                    }
                )

            except IndexError:
                pass

        i += 1

    return penalties