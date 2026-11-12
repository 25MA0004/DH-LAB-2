"""
=====================================================================
Topic: Retrieval-Augmented Generation (RAG) Pipeline for Indian Flora & Fauna
Author Name(s): Debopriya Dasgupta
Short Description: End-to-end RAG ingestion, semantic chunk retrieval,
and LLM extraction pipeline over five canonical Bengali novels in
English translation:
  1. The Home and the World (Rabindranath Tagore)
  2. Srikanta (Sarat Chandra Chattopadhyay)
  3. Gora (Rabindranath Tagore)
  4. Anandamath (Bankim Chandra Chattopadhyay)
  5. Kapalkundala (Bankim Chandra Chattopadhyay)
Semester: Monsoon Semester 2026
Affiliation: Student
=====================================================================
"""

import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CORPUS_DIR = Path("corpus")

NOVEL_FILES = {
    "The Home and the World": "the_home_and_the_world.txt",
    "Srikanta": "srikanta.txt",
    "Gora": "gora.txt",
    "Anandamath": "anandamath.txt",
    "Kapalkundala": "kapalkundala.txt",
}

RAG_QUERIES = {
    "flora": (
        "trees forest garden flowers lotus jasmine bakul champak banyan peepal "
        "sal bamboo mango palm kash grass tulsi paddy rice crops herbs plants"
    ),
    "fauna": (
        "tiger leopard jackal hyena wild boar deer elephant cow horse dog "
        "cuckoo koel crow kite vulture owl kingfisher crane peacock "
        "cobra snake crocodile fish rohu hilsa shark firefly bee mosquito"
    ),
}


def load_and_chunk_corpus(corpus_dir: Path, chunk_size: int = 180, overlap: int = 30):
    """Load all five literary texts and split them into overlapping word chunks."""
    chunks = []
    for title, filename in NOVEL_FILES.items():
        filepath = corpus_dir / filename
        if not filepath.exists():
            print(f"[WARNING] Missing corpus file: {filepath}")
            continue
        raw_text = filepath.read_text(encoding="utf-8")
        cleaned = re.sub(r"\s+", " ", raw_text).strip()
        words = cleaned.split(" ")
        step = max(1, chunk_size - overlap)
        for idx in range(0, len(words), step):
            segment = " ".join(words[idx : idx + chunk_size])
            if segment:
                chunks.append({
                    "novel": title,
                    "chunk_id": f"{filename}::chunk_{idx // step}",
                    "text": segment,
                })
    return chunks


def retrieve_top_k(chunks, query: str, top_k: int = 15):
    """Retrieve the top-k ecological context passages using TF-IDF cosine similarity."""
    documents = [c["text"] for c in chunks]
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    doc_matrix = vectorizer.fit_transform(documents)
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, doc_matrix).flatten()
    ranked_indices = scores.argsort()[::-1][:top_k]
    return [
        {**chunks[i], "score": round(float(scores[i]), 4)}
        for i in ranked_indices
        if scores[i] > 0
    ]


def build_extraction_prompt(retrieved_flora, retrieved_fauna):
    """Construct the grounded RAG prompt passed to the LLM (Google Gemini)."""
    flora_context = "\n".join(
        f"[{c['novel']}] {c['text']}" for c in retrieved_flora
    )
    fauna_context = "\n".join(
        f"[{c['novel']}] {c['text']}" for c in retrieved_fauna
    )
    return f"""You are a computational literary ecologist extracting Indian cultural and natural elements.
Using ONLY the retrieved passages below from five Bengali novels (The Home and the World, Srikanta, Gora, Anandamath, Kapalkundala), extract all distinct names of Indian flora and fauna.

Group flora into: Trees, Plants, Flowers, Herbs, Crops.
Group fauna into: Mammals, Birds, Reptiles, Fish, Insects.

Return valid JSON with two keys: "flora_RAG_extraction" and "fauna_RAG_extraction".

=== RETRIEVED BOTANICAL CONTEXT ===
{flora_context}

=== RETRIEVED ZOOLOGICAL CONTEXT ===
{fauna_context}
"""


def run_rag_pipeline():
    if not CORPUS_DIR.exists():
        print(f"Create '{CORPUS_DIR}/' and place the 5 novel .txt files inside to run live retrieval.")
        return
    chunks = load_and_chunk_corpus(CORPUS_DIR)
    print(f"Indexed {len(chunks)} total chunks across {len(NOVEL_FILES)} novels.")
    top_flora = retrieve_top_k(chunks, RAG_QUERIES["flora"], top_k=15)
    top_fauna = retrieve_top_k(chunks, RAG_QUERIES["fauna"], top_k=15)
    prompt = build_extraction_prompt(top_flora, top_fauna)
    Path("rag_grounded_prompt.txt").write_text(prompt, encoding="utf-8")
    print("Saved grounded RAG extraction prompt to 'rag_grounded_prompt.txt'.")


if __name__ == "__main__":
    run_rag_pipeline()