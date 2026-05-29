import fitz


def extract_pdf_text(pdf_bytes):

    text = ""

    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text