import re


def clean(text):
    return " ".join(text.split())


def is_english(line):
    return bool(re.search(r"[A-Za-z]", line))


def extract_maharashtra_penalties(text):

    lines = [
        clean(line)
        for line in text.splitlines()
        if clean(line)
    ]

    records = []

    i = 0

    while i < len(lines):

        if re.match(r"^\d+$", lines[i]):

            try:
                section = lines[i + 1]

                if (
                    "MVA" not in section
                    and "CMVR" not in section
                    and "MMVR" not in section
                ):
                    i += 1
                    continue

                violation = lines[i + 2]

                fine = lines[i + 4]

                repetitive = lines[i + 5]

                records.append(
                    {
                        "state": "Maharashtra",
                        "violation": violation,
                        "section": section,
                        "fine_amount": (
                            f"Fine: {fine} | "
                            f"Repetitive Fine: {repetitive}"
                        ),
                        "source_url":
                        "https://cdnbbsr.s3waas.gov.in/s3d827f12e35eae370ba9c65b7f6026695/uploads/2025/01/202501041665079600.pdf",
                    }
                )

            except Exception:
                pass

        i += 1

    return records