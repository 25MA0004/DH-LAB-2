# =====================================================================
# Topic: Extraction of Indian Cultural Elements Using RAG
# =====================================================================
# Author Name(s): Debopriya Dasgupta
# Short Description: Indian flora and fauna extracted via a Retrieval-
# Augmented Generation (RAG) pipeline across five canonical Bengali
# novels (in English translation): The Home and the World, Srikanta,
# Gora, Anandamath, and Kapalkundala.
# Semester: Monsoon Semester 2026
# Affiliation: Student
# =====================================================================

flora_RAG_extraction = [
    # --- Trees ---
    "Banyan (Ficus benghalensis)",
    "Peepal / Ashwattha (Ficus religiosa)",
    "Sal (Shorea robusta)",
    "Mango (Mangifera indica)",
    "Bakul (Mimusops elengi)",
    "Champak / Champa (Magnolia champaca)",
    "Neem (Azadirachta indica)",
    "Tamarind (Tamarindus indica)",
    "Babla / Babul (Vachellia nilotica)",
    "Hijal (Barringtonia acutangula)",
    "Mahua (Madhuca longifolia)",
    "Sundari Mangrove (Heritiera fomes)",
    "Casuarina / Jhau (Casuarina equisetifolia)",
    "Coconut Palm (Cocos nucifera)",
    "Palmyra Palm / Tal (Borassus flabellifer)",
    "Date Palm / Khejur (Phoenix sylvestris)",
    "Betel-Nut / Areca Palm (Areca catechu)",
    "Jackfruit (Artocarpus heterophyllus)",
    "Sandalwood (Santalum album)",

    # --- Plants ---
    "Bamboo (Bambusa vulgaris)",
    "Kash Grass (Saccharum spontaneum)",
    "Banana / Plantain (Musa paradisiaca)",
    "Betel Vine / Paan (Piper betle)",
    "Screw-Pine / Keya (Pandanus odorifer)",
    "Water Hyacinth (Pontederia crassipes)",
    "Cane / Rattan (Calamus rotang)",

    # --- Flowers ---
    "Sacred Lotus (Nelumbo nucifera)",
    "Water Lily / Shapla (Nymphaea nouchali)",
    "Jasmine / Mallika (Jasminum sambac)",
    "Beli / Arabian Jasmine (Jasminum)",
    "Marigold / Genda (Tagetes erecta)",
    "Hibiscus / Jaba (Hibiscus rosa-sinensis)",
    "Night-Flowering Jasmine / Shiuli (Nyctanthes arbor-tristis)",
    "Rose (Rosa indica)",

    # --- Herbs ---
    "Tulsi / Holy Basil (Ocimum tenuiflorum)",
    "Kusha / Darbha Grass (Desmostachya bipinnata)",
    "Durva / Bermuda Grass (Cynodon dactylon)",
    "Hemp / Ganja (Cannabis sativa)",

    # --- Crops ---
    "Paddy / Rice (Oryza sativa)",
    "Mustard / Sarson (Brassica juncea)",
    "Jute / Pat (Corchorus capsularis)",
    "Sugarcane (Saccharum officinarum)"
]

fauna_RAG_extraction = [
    # --- Mammals ---
    "Royal Bengal Tiger (Panthera tigris tigris)",
    "Indian Leopard / Panther (Panthera pardus fusca)",
    "Golden Jackal (Canis aureus)",
    "Striped Hyena (Hyaena hyaena)",
    "Indian Wild Boar (Sus scrofa cristatus)",
    "Spotted Deer / Chital (Axis axis)",
    "Hanuman Langur / Monkey (Semnopithecus entellus)",
    "Indian Elephant (Elephas maximus indicus)",
    "Zebu Cattle / Cow & Bullock (Bos indicus)",
    "Water Buffalo (Bubalus bubalis)",
    "Horse (Equus ferus caballus)",
    "Indian Pariah Dog (Canis lupus familiaris)",
    "Flying Fox / Fruit Bat (Pteropus medius)",

    # --- Birds ---
    "Asian Koel / Indian Cuckoo (Eudynamys scolopaceus)",
    "Indian Peafowl / Peacock (Pavo cristatus)",
    "House Crow (Corvus splendens)",
    "Black Kite / Pariah Kite (Milvus migrans)",
    "White-Rumped Vulture (Gyps bengalensis)",
    "Barn Owl / Spotted Owlet (Tyto alba / Athene brama)",
    "White-Throated Kingfisher (Halcyon smyrnensis)",
    "Indian Pond Heron / Crane (Ardeola grayii)",
    "Rock Pigeon / Dove (Columba livia)",
    "House Sparrow (Passer domesticus)",
    "Wild Duck / Waterfowl (Anas poecilorhyncha)",
    "Seagull / Coastal Tern (Larus brunnicephalus)",

    # --- Reptiles ---
    "Indian Cobra (Naja naja)",
    "Russell's Viper (Daboia russelii)",
    "Common Krait (Bungarus caeruleus)",
    "Estuarine / Saltwater Crocodile (Crocodylus porosus)",
    "Mugger Crocodile / Gharial (Crocodylus palustris)",
    "Bengal Monitor Lizard (Varanus bengalensis)",
    "Indian Flap-Shell Turtle (Lissemys punctata)",

    # --- Fish ---
    "Rohu / Rui (Labeo rohita)",
    "Hilsa / Ilish (Tenualosa ilisha)",
    "Catla (Labeo catla)",
    "Walking Catfish / Magur (Clarias batrachus)",
    "Estuarine Shark (Carcharhinus leucas)",

    # --- Insects ---
    "Indian Firefly (Luciola praeusta)",
    "Indian Honeybee (Apis cerana indica)",
    "Tropical Mosquito (Anopheles / Culex)",
    "Locust / Grasshopper (Hieroglyphus banian)",
    "Monsoon Cicada (Platypleura octoguttata)"
]

# Provenance mapping across the 5 literary texts in the RAG repository
corpus_flora_fauna_index = {
    "The Home and the World (Rabindranath Tagore)": {
        "flora": [
            "Bakul", "Champak", "Jasmine", "Sacred Lotus", "Mango",
            "Banyan", "Bamboo", "Paddy / Rice", "Mustard"
        ],
        "fauna": [
            "Asian Koel", "House Crow", "Black Kite", "Rock Pigeon",
            "Golden Jackal", "Indian Cobra", "Horse", "Zebu Cattle", "Indian Firefly"
        ]
    },
    "Srikanta (Sarat Chandra Chattopadhyay)": {
        "flora": [
            "Kash Grass", "Babla / Babul", "Banyan", "Peepal", "Bamboo",
            "Hijal", "Tamarind", "Date Palm", "Palmyra Palm", "Water Hyacinth",
            "Tulsi", "Paddy / Rice"
        ],
        "fauna": [
            "Golden Jackal", "Striped Hyena", "Indian Wild Boar", "Indian Leopard",
            "Indian Cobra", "Barn Owl", "White-Rumped Vulture", "White-Throated Kingfisher",
            "Indian Pond Heron", "Rohu", "Hilsa", "Mugger Crocodile", "Indian Firefly"
        ]
    },
    "Gora (Rabindranath Tagore)": {
        "flora": [
            "Mango", "Neem", "Banyan", "Peepal", "Coconut Palm",
            "Betel-Nut / Areca Palm", "Tulsi", "Sandalwood", "Marigold",
            "Paddy / Rice", "Sugarcane"
        ],
        "fauna": [
            "Zebu Cattle (Cow & Bullock)", "Horse", "House Crow",
            "House Sparrow", "Asian Koel", "Black Kite", "Indian Pariah Dog"
        ]
    },
    "Anandamath (Bankim Chandra Chattopadhyay)": {
        "flora": [
            "Sal", "Mahua", "Banyan", "Peepal", "Tamarind", "Bamboo",
            "Sacred Lotus", "Jasmine", "Champak", "Paddy / Rice"
        ],
        "fauna": [
            "Royal Bengal Tiger", "Spotted Deer", "Indian Wild Boar",
            "Hanuman Langur", "Horse", "Indian Elephant",
            "White-Rumped Vulture", "Barn Owl", "Indian Peafowl"
        ]
    },
    "Kapalkundala (Bankim Chandra Chattopadhyay)": {
        "flora": [
            "Casuarina / Jhau", "Screw-Pine / Keya", "Sundari Mangrove",
            "Banyan", "Palmyra Palm", "Coconut Palm", "Bakul", "Jasmine / Mallika"
        ],
        "fauna": [
            "Royal Bengal Tiger", "Estuarine Crocodile", "Estuarine Shark",
            "Indian Cobra", "Golden Jackal", "Seagull", "Indian Pond Heron", "Indian Firefly"
        ]
    }
}

if __name__ == "__main__":
    print(f"Total Indian Flora extracted : {len(flora_RAG_extraction)}")
    print(f"Total Indian Fauna extracted : {len(fauna_RAG_extraction)}")
    print("\nSample Flora:", flora_RAG_extraction[:6])
    print("Sample Fauna:", fauna_RAG_extraction[:6])