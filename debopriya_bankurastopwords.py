"""
=====================================================================
Topic: Indic Language Stop Words for Natural Language Processing
=====================================================================
Author Name(s): Debopriya Dasgupta
Short Description: This file contains a curated stop-word list for the
Bankura dialect of Bengali (Bankuri / Western Rarh Bengali), spoken in
Bankura district, West Bengal. These words may be used during text
preprocessing in Natural Language Processing (NLP).
Semester: Monsoon Semester 2026
Affiliation: Student
Note:
This list contains illustrative and dialect-specific functional words
(pronouns, postpositions, conjunctions, auxiliary verbs, and discourse
particles) for NLP preprocessing. Please modify it according to your
specific corpus requirements.
=====================================================================
"""

# 1. Bankura Stop Words
# Language: Bankura (Bankuri / Western Rarh Dialect of Bengali)
# Script: Bengali
bankura_stopwords = [
    # --- Pronouns & Demonstratives (সর্বনাম ও নির্দেশক) ---
    "হামি",      # I (dialectal form of আমি)
    "হামার",     # my / mine (আমার)
    "হামাকে",    # to me (আমাকে)
    "হামাক",     # to me - contracted Rarh form
    "হামরা",     # we (আমরা)
    "হামাদের",   # our (আমাদের)
    "হামদের",    # our - contracted form
    "তু",        # you - familiar (তুই/তুমি)
    "তুই",       # you - familiar
    "তোর",       # your (তোর/তোমার)
    "তোহার",     # your - dialectal form
    "তোকে",      # to you (তোকে/তোমাকে)
    "তোক",       # to you - contracted form
    "তোরা",      # you - plural
    "তোমরা",     # you - plural
    "উ",         # he / she / that (ও/সে)
    "উয়ার",     # his / her / its (ওর/তার)
    "উহার",      # his / her / its
    "উর",        # his / her - contracted form
    "উকে",       # to him / her (ওকে/তাকে)
    "উক",        # to him / her - contracted form
    "উরা",       # they (ওরা/তারা)
    "উয়ারা",    # they
    "ই",         # this (এই)
    "এই",        # this
    "ইটা",       # this one (এটা)
    "এইটা",      # this one
    "উটা",       # that one (ওটা)
    "ওটা",       # that one
    "ইয়ার",     # of this (এর)
    "যে",        # who / which
    "যার",       # whose
    "যাকে",      # whom
    "যাক",       # whom - contracted form
    "কে",        # who
    "কার",       # whose
    "কাকে",      # whom
    "কাক",       # whom - contracted form
    "কি",        # what / interrogative particle
    "কী",        # what
    "কিছু",      # some / something
    "কেউ",       # someone / anyone
    "সব",        # all
    "সবাই",      # everyone
    "নিজে",      # self
    "নিজের",     # own

    # --- Postpositions & Case Markers (অনুসর্গ) ---
    "থিকে",      # from (dialectal form of থেকে)
    "থ্যে",       # from - spoken Bankura contraction
    "থেকে",      # from
    "লগে",       # with (dialectal form of সাথে/সঙ্গে)
    "সাথে",      # with
    "সঙ্গে",      # with
    "তরে",       # for (dialectal/poetic form of জন্য)
    "লাগি",      # for (Rarh dialectal postposition)
    "জন্য",      # for
    "জন্যে",     # for
    "দি",        # by / with / through (দিয়ে)
    "দিয়ে",      # by / with
    "দিয়া",      # by / with
    "করে",       # by means of / having done
    "কইরে",      # having done - Bankura epenthetic form
    "মাজে",      # inside / in the middle (মাঝে)
    "মাঝে",      # in the middle
    "ভিতরে",     # inside
    "ভিতর",      # inside
    "উপরে",      # on / above
    "উপর",       # on / above
    "নিচে",      # below / under
    "তলে",       # beneath / under
    "কাছে",      # near
    "পাশে",      # beside
    "আগে",       # before
    "পরে",       # after
    "পাছে",      # behind / after
    "বিনা",      # without
    "ছাড়া",      # without / except
    "পর্যন্ত",    # until
    "তক",        # until / up to
    "পানে",      # towards
    "দিকে",      # towards

    # --- Conjunctions & Connectors (সংযোজক অব্যয়) ---
    "আর",        # and
    "এবং",       # and
    "কিন্তু",     # but
    "তবু",       # yet / still
    "তবুও",      # even then
    "বা",        # or
    "অথবা",      # or
    "নাইলে",     # otherwise (dialectal form of নইলে)
    "নয়তো",      # otherwise
    "যদি",       # if
    "তবে",       # then
    "তাইলে",     # then (dialectal form of তাহলে)
    "তাহলে",     # then
    "কারণ",      # because
    "যেন",       # so that / as if
    "য্যান",      # as if - spoken Bankura form
    "তাই",       # so / therefore
    "যখন",       # when
    "তখন",       # then
    "যেমন",      # as / like
    "তেমন",      # so / such

    # --- Auxiliary & Light Verbs (সহায়ক ক্রিয়া) ---
    "আছে",       # is / exists
    "আছিল",      # was (dialectal past form of ছিল)
    "ছিল",       # was
    "নাই",       # is not / no (dialectal form of নেই)
    "নেই",       # is not
    "হয়",       # is / happens
    "হইল",       # happened / became (হলো)
    "হলো",       # happened / became
    "হল",        # happened / became
    "হবে",       # will be
    "হবেক",      # will be (-ক future suffix typical of Bankura)
    "করে",       # does
    "কইল",       # did (করল)
    "করল",       # did
    "করবে",      # will do
    "করবেক",     # will do (-ক future suffix)
    "যায়",       # goes
    "গেইল",      # went (গেল)
    "গেল",       # went
    "যাবে",      # will go
    "যাবেক",     # will go (-ক future suffix)
    "বটে",       # indeed / is (characteristic Rarh/Bankura copula)
    "বটেক",      # indeed / is (emphatic Bankura form)
    "পারে",      # can / is able to
    "থাকে",      # stays / remains
    "থাকবেক",    # will remain

    # --- Interrogatives, Adverbs & Discourse Particles (প্রশ্নবাচক ও অব্যয়) ---
    "কেনে",      # why (dialectal form of কেন)
    "কেন",       # why
    "ক্যামন",     # how (কেমন)
    "কেমন",      # how
    "কবে",       # when
    "কখন",       # when
    "কুথায়",     # where (dialectal form of কোথায়)
    "কুথা",      # where - contracted Bankura form
    "কোথায়",     # where
    "ইখানে",     # here (এখানে)
    "ইথা",       # here - Rarh dialectal form
    "এখানে",     # here
    "উখানে",     # there (ওখানে)
    "উথা",       # there - Rarh dialectal form
    "ওখানে",     # there
    "সেখানে",    # there
    "অখন",       # now (dialectal form of এখন)
    "এখন",       # now
    "আইজ",       # today (আজ)
    "আজ",        # today
    "কাইল",      # tomorrow / yesterday (কাল)
    "কাল",       # tomorrow / yesterday
    "মেলা",      # many / a lot (iconic Bankura quantifier, e.g., মেলা লোক)
    "খুব",       # very
    "অনেক",      # many / much
    "একটুক",     # a little (একটু)
    "একটু",      # a little
    "অল্প",       # a little / few
    "না",        # no / not
    "নয়",       # is not
    "হ্যাঁ",      # yes
    "তো",        # discourse particle
    "গো",        # vocative/discourse particle
    "আরও",       # more / also
    "শুধু",       # only
    "মাত্র"       # only / merely
]
