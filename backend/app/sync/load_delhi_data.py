from app.sync.delhi_scraper import (
    fetch_delhi_penalties
)

from app.sync.penalty_loader import (
    save_penalties
)

records = fetch_delhi_penalties()

print(f"Found {len(records)} records")

save_penalties(records)

print("Done")