# paste into ner_project/train_data.py
# Small sample training data for demo purposes.
# Each item: (text, {"entities":[(start_char, end_char, "LABEL"), ...]})

TRAIN_DATA = [
    ("John Smith works at Acme Corp in London.", {"entities":[(0,10,"PERSON"), (21,30,"ORG"), (34,40,"GPE")]}),
    ("Apple released the iPhone 12 on October 13, 2020.", {"entities":[(0,5,"ORG"), (18,27,"PRODUCT"), (31,48,"DATE")]}),
    ("Dr. Priya Patel was born on 1990-05-05 in Mumbai.", {"entities":[(0,13,"PERSON"), (31,41,"DATE"), (45,51,"GPE")]}),
]
