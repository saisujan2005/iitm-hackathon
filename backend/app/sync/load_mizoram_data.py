from app.sync.mizoram_scraper import (
    scrape_mizoram_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_mizoram_penalties()

print(f"Found {len(records)} records")

save_penalties(records)

print(
    f"Loaded {len(records)} Mizoram violations"
)