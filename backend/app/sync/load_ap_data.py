from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text

from app.sync.ap_parser import (
    extract_ap_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

URL = (
    "https://www.aptransport.org/html/pdf/prosecution-11-03-10.pdf"
)

pdf_bytes = download_pdf(
    URL
)

text = extract_pdf_text(
    pdf_bytes
)

records = extract_ap_penalties(
    text
)

print(
    f"Found {len(records)} records"
)

save_penalties(
    records
)

print(
    f"Loaded {len(records)} Andhra Pradesh violations"
)