from datetime import datetime

from app.db.database import SessionLocal
from app.models.source import Source

from app.sync.pdf_fetcher import download_pdf
from app.sync.webpage_fetcher import fetch_page
from app.sync.hash_service import generate_hash


def sync_source(state, url, source_type):

    db = SessionLocal()

    try:

        if source_type == "PDF":
            content = download_pdf(url)
        else:
            content = fetch_page(url).encode()

        current_hash = generate_hash(content)

        source = (
            db.query(Source)
            .filter(Source.state == state)
            .first()
        )

        if source is None:

            source = Source(
                state=state,
                url=url,
                last_hash=current_hash,
                source_type=source_type
            )

            db.add(source)
            db.commit()

            print(f"{state}: Added to database")

            return

        if source.last_hash == current_hash:

            print(f"{state}: No changes found")

        else:

            print(f"{state}: CHANGE DETECTED")

            source.last_hash = current_hash
            source.last_updated = datetime.utcnow()

            db.commit()

    finally:
        db.close()