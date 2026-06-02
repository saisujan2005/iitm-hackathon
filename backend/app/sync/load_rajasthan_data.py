from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text
from app.sync.rajasthan_parser import (
    extract_rajasthan_penalties
)
from app.sync.penalty_loader import (
    save_penalties
)

URL = (
    "https://jodhpurpolice.rajasthan.gov.in/"
    "storage/app/public/challan/"
    "PENTLY_JM9X61635150854.pdf"
)

pdf_bytes = download_pdf(URL)

text = extract_pdf_text(pdf_bytes)

records = extract_rajasthan_penalties(text)

print(
    f"Found {len(records)} records"
)

for record in records[:10]:
    print(record)

save_penalties(records)

print(
    f"Loaded {len(records)} Rajasthan violations"
)