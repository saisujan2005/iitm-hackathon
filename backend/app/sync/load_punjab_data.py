from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text

from app.sync.punjab_parser import (
    extract_punjab_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

URL = (
    "https://www.chandigarhtrafficpolice.gov.in/"
    "Content/ChdTrafficAssets/pdf/latest-fine-list.pdf"
)

pdf_bytes = download_pdf(URL)

text = extract_pdf_text(pdf_bytes)

records = extract_punjab_penalties(text)

print(
    f"Found {len(records)} records"
)

# Uncomment only for debugging
# for record in records[:10]:
#     print(record)

save_penalties(records)

print(
    f"Loaded {len(records)} Punjab violations"
)