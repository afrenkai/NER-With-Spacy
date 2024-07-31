# import spacy
# import random

# # Load the transformer model
# nlp = spacy.load("en_core_web_trf")

# # Assuming you have your dataset formatted as described above
# dataset = [
#     ("Apple Inc. is planning to open a new store in New York City.", {
#         "entities": [(0, 9, "ORG"), (41, 54, "GPE")]
#     }),
#     ("The Eiffel Tower in Paris attracts millions of visitors each year.", {
#         "entities": [(4, 16, "LOC"), (20, 25, "GPE")]
#     }),
# ]

# # Function to apply NER to a single text
# def perform_ner(text):
#     doc = nlp(text)
#     return [(ent.text, ent.label_) for ent in doc.ents]

# # Process the entire dataset
# results = []
# for text, _ in dataset:
#     entities = perform_ner(text)
#     results.append((text, entities))

# # Print a few random results
# for _ in range(3):
#     sample = random.choice(results)
#     print(f"Text: {sample[0]}")
#     print("Entities:", sample[1])
#     print()

# # If you want to evaluate the model's performance against your annotations:
# def evaluate_ner(dataset):
#     correct = 0
#     total = 0
#     for text, annot in dataset:
#         doc = nlp(text)
#         gold_entities = set([(start, end, label) for start, end, label in annot['entities']])
#         pred_entities = set([(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents])
#         correct += len(gold_entities.intersection(pred_entities))
#         total += len(gold_entities.union(pred_entities))
    
#     precision = correct / total if total > 0 else 0
#     return precision

# precision = evaluate_ner(dataset)
# print(f"Precision: {precision:.2f}")