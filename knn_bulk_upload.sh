#!/bin/bash
curl -H "Content-Type: application/x-ndjson" -X POST "http://localhost:9200/_bulk" --data-binary "@knn_bulk_data.json"