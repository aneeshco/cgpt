"""Converstation Buffer Memory"""
from init import *

llm = ChatOpenAI(temperature=0.0, model=llm_model)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=False
)

conversation.predict(input="Hi, my name is Andrew")
conversation.predict(input="What is 1+1?")
conversation.predict(input="What is my name?")
print(memory.buffer)
print("*****************************")
memory.load_memory_variables({})
memory = ConversationBufferMemory()
memory.save_context({"input": "Hi"}, 
                    {"output": "What's up"})
print(memory.buffer)
print("*****************************")
memory.load_memory_variables({})
memory.save_context({"input": "Not much, just hanging"}, 
                    {"output": "Cool"})
print(memory.buffer)
print("*****************************")
memory.load_memory_variables({})

