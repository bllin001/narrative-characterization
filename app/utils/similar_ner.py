import json
from transformers import pipeline

# Load the JSON data
with open('extracted_entities.json', 'r') as file:
    data = json.load(file)

# Extract entities with their types
entities = []
for model_data in data:
    for response in model_data['response']:
        entities.append((response['entity'], response['type']))

# Initialize a similarity model
similarity_model = pipeline('feature-extraction', model='sentence-transformers/all-MiniLM-L6-v2')

# Function to calculate cosine similarity
def cosine_similarity(vec1, vec2):
    return sum(a*b for a, b in zip(vec1, vec2)) / (sum(a**2 for a in vec1)**0.5 * sum(b**2 for b in vec2)**0.5)

# Generate embeddings for each entity
entity_embeddings = {entity: similarity_model(entity[0])[0][0] for entity in entities}

# Create a unique list of entities based on similarity and length
unique_entities = []
threshold = 0.8  # Similarity threshold

for entity, embedding in entity_embeddings.items():
    found_similar = False
    for i, unique_entity in enumerate(unique_entities):
        if cosine_similarity(embedding, entity_embeddings[unique_entity]) > threshold:
            # Apply length comparison only for "Person" entities
            if entity[1] == "Person" and len(entity[0]) > len(unique_entity[0]):
                unique_entities[i] = (entity[0], unique_entity[1])  # Update name, keep type
            found_similar = True
            break
    if not found_similar:
        unique_entities.append(entity)

# Output the unique entities with their types
unique_entities_with_types = [{"entity": entity[0], "type": entity[1]} for entity in unique_entities]

print("Unique Entities with Types:")
print(json.dumps(unique_entities_with_types, indent=4))

# Save the unique entities with their types to a JSON file
with open('unique_entities_with_types.json', 'w') as file:
    json.dump(unique_entities_with_types, file, indent=4)
