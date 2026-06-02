from app.sync.wb_scraper import (
    scrape_wb_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_wb_penalties()

print(
    f"Found {len(records)} records"
)

save_penalties(records)

print(
    f"Loaded {len(records)} West Bengal violations"
)