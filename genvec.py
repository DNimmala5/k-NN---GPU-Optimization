import numpy as np
import json

# Constants
DOC_COUNT = 10000
DIMENSION = 15

# Generate random vectors - using normal distribution for better IP distribution
vectors = np.random.randn(DOC_COUNT, DIMENSION)  # using randn instead of rand for normal distribution

# Normalize the vectors (L2 normalization) - important for IP similarity
norms = np.linalg.norm(vectors, axis=1, keepdims=True)
vectors = vectors / norms

# Create documents in the format needed for Elasticsearch bulk API
bulk_data = []
for i, vector in enumerate(vectors):
    # Create action line
    action = {"index": {"_index": "my-knn-index", "_id": str(i+1)}}
    # Create document line
    doc = {"location": vector.tolist()}
    
    bulk_data.append(json.dumps(action))
    bulk_data.append(json.dumps(doc))

# Convert to NDJSON format
bulk_body = "\n".join(bulk_data) + "\n"

# Write to file
with open('bulk_data_10k.json', 'w') as f:
    f.write(bulk_body)

print("Generated bulk_data_10k.json with 10k normalized vectors of dimension 15 (suitable for IP similarity)")
