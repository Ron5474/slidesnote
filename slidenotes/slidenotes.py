import sys
from pathlib import Path
from slidenotes.extractor import extract
from slidenotes.generator import generate


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print("Usage: slidenotes <path/to/slides.pdf>", file=sys.stderr)
        sys.exit(1)

    pdf_path = Path(argv[0])

    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    notes_path = pdf_path.parent / (pdf_path.stem + "_notes.md")

    if notes_path.exists():
        print(f"Notes already exist: {notes_path}")
        return

    print(f"Extracting text from {pdf_path}...")
    text = extract(str(pdf_path))

    print("Generating notes...")
    notes = generate(text)

    notes_path.write_text(notes, encoding="utf-8")
    print(f"Notes saved: {notes_path}")


if __name__ == "__main__":
    main()
