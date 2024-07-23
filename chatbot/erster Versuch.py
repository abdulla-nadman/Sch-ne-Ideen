# bot.py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend ??",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"?? {chatbot.get_response(query)}")



import time

start_time = time.perf_counter()

# Your code or function call here

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time)
