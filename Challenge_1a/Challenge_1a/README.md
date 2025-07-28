# 📄 PDF Outline Extractor

This project extracts a structured outline (Title, H1, H2, H3 headings) from PDF documents and outputs a clean JSON file — ideal for document understanding, search, and summarization.

---

## 🚀 Features

- ✅ Extracts:
  - **Title** from the first page
  - **Headings**:
    - `H1`: e.g., `1. Introduction`
    - `H2`: e.g., `1.1 Scope`
    - `H3`: e.g., `1.1.1 Definitions`
- ✅ Outputs valid JSON in the format below:
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "1. Introduction", "page": 1 },
    { "level": "H2", "text": "1.1 What is AI?", "page": 2 },
    { "level": "H3", "text": "1.1.1 History of AI", "page": 3 }
  ]
}
