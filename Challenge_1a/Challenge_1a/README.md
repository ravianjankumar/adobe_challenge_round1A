# Challenge 1A: Understand Your Document  
## PDF Title & Outline Extractor

### 📌 Objective
Build a solution that extracts structured information from a PDF file, including:
- The **document title**
- A hierarchical list of **headings (H1, H2, H3)** with their page numbers

The output is a structured JSON that can be used in downstream tasks like semantic search or recommendation systems.

---

### 📁 Folder Structure

Challenge_1a/
├── main.py
├── Dockerfile
├── requirements.txt
├── input/
│ └── file01.pdf
├── output/
│ └── file01.json ← (auto-generated)
└── README.md

---

### 📄 Sample Output Format

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```
pip install -r requirements.txt
python main.py

docker build --platform linux/amd64 -t pdf-outline-extractor .

docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-outline-extractor

