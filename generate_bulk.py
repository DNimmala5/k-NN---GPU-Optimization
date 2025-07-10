import numpy as np
import json

# === Configuration ===
DOC_COUNT = 10000
DIMENSION = 15
INDEX_NAME = "my-knn-index"
FIELD_NAME = "location"

# === Generate L2-normalized random vectors ===
vectors = np.random.rand(DOC_COUNT, DIMENSION)
norms = np.linalg.norm(vectors, axis=1, keepdims=True)
vectors = vectors / norms

# === Build bulk NDJSON payload ===
bulk_data = []
for i, vector in enumerate(vectors):
    action = {"index": {"_index": INDEX_NAME, "_id": str(i)}}
    doc = {FIELD_NAME: vector.tolist()}
    bulk_data.append(action)
    bulk_data.append(doc)

bulk_body = "\n".join([json.dumps(line) for line in bulk_data]) + "\n"

# === Write NDJSON to file ===
with open('test_bulk_data.json', 'w') as f:
    f.write(bulk_body)

# === Create upload script ===
bulk_upload_script = """
#!/bin/bash
curl -H "Content-Type: application/x-ndjson" -X POST "http://localhost:9200/_bulk" --data-binary "@test_bulk_data.json"
"""

with open('test_bulk_upload.sh', 'w') as f:
    f.write(bulk_upload_script)
