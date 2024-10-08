# A simple query responder

import random

# Define a dictionary of queries and their corresponding responses
query_responses = {
    "What's your name?": ["My name is Query Responder.", "I'm Query Responder."],
    "How are you doing?": ["I'm doing well, thank you.", "I'm doing great, thanks for asking!"],
    "What's the weather like?": ["I'm sorry, I cannot provide weather information at the moment.", "I'm afraid I don't have access to weather information."],
    "Tell me a joke.": ["Why don't scientists trust atoms? Because they make up everything.", "Why did the tomato turn red? Because it saw the salad dressing!"],
    "What is the meaning of life?": ["That's a deep question. I'm afraid I don't have an answer for you."],
    "What's the capital of France?": ["The capital of France is Paris.", "Paris is the capital of France."]
}

# Define a function that returns a response for a given query
def get_response(query):
    response = query_responses.get(query)
    if response:
        return random.choice(response)
    else:
        return "I'm sorry, I don't understand your question."

# Test the function with some queries
print(get_response("What's your name?"))
print(get_response("How are you doing?"))
print(get_response("What's the weather like?"))
print(get_response("Tell me a joke."))
print(get_response("What is the meaning of life?"))
print(get_response("What's the capital of France?"))



# simple query responder with open AI(api key)

import openai
import random

# Your OpenAI API key (replace with your actual API key)
openai.api_key = 'YOUR_API_KEY_HERE'

# Define a function that returns a response for a given query using OpenAI API
def get_response(query):
    try:
        # Call the OpenAI API with the query
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose different models
            prompt=query,
            max_tokens=150  # Adjust the response length as needed
        )
        # Extract the text response
        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        return f"An error occurred: {e}"

# Test the function with some queries
print(get_response("What's your name?"))
print(get_response("How are you doing?"))
print(get_response("What's the weather like?"))
print(get_response("Tell me a joke."))
print(get_response("What is the meaning of life?"))
print(get_response("What's the capital of France?"))

