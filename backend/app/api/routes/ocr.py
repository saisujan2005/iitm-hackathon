from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.ocr_service import (
    extract_challan_details,
    explain_violation
)

from app.ai.db_tools import (
    search_by_section
)

router = APIRouter(
    prefix="/ocr",
    tags=["OCR"]
)


@router.post("/upload")
async def upload_challan(
    file: UploadFile = File(...)
):

    image_bytes = await file.read()

    details = extract_challan_details(
        image_bytes
    )

    section = details.get(
        "section"
    )

    if section:

        penalty = search_by_section(
            section
        )

        if penalty:

            explanation = explain_violation(
                penalty.violation,
                penalty.section
            )

            return {

                "ocr": details,

                "official_record": {

                    "violation":
                        penalty.violation,

                    "state":
                        penalty.state,

                    "fine":
                        penalty.fine_amount,

                    "section":
                        penalty.section,

                    "source":
                        penalty.source_url,

                    "explanation":
                        explanation
                }
            }

    return {

        "ocr": details,

        "message":
            "OCR completed successfully. The detected section is not currently available in the local penalty database.",

        "detected_section":
           section    
    }