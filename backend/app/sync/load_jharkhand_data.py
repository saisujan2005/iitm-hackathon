from app.sync.jharkhand_scraper import (
    scrape_jharkhand_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_jharkhand_penalties()

print(
    f"Found {len(records)} records"
)

save_penalties(records)

print(
    f"Loaded {len(records)} Jharkhand violations"
)