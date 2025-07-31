import numpy as np
import json

# Constants
DOC_COUNT = 30000
DIMENSION = 15
INDEX_NAME = "my-knn-index"
VECTOR_FIELD = "location"

# Generate random vectors
vectors = np.random.rand(DOC_COUNT, DIMENSION)
# Normalize the vectors (L2 normalization)
norms = np.linalg.norm(vectors, axis=1, keepdims=True)
vectors = vectors / norms

# Create the bulk data
bulk_data = []
for i, vector in enumerate(vectors, 1):  # Start enumeration from 1
    # Action line
    action = {"index": {"_index": INDEX_NAME, "_id": str(i)}}
    # Document line
    doc = {VECTOR_FIELD: vector.tolist()}
    
    # Add both lines
    bulk_data.append(json.dumps(action))
    bulk_data.append(json.dumps(doc))

# Join with newlines and add final newline
bulk_body = "\n".join(bulk_data) + "\n"

# Write to file
with open('bulk_vectors.json', 'w') as f:
    f.write(bulk_body)

print(f"JSON file 'bulk_vectors.json' has been created with {DOC_COUNT} vectors of {DIMENSION} dimensions each.")
print("You can now use this file with your curl command to upload the data.")
