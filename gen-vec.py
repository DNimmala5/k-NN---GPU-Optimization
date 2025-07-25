import numpy as np
import json

# Constants
DOC_COUNT = 10000
DIMENSION = 15

# Generate random vectors
vectors = np.random.rand(DOC_COUNT, DIMENSION)
# Normalize the vectors (L2 normalization)
norms = np.linalg.norm(vectors, axis=1, keepdims=True)
vectors = vectors / norms

# Create documents in the format needed for Elasticsearch bulk API
bulk_data = []
for i, vector in enumerate(vectors):
    action = {"index": {"_index": "my-knn-index", "_id": str(i)}}
    doc = {"location": vector.tolist()}
    
    bulk_data.append(action)
    bulk_data.append(doc)

# Convert to NDJSON format
bulk_body = "\n".join([json.dumps(line) for line in bulk_data]) + "\n"

# Write to file
with open('knn_bulk_data.json', 'w') as f:
    f.write(bulk_body)

# Create the bulk upload script
bulk_upload_script = """
#!/bin/bash
curl -H "Content-Type: application/x-ndjson" -X POST "http://localhost:9200/_bulk" --data-binary "@knn_bulk_data.json"
"""

with open('knn_bulk_upload.sh', 'w') as f:
    f.write(bulk_upload_script)
