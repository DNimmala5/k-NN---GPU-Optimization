import numpy as np
import json

DOC_COUNT = 1000
DIMENSION = 15
INDEX_NAME = "my-knn-index"
FIELD_NAME = "location"

# Generate L2-normalized random vectors in batches to save memory
batch_size = 10000  # generate 10k vectors at a time
with open("test_bulk_data.json", "w") as f:
    for start in range(0, DOC_COUNT, batch_size):
        end = min(start + batch_size, DOC_COUNT)
        vectors = np.random.rand(end - start, DIMENSION)
        vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
        for i, vec in enumerate(vectors, start=start + 1):
            f.write(json.dumps({"index": {"_index": INDEX_NAME, "_id": str(i)}}) + "\n")
            f.write(json.dumps({FIELD_NAME: vec.tolist()}) + "\n")
