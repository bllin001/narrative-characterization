# Read global variable OPENAI_KEY with your API key
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_community.llms import Ollama

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant who characterizes narratives into actors, factors, and mechanisms. Actors can range from governmental bodies to grassroots movements, each playing a distinct role in the narrative construction. Factors encompass socioeconomic, cultural, and environmental variables, while mechanisms refer to processes or actions taken to generate events, analyze a text, and extract the actors, factors, and mechanisms."),
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)

# Initialize the Ollama model
chat_model = Ollama(model="mistral")

# Define the input text and prompt
text = "President Joe Biden criticized the Supreme Court's decision on the redistricting of the South Carolina district by issuing a public statement highlighting concerns about racial discrimination."
input_text = f"What are the actors, factors, and mechanisms in the following text: {text}"


# Generate the response using the LangChain model
response = chat_model.invoke([input_text])
print(response)