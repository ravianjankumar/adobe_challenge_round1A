import os
import json
import re
import pdfplumber
from pathlib import Path

def extract_headings(pdf_path):
    title = ""
    outline = []

    with pdfplumber.open(pdf_path) as pdf:
        page_texts = [(i + 1, page.extract_text() or "") for i, page in enumerate(pdf.pages)]
        for line in page_texts[0][1].split("\n"):
            if len(line.strip()) > 15:
                title = line.strip()
                break
        if not title:
            title = "Untitled Document"

        h1_pattern = re.compile(r"^\d+\.\s+[^().]{3,}")
        h2_pattern = re.compile(r"^\d+\.\d+\s+.+")
        h3_pattern = re.compile(r"^\d+\.\d+\.\d+\s+.+") 

        for page_num, text in page_texts:
            lines = text.split("\n")
            for line in lines:
                line = line.strip()
                if not line or len(line.split()) < 3:
                    continue

                if h3_pattern.match(line):
                    outline.append({"level": "H3", "text": line, "page": page_num})
                elif h2_pattern.match(line):
                    outline.append({"level": "H2", "text": line, "page": page_num})
                elif h1_pattern.match(line):
                    outline.append({"level": "H1", "text": line, "page": page_num})

    return title, outline

def process_pdfs():
    base_dir = Path(__file__).resolve().parent
    input_dir = base_dir / "input"
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF(s) in {input_dir}")

    for pdf_file in pdf_files:
        title, outline = extract_headings(pdf_file)
        result = {
            "title": title,
            "outline": outline
        }

        output_file = output_dir / f"{pdf_file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        print(f"Processed {pdf_file.name} -> {output_file.name}")

if __name__ == "__main__":
    print("Starting PDF outline extraction...")
    process_pdfs()
    print("All PDFs processed.")
