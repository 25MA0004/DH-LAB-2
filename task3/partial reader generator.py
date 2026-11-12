"""
Synthetic Reading - Step 1: Partial Reading Generator
Story: "Subha" by Rabindranath Tagore (Stories from Tagore, 1918)
Author: Debopriya Dasgupta | Monsoon Semester 2026
"""
import random
import re
import math

CORPUS = "subha_corpus.txt"
OUT = "partial_reading.txt"
N_PARTS = 3
SAMPLE_RATIO = 0.20
SEED = 42

raw = open(CORPUS, encoding="utf-8").read()
story = raw.split("=====STORY STARTS BELOW=====")[1]

paras = [p.strip() for p in story.split("\n") if p.strip()]
text = " ".join(paras)

sentences = re.split(r'(?<=[.!?])(?:"|\u201d)?\s+(?=["\u201c]?[A-Z])', text)
sentences = [s.strip() for s in sentences if s.strip()]

total = len(sentences)
size = math.ceil(total / N_PARTS)
parts = [sentences[i:i + size] for i in range(0, total, size)]

random.seed(SEED)
lines = [
    "PARTIAL READING - Subha (Rabindranath Tagore)",
    f"Method: {total} sentences divided into {len(parts)} equal parts; "
    f"random {int(SAMPLE_RATIO * 100)}% of sentences sampled per part (seed={SEED}).",
    "Sentences are shown in their original story order.",
    "=" * 70
]

for n, part in enumerate(parts, 1):
    k = max(1, round(len(part) * SAMPLE_RATIO))
    idx = sorted(random.sample(range(len(part)), k))
    lines.append(f"\nPART {n}  ({len(part)} sentences, {k} sampled)")
    lines.append("-" * 70)
    for i in idx:
        lines.append(f"[{n}.{i+1}] {part[i]}")

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"Total sentences: {total}; parts: {[len(p) for p in parts]}")