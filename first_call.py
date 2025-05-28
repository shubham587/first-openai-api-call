import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)



def first_call():
    system_message = "You are a helpful assistant that provides information and answers questions."

    print("Welcome to the OpenAI API!")
    user_input = input("Please enter your question or request: ")
    
    if not user_input.strip():
        print("You must enter a question or request.")
        return
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
        )
        print("Response from OpenAI:")
        print("--------------------------------------------------")
        # print(f"{response =}")
        print(response.choices[0].message.content)
        print("--------------------------------------------------")
        print("total tokens used:", response.usage.total_tokens)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    first_call()
