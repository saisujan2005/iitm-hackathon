from fastapi import APIRouter

router = APIRouter(prefix="/laws", tags=["Laws"])

@router.get("/")
def get_laws():

    return {
        "laws": [
            {
                "state": "Karnataka",
                "law": "Helmet mandatory under Section 129"
            },
            {
                "state": "Delhi",
                "law": "Seatbelt mandatory"
            }
        ]
    }