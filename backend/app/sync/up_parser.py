import re


PDF_URL = (
    "https://uppolice.gov.in/site/writereaddata/RTI/"
    "RTI_201803191216313459.pdf"
)


def extract_up_penalties(text):

    penalties = []

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    # Find first real offence
    start = None

    for i, line in enumerate(lines):

        if "Driving licence given to" in line:
            start = i - 11   # back up to "1."
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

        joined = " ".join(block)

        # stop before Police Act section
        if "Police Act" in joined:
            break

        if len(block) < 4:
            continue

        # remove serial number
        content = block[1:]

        # remove officer column
        while content and (
            "Police" in content[0]
            or "Gazetted" in content[0]
            or "Inspectors" in content[0]
            or "Officers" in content[0]
            or "Jurisdiction" in content[0]
            or "appointed." in content[0]
            or "-Above-" in content[0]
        ):
            content.pop(0)

        if not content:
            continue

        # find section start
        section_idx = None

        for i, line in enumerate(content):

            if (
                "Motor Vehicles Act" in line
                or "Central Motor Vehicles" in line
                or "U.P. Motor Vehicles" in line
                or line.startswith("Section")
            ):
                section_idx = i
                break

        if section_idx is None:
            continue

        offence = " ".join(
            content[:section_idx]
        )

        remaining = content[section_idx:]

        fine_idx = None

        for i, line in enumerate(remaining):

            if re.search(r"\d+/-", line):
                fine_idx = i
                break

        if fine_idx is None:
            continue

        section = " ".join(
            remaining[:fine_idx]
        )

        fine = " ".join(
            remaining[fine_idx:]
        )

        offence = re.sub(
            r"\s+",
            " ",
            offence
        ).strip()

        section = re.sub(
            r"\s+",
            " ",
            section
        ).strip()

        fine = re.sub(
            r"\s+",
            " ",
            fine
        ).strip()

        penalties.append({

            "state":
                "Uttar Pradesh",

            "violation":
                offence,

            "section":
                section,

            "fine_amount":
                fine,

            "source_url":
                PDF_URL
        })

    return penalties