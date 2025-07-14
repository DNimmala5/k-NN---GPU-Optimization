import numpy as np
import json

# Updated constants
DOC_COUNT = 15000
DIMENSION = 20

# Generate random vectors
vectors = np.random.rand(DOC_COUNT, DIMENSION)
# Normalize the vectors
norms = np.linalg.norm(vectors, axis=1, keepdims=True)
vectors = vectors / norms

# Create documents for bulk API
bulk_data = []
for i, vector in enumerate(vectors):
    action = {"index": {"_index": "my-knn-index", "_id": str(i)}}
    doc = {"location": vector.tolist()}  # Changed field name to match your example
    
    bulk_data.append(action)
    bulk_data.append(doc)

# Convert to NDJSON format
bulk_body = "\n".join([json.dumps(line) for line in bulk_data]) + "\n"

# Write to file
with open('knn_bulk_data.json', 'w') as f:
    f.write(bulk_body)
