from app.sync.source_sync_service import sync_source

sync_source(
    "Delhi",
    "https://traffic.delhipolice.gov.in/traffic-offences",
    "WEBPAGE"
)

sync_source(
    "Karnataka",
    "https://vijayanagarapolice.karnataka.gov.in/storage/pdf-files/traffic%20rules%20%20and%20fines%20e.pdf",
    "PDF"
)