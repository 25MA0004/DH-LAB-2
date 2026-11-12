# =====================================================================
# Topic: Extraction of Ableism, Multispecies Affect & Caste Dynamics
# =====================================================================
# Author Name(s): Debopriya Dasgupta
# Short Description: Categorized LLM extractions from Rabindranath
# Tagore's "Subha" (1918) analyzed through Critical Disability Studies,
# Affective Economies, and Ecofeminism, with narrative trajectory plots.
# Semester: Monsoon Semester 2026
# Affiliation: Student
# =====================================================================

import matplotlib.pyplot as plt
import numpy as np

# Categorized LLM extractions (verified verbatim against subha_corpus.txt)
thematic_extractions = {
    "Phonocentric Ableism & Social Stigma": [
        {
            "quote": "All the world seemed to think that, because she did not speak, therefore she did not feel; it discussed her future and its own anxiety freely in her presence.",
            "part": "Part 1"
        },
        {
            "quote": "Especially her mother looked upon her as a deformity in herself.",
            "part": "Part 1"
        },
        {
            "quote": "her mother regarded her with aversion as a stain upon her own body.",
            "part": "Part 1"
        },
        {
            "quote": "he could speak, and his gift of speech left them without any common language.",
            "part": "Part 2"
        },
        {
            "quote": "People blamed them, and even talked of making them outcasts.",
            "part": "Part 2"
        },
        {
            "quote": "His second wife was not dumb; she had a good deal to say.",
            "part": "Part 3"
        }
    ],
    "Embodied & Multispecies Affective Language": [
        {
            "quote": "But black eyes need no translating; the mind itself throws a shadow upon them.",
            "part": "Part 1"
        },
        {
            "quote": "This murmur and movement of Nature were the dumb girl's language; that speech of the dark eyes, which the world of men could not understand, found its meaning in the language of Nature.",
            "part": "Part 1"
        },
        {
            "quote": "Though she had no words, she murmured lovingly, and they understood her gentle sighing better than all speech.",
            "part": "Part 1"
        },
        {
            "quote": "Coming close to her, they would rub their horns softly against her arms, and in dumb, puzzled fashion try to comfort her.",
            "part": "Part 2"
        },
        {
            "quote": "She fed them with her hand; she clasped their necks; she looked into their faces with eyes filled with tears, and the drops fell from her lids on to their hoofs.",
            "part": "Part 3"
        }
    ],
    "Patriarchal Commodification & Caste Orthodoxy": [
        {
            "quote": "With a vague fear that had been gathering for days, she dogged her father and mother like a dumb animal.",
            "part": "Part 3"
        },
        {
            "quote": "She imprisoned her hair, knotting it up in laces, she hung her about with ornaments, and did her best to kill her natural beauty.",
            "part": "Part 3"
        },
        {
            "quote": "Her parents were dizzy with anxiety and fear when they saw the god arrive to select the beast for his sacrifice.",
            "part": "Part 3"
        },
        {
            "quote": "Like the oyster's pearls, the child's tears only increased her value, and he made no other comment.",
            "part": "Part 3"
        },
        {
            "quote": "Having delivered over their dumb girl into another's hands, Subha's parents returned home.",
            "part": "Part 3"
        },
        {
            "quote": "They had saved their caste in this and their safety in the next world!",
            "part": "Part 3"
        }
    ]
}


def visualize_themes():
    categories = list(thematic_extractions.keys())
    short_labels = ["Phonocentric\nAbleism", "Multispecies\nAffect", "Patriarchal\nCommodification"]
    counts = [len(thematic_extractions[c]) for c in categories]

    parts = ["Part 1", "Part 2", "Part 3"]
    part_matrix = np.array([
        [sum(1 for item in thematic_extractions[c] if item["part"] == p) for p in parts]
        for c in categories
    ])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    colors = ["#2B5C8F", "#2E8B57", "#B83A3A"]

    # Panel A: Total frequency per theme
    bars = axes[0].bar(short_labels, counts, color=colors, edgecolor="black", width=0.55)
    axes[0].set_title("A. Total Extracted Thematic Instances", fontsize=12, fontweight="bold")
    axes[0].set_ylabel("Number of Verbatim Passages", fontsize=11)
    axes[0].set_ylim(0, max(counts) + 1.5)
    for bar in bars:
        h = bar.get_height()
        axes[0].text(
            bar.get_x() + bar.get_width() / 2,
            h + 0.15,
            str(int(h)),
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold"
        )

    # Panel B: Structural shift across Parts 1, 2, and 3
    x = np.arange(len(parts))
    width = 0.25
    for idx, (label, color) in enumerate(zip(short_labels, colors)):
        axes[1].bar(
            x + (idx - 1) * width,
            part_matrix[idx],
            width=width,
            label=label.replace("\n", " "),
            color=color,
            edgecolor="black"
        )

    axes[1].set_title("B. Narrative Shift Across Story Parts (Rural to Urban)", fontsize=12, fontweight="bold")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(
        ["Part 1\n(Childhood & Nature)", "Part 2\n(Kinship & Stigma)", "Part 3\n(Calcutta & Marriage)"],
        fontsize=10
    )
    axes[1].set_ylabel("Passages per Section", fontsize=11)
    axes[1].set_ylim(0, 7)
    axes[1].legend(frameon=True, fontsize=9)

    fig.suptitle(
        "Synthetic Reading Analysis of Tagore's 'Subha': Ableism, Affect, and Caste Commodification",
        fontsize=14,
        fontweight="bold"
    )
    plt.tight_layout()
    plt.savefig("subha_theme_analysis.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    visualize_themes()