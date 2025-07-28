# Challenge 1A – Approach Explanation  
## Title & Outline Extractor from PDF

### Objective
The objective is to extract a structured outline from any PDF document (≤ 50 pages), including:
- Document title
- Headings of levels H1, H2, and H3 with page numbers

The output is written in a well-defined JSON format and is designed to be used in offline, CPU-only environments with no internet access and ≤ 200MB model size.

---

### Methodology

#### 1. PDF Parsing
We use `pdfplumber` to open and parse the PDF pages. This allows accurate extraction of words, font sizes, and layout positions — necessary for inferring heading structure.

Each page is processed to:
- Extract raw text
- Extract word-level details (text, font size, position)

---

#### 2. Title Detection
The document title is assumed to be:
- The first large, prominent line of text on the first page
- Typically ≥ 20 font size and longer than a few words

We pick the **first such match** and store it as the document title.

---

#### 3. Heading Level Inference

We use a hybrid technique combining:
- **Font size statistics** across the document to identify most common large sizes
- **Regex pattern matching** for heading-like structures (e.g., numbered titles)

**Font size-based strategy:**
- Collect all font sizes used
- Take the top 3 largest sizes
  - Highest → H1
  - Medium → H2
  - Smallest among top → H3

**Pattern matching enhancements:**
We use regular expressions to detect headings:
- `^\d+\.` → likely H2
- `^\d+\.\([a-zA-Z]\)` → likely H3

We also merge multi-line headings heuristically for improved accuracy.

---

### Output Generation
We construct a JSON object with:
- `"title"`: the inferred document title
- `"outline"`: list of headings with structure:
  ```json
  {
    "level": "H2",
    "text": "3. Introduction to Travel Planning",
    "page": 2
  }
