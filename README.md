# **LLM Narrative Characterization and Entity Extraction**

This repository explores the use of Large Language Models (LLMs) for characterizing narratives and extracting entities. It focuses on identifying key narrative components—Actors, Factors, and Mechanisms (AFM)

**Read more about it in my blog titled:** [*2024-12-XX: From Narrative to Conceptualization: The Role of Large Language Models in Analysis, Modeling, and Simulation*](https://your-website-link.com)

---

## **Repository Structure**

```plaintext
├── .env                     # Environment variables placeholder
├── .gitignore               # Ignored files and directories
├── LICENSE                  # License file for the project
├── README.md                # Project overview and documentation
├── code/                    # Source code for extraction and processing
│   ├── all_llms.py          # Testing script for multiple LLMs
│   ├── gpt-4o.py            # Testing script for GPT-4 outputs
│   ├── llama3.py            # Testing script for Llama outputs
│   └── mistral.py           # Testing script for Mistral outputs
├── data/                    # Data files for entity extraction and characterization
│   ├── AFM.xlsx             # Spreadsheet for narrative analysis
│   ├── llms_output.csv      # Extracted entities from LLMs in CSV format
│   └── llms_output.json     # Extracted entities from LLMs in JSON format
```

---

## **Project Overview**

Narratives are fundamental to human communication, capturing the complexity of real-world phenomena. This project uses LLMs to characterize narratives by identifying:

1. **Actors** - Key participants (e.g., President Joe Biden).
2. **Factors** - Influencing elements (e.g., racial discrimination, redistricting).
3. **Mechanisms** - Actions or processes taken (e.g., issuing public statements).

By organizing these components, we transform unstructured text into structured representations, such as knowledge graphs, for improved analysis and understanding.

---

## **Key Features**

- **Entity Extraction**:
  - Extract entities and their relationships using LLMs like GPT-4o, Llama 3.1, and Mistral.
  - Use Named Entity Recognition (NER) and regex for entity extraction.

- **Narrative Characterization**:
  - Categorize narratives into Actors, Factors, and Mechanisms (AFM).
  - You could build structured models for visualization and analysis.

---

## **Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/bllin001/narrative-characterization.git
cd narrative-characterization
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Configure Environment Variables**
Create a `.env` file to store sensitive information, such as API keys:
```plaintext
OPENAI_KEY=your_openai_api_key
```

---

## **Scripts**

### **`all_llms.py`**
Runs multiple language models to characterize narratives into actors, factors, and mechanisms.

### **`gpt-4o.py`, `llama3.py`, `mistral.py`**
These scripts are used to characterize narratives using specific language models.

---

## **Usage**

1. **Run `all_llms.py` for Multi-Model Analysis**:
   ```bash
   python code/all_llms.py
   ```

2. **Run Specific Model Scripts**:
   To run specific language models:
   ```bash
   python code/gpt-4o.py
   python code/llama3.py
   python code/mistral.py
   ```

---

## **Data**

- **`data/abm_description.txt`**: Contains descriptions of the ABM model.
- **`data/llms_output.csv`**: Outputs of the language models in CSV format.
- **`data/llms_output.json`**: Outputs of the language models in JSON format.
- **`data/prompt_afm.txt`**: Prompt template for AFM characterization.

---

## **Outputs**

Processed outputs include:
- **`llms_output.csv`**: Extracted entities in CSV format.
- **`llms_output.json`**: Extracted entities in JSON format.

---

## **Contributions to Modeling and Simulation**

This project contributes to integrating LLMs with simulation and conceptual modeling by:
1. Benchmarking Named Entity Recognition models for AFM tasks.
2. Developing datasets and scripts for narrative characterization.
3. Extracting and visualizing relationships in narratives using knowledge graphs.

---

## **Future Directions**

- Develop custom NER models for narrative characterization.
- Expand datasets to support training and evaluation of AFM extractions.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
