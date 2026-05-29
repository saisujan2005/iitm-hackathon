from app.sync.pdf_fetcher import download_pdf
from app.sync.pdf_parser import extract_pdf_text

url = (
    "https://vijayanagarapolice.karnataka.gov.in/"
    "storage/pdf-files/traffic%20rules%20%20and%20fines%20e.pdf"
)

pdf = download_pdf(url)

text = extract_pdf_text(pdf)

print(text[:3000])