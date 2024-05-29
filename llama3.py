import ollama

text = 'President Joe Bide criticized the Supreme Court’s decision on the redistricting of the South Carolina district by issuing a public statement highlighting concerns about racial discrimination.'

prompt = f"I want you to characterize the following text into actors, factors, and mechanisms. Actors can range from governmental bodies to grassroots movements, each playing a distinct role in the narrative construction. Factors encompass the various elements influencing the narrative, such as values, interests, and divergences among stakeholders. Conversely, mechanisms delve into the actors’ actions, strategies, and processes to advance their narratives and agendas. {text}"

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])

print('Narrative Characterization:')
print(response['message']['content'])

prompt = f"Make a visual representation of the narrative characterization. Consider that the nodes represent actors, factors, and mechanisms in the context of a knowledge graph. At the same time, the edges show the relationships on how actors use mechanisms to interact with factors (actions taken by actors), such as “upheld the redistricting,” “criticized the decision,” and “benefited from redistricting.” {response['message']['content']}"

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])

print('Visual Representation of the Narrative Characterization:')
print(response['message']['content'])