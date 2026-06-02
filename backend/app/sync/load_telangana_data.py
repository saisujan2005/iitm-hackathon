from app.sync.telangana_scraper import (
    scrape_telangana_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_telangana_penalties()

print(
    f"Found {len(records)} records"
)

save_penalties(records)

print(
    f"Loaded {len(records)} Telangana violations"
)