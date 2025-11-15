from google import genai

# Initialize the GenAI client; importing genai client
# gives a text response to a prompt
client = genai.Client() # function inside google gemini; gets info from the gemini model


# Generate content using the Gemini 2.5 Flash model
response = client.models.generate_content( 

    model = 'gemini-2.5-flash',
    contents='What are the different types of cheese created and what does that procees look like?'
    
    
)

print(response.text)