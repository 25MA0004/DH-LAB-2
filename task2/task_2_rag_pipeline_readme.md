# Task 2: Extraction of Indian Cultural Elements Using RAG

- **Course Assignment:** Monsoon Semester 2026 — Digital Humanities & NLP
- **Author:** Debopriya Dasgupta
- **Affiliation:** Student
- **Primary Deliverable:** [`flora_fauna.py`](./flora_fauna.py)

---

## 1. Overview

This directory contains the Retrieval-Augmented Generation (RAG) workflow and final extracted Python data lists for **Task 2 (Extraction of Indian Cultural Elements Using RAG)**.

To keep the GitHub repository lightweight and free of large raw text blobs (~400,000+ words across five full-length novels), the plain-text novel files are **not** committed directly to version control. Instead, this repository provides:

1. **`download_corpus.py`** — An automated, zero-dependency script that downloads and cleans the public-domain English translations of all five novels into a local `corpus/` folder.
2. **`rag_pipeline.py`** — The semantic chunking and TF-IDF cosine-similarity retrieval script that extracts high-relevance ecological passages across the corpus and constructs the grounded prompt (`rag_grounded_prompt.txt`) used for LLM extraction (Google Gemini).
3. **`flora_fauna.py`** — The finalized assignment deliverable containing `flora_RAG_extraction`, `fauna_RAG_extraction`, and a novel-by-novel provenance index (`corpus_flora_fauna_index`).

---

## 2. Literary Corpus Covered

The RAG pipeline indexes five canonical Bengali novels in public-domain English translation:

| # | Novel Title | Author | Translator & Edition | Local Corpus Filename |
|---|---|---|---|---|
| 1 | *The Home and the World* | Rabindranath Tagore | Surendranath Tagore (1919, Gutenberg #7166) | `corpus/the_home_and_the_world.txt` |
| 2 | *Srikanta* | Sarat Chandra Chattopadhyay | K. C. Sen & Theodosia Thompson (1922) | `corpus/srikanta.txt` |
| 3 | *Gora* | Rabindranath Tagore | W. W. Pearson (1924) | `corpus/gora.txt` |
| 4 | *Anandamath (The Abbey of Bliss)* | Bankim Chandra Chattopadhyay | Nares Chandra Sen-Gupta (1906) | `corpus/anandamath.txt` |
| 5 | *Kapalkundala (Kopal-Kundala)* | Bankim Chandra Chattopadhyay | H. A. D. Phillips (1885, Wikisource) | `corpus/kapalkundala.txt` |

---

## 3. Directory Structure

```text
task2_rag_cultural_elements/
├── README.md                  # Execution instructions for the invigilator
├── download_corpus.py         # Step 1: Fetches & cleans the 5 novels into corpus/
├── rag_pipeline.py            # Step 2: Chunks corpus, retrieves context & builds RAG prompt
├── flora_fauna.py             # Step 3: Final deliverable with extracted flora & fauna lists
└── corpus/                    # Generated locally when running download_corpus.py
    ├── the_home_and_the_world.txt
    ├── srikanta.txt
    ├── gora.txt
    ├── anandamath.txt
    └── kapalkundala.txt
```

---

## 4. Prerequisites & Setup

- **Python:** Version 3.8 or higher.
- **Dependencies:**
  - `download_corpus.py` and `flora_fauna.py` use **only the Python standard library** (no external packages needed).
  - `rag_pipeline.py` uses `scikit-learn` for TF-IDF vectorization and cosine similarity.

Install `scikit-learn` if it is not already present in your environment:

```bash
pip install scikit-learn
```

---

## 5. Step-by-Step Instructions to Run the Pipeline

### Step 1: Generate the Local Literary Corpus (`download_corpus.py`)

Run the corpus builder script from the directory containing these files:

```bash
python download_corpus.py
```

- **What this does:** Connects to Project Gutenberg, the Internet Archive, and Wikisource, strips boilerplate headers/HTML markup, standardizes metadata headers, and saves all five `.txt` files inside `corpus/`.
- **Offline Alternative:** If running in an environment without internet access, create a `corpus/` folder manually and place plain-text copies of the five novels using the exact filenames listed in Section 2.

---

### Step 2: Run the RAG Chunking & Retrieval Pipeline (`rag_pipeline.py`)

Once the `corpus/` folder is populated, execute the RAG pipeline:

```bash
python rag_pipeline.py
```

- **What this does:**
  1. Loads all five novels from `corpus/` and splits them into overlapping **180-word segments** (30-word overlap).
  2. Vectorizes the chunks using TF-IDF (`ngram_range=(1, 2)`) and retrieves the **top-15 botanical** and **top-15 zoological** passages via cosine similarity.
  3. Assembles the retrieved passages into a grounded LLM prompt and writes it to **`rag_grounded_prompt.txt`**, which was passed to Google Gemini to extract the structured species lists.

---

### Step 3: Verify the Extracted Deliverable (`flora_fauna.py`)

Run or import `flora_fauna.py` to inspect the finalized extraction results:

```bash
python flora_fauna.py
```

- **Data Structures Provided:**
  - `flora_RAG_extraction`: 42 Indian botanical species categorized across *Trees, Plants, Flowers, Herbs, and Crops*.
  - `fauna_RAG_extraction`: 42 Indian zoological species categorized across *Mammals, Birds, Reptiles, Fish, and Insects*.
  - `corpus_flora_fauna_index`: Dictionary mapping each extracted species back to the specific novel(s) in which it appears.