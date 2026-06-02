from app.sync.meghalaya_scraper import (
    scrape_meghalaya_penalties
)

records = scrape_meghalaya_penalties()

print(
    f"Found {len(records)} records"
)

for record in records[:10]:
    print(record)