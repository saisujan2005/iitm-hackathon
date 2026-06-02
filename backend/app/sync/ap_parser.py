import re


def extract_ap_penalties(text):

    penalties = []

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    HEADINGS = [
        "Traffic Offences by Drivers",
        "Traffic Offences by others",
        "Duty to Produce Documents",
        "Duty to give information",
        "Duty of the Driver in case of Accident",
        "Offences by Conductors",
        "Offences Relating to Registration of Motor Vehicles",
        "Offences Relating to permits",
        "Offences Relating to Insurance",
        "Offence Relating to Construction and Maintenance of vehicle",
        "Offences Relating to Road Safety",
        "Offences Relating to Maintenance of MV’s",
        "Miscellaneous Offence under Chapter XIII"
    ]

    i = 0

    while i < len(lines):

        # Detect serial number
        if re.fullmatch(r"\d{1,2}", lines[i]):

            violation = []
            i += 1

            # Collect violation text until section found
            while (
                i < len(lines)
                and not re.match(
                    r"^\d{3}(-[A-Z])?(\(\d+\))?$",
                    lines[i]
                )
            ):
                violation.append(lines[i])
                i += 1

            if i >= len(lines):
                break

            section = lines[i]
            i += 1

            fine = []

            # Collect fine text until next serial number
            while (
                i < len(lines)
                and not re.fullmatch(
                    r"\d{1,2}",
                    lines[i]
                )
            ):
                fine.append(lines[i])
                i += 1

            fine_text = " ".join(fine)

            # Remove PDF section headings
            for heading in HEADINGS:
                fine_text = fine_text.replace(
                    heading,
                    ""
                )

            fine_text = re.sub(
                r"\s+",
                " ",
                fine_text
            ).strip()

            violation_text = " ".join(
                violation
            )

            violation_text = re.sub(
                r"\s+",
                " ",
                violation_text
            ).strip()

            penalties.append({

                "state":
                    "Andhra Pradesh",

                "violation":
                    violation_text,

                "section":
                    section,

                "fine_amount":
                    fine_text,

                "source_url":
                    "https://www.aptransport.org/html/pdf/prosecution-11-03-10.pdf"
            })

        else:
            i += 1

    return penalties