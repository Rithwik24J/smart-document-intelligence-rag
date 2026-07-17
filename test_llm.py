from llm import load_llm

llm = load_llm()

response = llm.invoke("Say hello in one sentence.")

print(response.content)