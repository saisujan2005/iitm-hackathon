from app.sync.delhi_scraper import (
    scrape_delhi
)

from app.sync.penalty_loader import (
    save_penalties
)

records = scrape_delhi()

save_penalties(records)

print(
    f"Saved {len(records)} Delhi penalties"
)