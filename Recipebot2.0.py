#Import required libraries
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

#  Page Configuration
st.set_page_config(page_title="Recipe Chatbot", layout="wide")
st.title("Welcome to Recipebot 😊!")

# Initialize the model
llm = ChatOllama(
    model="llama2",  # Fixed model name
    temperature=0.7 
)

# Create Prompt Template and create Chain
prompt = PromptTemplate.from_template("""
You are an expert chef and cooking assistant with years of culinary experience. Based on the ingredients provided, suggest delicious and creative recipes.

Ingredients Available: {ingredients}

Please provide a detailed recipe in the following format:

🍳 RECIPE NAME:
(Suggest a creative and appetizing name)

📋 OVERVIEW:
- Cuisine Type:
- Servings: 
- Difficulty Level: (Easy/Medium/Hard)
- Preparation Time:
- Cooking Time:
- Total Time:

🧪 INGREDIENTS NEEDED:
(List all ingredients with precise measurements)

📝 INSTRUCTIONS:
(Provide numbered, step-by-step cooking instructions)

👨‍🍳 PRO TIPS:
(Share 2-3 professional cooking tips specific to this recipe)

❗ ALLERGEN INFORMATION:
(Mention common allergens present in the recipe)

🔄 SUBSTITUTIONS:
(Suggest possible ingredient substitutions for dietary restrictions)

Keep the response well-structured and practical. If any essential ingredients are missing, suggest possible alternatives.
""")

chain = prompt | llm | StrOutputParser()

# Initialize chat history - Fixed variable name
if "messages" not in st.session_state:
    st.session_state.messages = []  # Fixed variable name

# Display chat history - Fixed variable name
for message in st.session_state.messages:  # Fixed variable name
    with st.chat_message(message["role"]):
        st.write(message["content"])
    
# Chat input
user_input = st.chat_input("Enter your ingredients here (e.g., chicken, rice, tomatoes)...")

# Process new message
if user_input: 
    # Save user message - Fixed variable name
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
        
    # Generate and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Creating recipe..."):
            response = chain.invoke({"ingredients": user_input})
            st.write(response)
            
        # Save assistant's response - Fixed variable name
        st.session_state.messages.append({"role": "assistant", "content": response})