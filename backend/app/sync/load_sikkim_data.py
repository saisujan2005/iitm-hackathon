from app.sync.sikkim_scraper import (
    scrape_sikkim_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_sikkim_penalties()

print(
    f"Found {len(records)} records"
)

save_penalties(records)

print(
    f"Loaded {len(records)} Sikkim violations"
)