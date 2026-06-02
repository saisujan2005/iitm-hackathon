from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text

from app.sync.maharashtra_parser import (
    extract_maharashtra_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

URL = (
    "https://cdnbbsr.s3waas.gov.in/"
    "s3d827f12e35eae370ba9c65b7f6026695/"
    "uploads/2025/01/202501041665079600.pdf"
)

pdf_bytes = download_pdf(URL)

text = extract_pdf_text(pdf_bytes)

records = extract_maharashtra_penalties(text)

print(
    f"Found {len(records)} records"
)

save_penalties(records)

print(
    f"Loaded {len(records)} Maharashtra violations"
)