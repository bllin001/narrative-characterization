from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
import os
import re
import json

# Define LLMS models
llms_models = ['llama3', 'mistral']
entities = []
output = []

text = "President Joe Biden criticized the Supreme Court's decision on the redistricting of the South Carolina district by issuing a public statement highlighting concerns about racial discrimination."

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful information extraction system."),
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)

# Define the input text and prompt
prompt = f"Given a passage, your task is to extract all entities and identify their entity types. The output should be a in a list of tuples of the following format: [(\"entity 1\", \"type of entity 1\"),..]\n Passage: {text}"


for model in llms_models:
    chat_model = Ollama(model=model)
    response = chat_model.invoke([prompt])

    # Regex pattern to extract entities and their types
    pattern = r'\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\)'

    # Find all matches in the string
    matches = re.findall(pattern, response)

    # Print the extracted entities and their types
    for entity, entity_type in matches:
        entities.append({'entity': entity, 'type': entity_type})
    print(entities)    
    output.append({'model': model, 'response': entities})

print(output)

# Save the final list of entities by model into a JSON file
output_file_path = os.path.join("utils", "extracted_entities.json")

# Write the data to the JSON file
with open(f"extracted_entities.json", 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

    
