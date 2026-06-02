import re


PDF_URL = (
    "https://www.chandigarhtrafficpolice.gov.in/"
    "Content/ChdTrafficAssets/pdf/latest-fine-list.pdf"
)


def extract_punjab_penalties(text):

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    starts = []

    for i, line in enumerate(lines):

        if re.match(
            r"^\d+[A-Z]?\s",
            line
        ):
            starts.append(i)

    starts.append(len(lines))

    records = []

    for idx in range(len(starts) - 1):

        start = starts[idx]
        end = starts[idx + 1]

        block = lines[start:end]

        joined = " ".join(block)

        # offence number
        m = re.match(
            r"^(\d+[A-Z]?)\s+(.*)",
            block[0]
        )

        if not m:
            continue

        offence_no = m.group(1)

        content = [m.group(2)]

        for line in block[1:]:
            content.append(line)

        # find section
        section_idx = None

        for i, line in enumerate(content):

            if (
                "s." in line.lower()
                or "r." in line.lower()
                or "194A" == line
                or "199A" in line
            ):
                section_idx = i
                break

        if section_idx is None:
            continue

        violation = " ".join(
            content[:section_idx]
        )

        remaining = content[section_idx:]

        fine_idx = None

        for i, line in enumerate(remaining):

            if (
                re.search(r"\d+", line)
                and (
                    line.strip().isdigit()
                    or "per excess" in line.lower()
                )
            ):
                fine_idx = i
                break

        if fine_idx is None:
            continue

        section = " ".join(
            remaining[:fine_idx]
        )

        fine_lines = remaining[fine_idx:]

        fine_amount = " ".join(
            fine_lines
        )

        violation = re.sub(
            r"\s+",
            " ",
            violation
        ).strip()

        section = re.sub(
            r"\s+",
            " ",
            section
        ).strip()

        fine_amount = re.sub(
            r"\s+",
            " ",
            fine_amount
        ).strip()

        records.append({

            "state":
                "Punjab",

            "violation":
                violation,

            "section":
                section,

            "fine_amount":
                fine_amount,

            "source_url":
                PDF_URL
        })

    return records