from app.sync.gujarat_scraper import (
    scrape_gujarat_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_gujarat_penalties()

print(
    f"Found {len(records)} records"
)

save_penalties(records)

print(
    f"Loaded {len(records)} Gujarat violations"
)