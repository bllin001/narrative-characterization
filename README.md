
## Scripts

### `afm_ner.py`

This script extracts entities and their types from a given text using different language models.

### `similar_ner.py`

This script processes the extracted entities to compute similarities and generate unique entities.

### `all_llms.py`

This script runs multiple language models to characterize narratives into actors, factors, and mechanisms.

### `llama3.py`, `gpt-4o.py`, `mistral.py`

These scripts are used to characterize narratives using specific language models.

## Data

- `data/extracted_entities.json`: Contains the extracted entities from different models.
- `data/unique_entities.json`: Contains the unique entities generated after processing.
- Other JSON files in the `data` directory store intermediate and final results of entity extraction and processing.

## Outputs

- `llms_output.csv`: Contains the output of the language models in CSV format.
- `llms_output.json`: Contains the output of the language models in JSON format.
- `image/cosine_similarity_heatmap_clustered_with_threshold.png`: Heatmap visualization of the cosine similarity between entities.

## Usage

1. Run `afm_ner.py` to extract entities from the text.
    ```sh
    python 
    ```

2. Run `similar_ner.py` to compute similarities and generate unique entities.
    ```sh
    python 
    ```

## License

This project is licensed under the MIT License.