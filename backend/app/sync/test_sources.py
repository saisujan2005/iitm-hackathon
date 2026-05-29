from app.sync.pdf_fetcher import download_pdf
from app.sync.webpage_fetcher import fetch_page
from app.sync.hash_service import generate_hash
from app.sync.source_urls import (
    DELHI_URL,
    KARNATAKA_URL
)


print("Testing Delhi...")

delhi_html = fetch_page(DELHI_URL)

print(
    "Delhi Hash:",
    generate_hash(delhi_html.encode())
)

print("Testing Karnataka...")

karnataka_pdf = download_pdf(KARNATAKA_URL)

print(
    "Karnataka Hash:",
    generate_hash(karnataka_pdf)
)