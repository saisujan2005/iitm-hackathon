from app.sync.mp_scraper import (
    scrape_mp_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_mp_penalties()

print(
    f"Found {len(records)} records"
)

save_penalties(records)

print(
    f"Loaded {len(records)} Madhya Pradesh violations"
)