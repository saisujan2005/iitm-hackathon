from app.sync.meghalaya_scraper import (
    scrape_meghalaya_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

URL = (
    "https://shillongpolice.gov.in/traffic_rules.html"
)

records = scrape_meghalaya_penalties()

print(
    f"Found {len(records)} records"
)

for record in records[:10]:
    print(record)

save_penalties(records)

print(
    f"Loaded {len(records)} Meghalaya violations"
)