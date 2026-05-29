from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text
from app.sync.karnataka_parser import extract_penalties

url = (
    "https://vijayanagarapolice.karnataka.gov.in/"
    "storage/pdf-files/traffic%20rules%20%20and%20fines%20e.pdf"
)

pdf = download_pdf(url)

text = extract_pdf_text(pdf)

data = extract_penalties(text)

print(f"Found {len(data)} records\n")

for row in data[:10]:
    print(row)