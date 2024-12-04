# Read global variable OPENAI_KEY with your API key
import os
import pandas as pd
import json
import openai
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import Ollama


# Load environment variables from .env file
_ = load_dotenv(find_dotenv()) # This loads the .env file

# Set OpenAI API key from environment variable
# openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.environ.get('OPENAI_KEY')

# Define LLMS models
llms_models = ['gpt-4o', 'llama3', 'mistral']
output = []

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant who characterizes narratives into actors, factors, and mechanisms. Actors can range from governmental bodies to grassroots movements, each playing a distinct role in the narrative construction. Factors encompass socioeconomic, cultural, and environmental variables, while mechanisms refer to processes or actions taken to generate events, analyze a text, and extract the actors, factors, and mechanisms."),
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)

# Read AMB model descriptions from abm_description.txt
with open('abm_description.txt', 'r') as file:
    text = file.readlines()

# Define the input text and prompt
prompt = f"What are the actors, factors, and mechanisms in the following text: {text}"

# Initialize the OpenAI model
for model in llms_models:
    if model == 'gpt-4o':
        chat_model = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=openai.api_key)
        response = chat_model.invoke([prompt]).content
    else:
        chat_model = Ollama(model=model)
        response = chat_model.invoke([prompt])
    output.append({'model': model, 'response': response})

# Save output in a json file
with open('llms_output.json', 'w') as file:
    json.dump(output, file)
    
# Save ouput in a csv file
df = pd.DataFrame(output)
df.to_csv('llms_output.csv', index=False)

print(output)
