import os
import pdfplumber


def extract(pdf_path: str) -> str:
    """Extract all text from a PDF file, one page at a time."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            pages.append(f"--- Page {i} ---\n{text}")

    return "\n\n".join(pages)
