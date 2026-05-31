from pathlib import Path
from pypdf import PdfReader


def extract_pdf_text(pdf_path: str):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_law_documents():

    laws_dir = Path("data/laws")

    documents = []

    for pdf_file in laws_dir.glob("*.pdf"):

        try:

            text = extract_pdf_text(
                str(pdf_file)
            )

            documents.append({
                "filename": pdf_file.name,
                "text": text
            })

            print(
                f"Loaded: {pdf_file.name}"
            )

        except Exception as e:

            print(
                f"Failed: {pdf_file.name}"
            )

            print(e)

    return documents