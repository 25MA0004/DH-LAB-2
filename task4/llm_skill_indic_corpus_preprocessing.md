---
name: indic-dialect-corpus-preprocessing
description: Standardizes, cleans, and linguistically preprocesses Indic literary and dialectal texts (such as Bankura/Rarh Bengali) for Natural Language Processing (NLP) and Digital Humanities workflows.
version: 1.0.0
author: [Enter Student Name(s)]
semester: Monsoon Semester 2026
affiliation: [Enter Department and Institution Name]
---

# SKILL: Indic Dialect & Literary Corpus Preprocessing for NLP

## 1. Name of the Work
**Preprocessing and Linguistic Normalization of Indic Dialectal and Literary Texts for Natural Language Processing (NLP)**

## 2. Purpose & Scope
This skill equips a Large Language Model (LLM) to act as a computational linguistics assistant for Indic languages and regional dialects (such as Bankura/Rarh Bengali, Hindi, Nagamese, Mizo, Gujarati, and Tamil). When invoked, the LLM transforms raw, noisy literary or spoken-dialect text into clean, Unicode-normalized, stop-word-filtered datasets ready for downstream tasks such as topic modeling, thematic extraction, Retrieval-Augmented Generation (RAG), and stylometric analysis.

## 3. Trigger Conditions
Activate this skill whenever the user asks to:
- Clean, normalize, or tokenize raw Indic-script or translated South Asian literary texts.
- Remove dialect-specific stop words (e.g., `bankura_stopwords`) while preserving culturally significant nouns, flora/fauna terms, and regional idioms.
- Prepare raw corpus text files before running LLM-based thematic extraction or RAG pipelines.

## 4. Step-by-Step Execution Protocol

### Step 1: Metadata & Boilerplate Stripping
- Identify and remove non-narrative headers, editorial footnotes, page markers (e.g., `[Pg 12]`), URLs, and standalone section numerals (`I`, `II`, `III`) unless explicitly requested for structural indexing.
- Preserve paragraph and sentence boundaries cleanly.

### Step 2: Unicode & Script Normalization
- Enforce **Unicode NFC (Canonical Composition)** across all Indic scripts (Bengali, Devanagari, Gujarati, Tamil, etc.) so split vowel diacritics (matras) and nukta characters are consistently encoded.
- Strip zero-width non-joiners (`U+200C`) and zero-width joiners (`U+200D`) only when they cause duplicate token splits, while preserving valid conjunct ligatures (যুক্তাক্ষর).
- Normalize punctuation variants (e.g., standardizing danda `।` and double danda `॥` spacing).

### Step 3: Dialect-Aware Stop-Word Filtering
- Cross-reference tokens against the target language/dialect stop-word list (for example, `bankura_stopwords` for Bankuri/Rarh Bengali).
- Remove high-frequency functional words—including dialectal pronouns (`হামি`, `উয়ার`), postpositions (`থিকে`, `লগে`, `তরে`), and auxiliary forms (`আছিল`, `নাই`, `বটেক`)—**without** deleting content-bearing regional vocabulary (such as local flora, kinship terms, or agricultural lexemes).

### Step 4: Morphological & Cultural Preservation
- Do **not** apply aggressive rule-based stemming that destroys dialectal verb inflections (such as the Bankura future `-ক` marker in `যাবেক` or `হবেক`) if the downstream task involves sociolinguistic or stylistic analysis.
- Flag and retain culturally specific entities (regional food, festivals, ecology, caste/class markers) for downstream RAG or thematic querying.

### Step 5: Structured Output Generation
Return the processed result in a reproducible, machine-readable JSON or Python-compatible structure containing:
1. `cleaned_text`: Normalized prose with noise removed.
2. `filtered_tokens`: List of content words remaining after dialectal stop-word removal.
3. `removed_stopwords_count`: Integer count of filtered functional tokens.
4. `preserved_cultural_terms`: List of notable regional or cultural lexemes retained.

## 5. Strict Constraints
- **Zero Hallucination:** Never invent, translate, or alter the spelling of authentic dialectal words in the source text.
- **Script Fidelity:** Maintain the original script of the input text unless transliteration is explicitly requested.
- **Deterministic Formatting:** When outputting Python or JSON structures, ensure valid syntax with no unescaped quotes.

## 6. Example Usage

### User Input
> "Preprocess the following Bankura Bengali sentence using `bankura_stopwords`:
> `হামি অখন কুথায় যাবেক তা উয়ার লগে কথা কইরে ঠিক করবেক।`"

### Expected Skill Output
```json
{
  "language_variety": "Bankura Dialect (Western Rarh Bengali)",
  "script": "Bengali",
  "cleaned_text": "হামি অখন কুথায় যাবেক তা উয়ার লগে কথা কইরে ঠিক করবেক।",
  "filtered_tokens": [
    "যাবেক",
    "তা",
    "কথা",
    "ঠিক",
    "করবেক"
  ],
  "removed_stopwords": [
    "হামি",
    "অখন",
    "কুথায়",
    "উয়ার",
    "লগে",
    "কইরে"
  ],
  "linguistic_notes": "Retained dialectal future verb forms ('যাবেক', 'করবেক') carrying the characteristic Rarh/Bankura '-ক' suffix while filtering functional pronouns, adverbs, and postpositions."
}
```

## 7. Verification Checklist Before Finalizing Output
- [ ] All header/footer noise removed without truncating narrative sentences.
- [ ] Indic Unicode characters normalized to NFC.
- [ ] Dialectal functional stop words accurately filtered using the target `*_stopwords.py` module.
- [ ] Output adheres strictly to valid JSON or Python syntax for direct integration into GitHub repositories.
