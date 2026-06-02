import re


PDF_URL = (
    "https://jodhpurpolice.rajasthan.gov.in/"
    "storage/app/public/challan/"
    "PENTLY_JM9X61635150854.pdf"
)


def extract_rajasthan_penalties(text):

    penalties = []

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    start = None

    for i, line in enumerate(lines):

        if line == "1.":
            start = i
            break

    if start is None:
        return penalties

    lines = lines[start:]

    blocks = []
    current = []

    for line in lines:

        if re.fullmatch(r"\d+\.", line):

            if current:
                blocks.append(current)

            current = [line]

        else:
            current.append(line)

    if current:
        blocks.append(current)

    for block in blocks:

        if len(block) < 4:
            continue

        serial = block[0]

        section = block[1]

        content = block[2:]

        fine_start = None

        for i, line in enumerate(content):

            if (
                "/-" in line
                or "For first offence" in line
                or "For first  offence" in line
                or "For subsequent offence" in line
                or "For Subsequent offence" in line
                or "per such vehicle" in line
                or "per such component" in line
                or "per excess passenger" in line
            ):
                fine_start = i
                break

        if fine_start is None:
            continue

        violation = " ".join(
            content[:fine_start]
        )

        fine = " ".join(
            content[fine_start:]
        )

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

        penalties.append({

            "state":
                "Rajasthan",

            "violation":
                violation,

            "section":
                section,

            "fine_amount":
                fine,

            "source_url":
                PDF_URL
        })

    return penalties