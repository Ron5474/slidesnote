# slidenotes

A CLI tool that converts PDF lecture slides into structured markdown notes using a privately hosted LLM. Run it before class — show up with notes already drafted.

## How it works

```
slidenotes lecture.pdf
```

1. Extracts all text from the PDF slide deck
2. Sends it to an LLM with a prompt tuned for graduate-level AI coursework
3. Writes `lecture_notes.md` in the same folder as the PDF

If `lecture_notes.md` already exists, it skips without regenerating.

## Output format

The generated notes include:
- Title and lecture overview
- Key concepts with clear explanations
- Important formulas or definitions (in code blocks)
- Summary bullets at the end

## Installation

### 1. Clone or download the project

```bash
cd /path/to/vibe-coding/slidenotes
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies and the CLI

```bash
pip install -r requirements.txt
pip install -e .
```

The `pip install -e .` step installs `slidenotes` as a command inside your virtual environment. While the venv is active, you can run `slidenotes` from any folder.

### 4. Set up your API key

```bash
cp .env.example .env
```

Edit `.env` and fill in your credentials:

```
API_KEY=your_actual_key_here
BASE_URL=https://aiapi.paid.lol
```

The `.env` file is gitignored and never committed.

## Calling slidenotes from any folder (without activating venv each time)

The cleanest way is to add the venv's `bin/` directory to your PATH permanently, or create a shell alias.

### Option A — Shell alias (recommended)

Add this to your `~/.zshrc`:

```bash
alias slidenotes='/path/to/vibe-coding/slidenotes/venv/bin/slidenotes'
```

Then reload:

```bash
source ~/.zshrc
```

Now `slidenotes lecture.pdf` works from any folder, any terminal, without activating the venv.

### Option B — Symlink to /usr/local/bin

```bash
sudo ln -s /path/to/vibe-coding/slidenotes/venv/bin/slidenotes /usr/local/bin/slidenotes
```

This makes it available system-wide as a regular command.

### Option C — Add venv bin to PATH permanently

Add this to your `~/.zshrc`:

```bash
export PATH="/path/to/vibe-coding/slidenotes/venv/bin:$PATH"
```

Replace `/path/to/vibe-coding/slidenotes` with the actual absolute path on your machine (e.g. `/home/ron/workspace/github.com/Ron5474/vibe-coding/slidenotes`).

## Usage

```bash
# Generate notes from a PDF
slidenotes lecture.pdf

# Works with any path
slidenotes ~/Downloads/nlp_week3.pdf
slidenotes /home/ron/courses/deep-learning/lecture5.pdf
```

Output file is always written next to the input PDF, named `<original_name>_notes.md`.

```
nlp_week3.pdf       → nlp_week3_notes.md
lecture5.pdf        → lecture5_notes.md
```

### Skip behavior

If notes already exist for a PDF, slidenotes will not overwrite them:

```
$ slidenotes lecture.pdf
Notes already exist: lecture_notes.md
```

To regenerate, delete the existing notes file first:

```bash
rm lecture_notes.md
slidenotes lecture.pdf
```

## Project structure

```
slidenotes/
├── slidenotes/
│   ├── __init__.py
│   ├── extractor.py     # Extracts text from PDF using pdfplumber
│   ├── generator.py     # Sends text to LLM, returns markdown
│   └── slidenotes.py    # CLI entry point
├── tests/
│   ├── test_extractor.py
│   ├── test_generator.py
│   └── test_cli.py
├── .env                 # Your credentials (not committed)
├── .env.example         # Template
├── requirements.txt
└── setup.py
```

## Running tests

```bash
source venv/bin/activate
pytest tests/ -v
```

## Dependencies

- [pdfplumber](https://github.com/jsvine/pdfplumber) — PDF text extraction
- [openai](https://github.com/openai/openai-python) — OpenAI-compatible API client
- [python-dotenv](https://github.com/theskumar/python-dotenv) — loads `.env` credentials
