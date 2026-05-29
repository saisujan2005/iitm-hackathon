from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text
from app.sync.karnataka_parser import extract_penalties
from app.sync.penalty_loader import save_penalties

URL = (
    "https://vijayanagarapolice.karnataka.gov.in/"
    "storage/pdf-files/traffic%20rules%20%20and%20fines%20e.pdf"
)

pdf = download_pdf(URL)

text = extract_pdf_text(pdf)

records = extract_penalties(text)

save_penalties(records)

print("Done")