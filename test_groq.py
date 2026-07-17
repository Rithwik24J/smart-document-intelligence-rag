from llm import load_llm

llm = load_llm()

response = llm.invoke("Say hello.")

print(response.content)