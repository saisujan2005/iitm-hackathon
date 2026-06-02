from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text

from app.sync.up_parser import (
    extract_up_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

URL = (
    "https://uppolice.gov.in/site/writereaddata/RTI/"
    "RTI_201803191216313459.pdf"
)

pdf_bytes = download_pdf(URL)

text = extract_pdf_text(pdf_bytes)

records = extract_up_penalties(text)

print(
    f"Found {len(records)} records"
)



save_penalties(records)

print(
    f"Loaded {len(records)} Uttar Pradesh violations"
)