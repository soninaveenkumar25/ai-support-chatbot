import openai

openai.api_key = "YOUR_API_KEY"

def chatbot(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": query}
        ]
    )
    return response['choices'][0]['message']['content']

if _name_ == "_main_":
    while True:
        user_input = input("Ask something: ")
        if user_input.lower() == "exit":
            break
        print("AI:", chatbot(user_input))
