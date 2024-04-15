import streamlit as st
import spacy
import spacy_streamlit as spt

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Streamlit app title and menu
st.title('NER TOKENIZER APP')
menu_task = ['NER', 'Tokenizer']
choice = st.sidebar.selectbox('Select Task', menu_task)

# Handle user choice
if choice == 'NER':
    st.subheader('Named Entity Recognition (NER)')
    rawtext = st.text_area("Enter Text", "Type here...")
    if st.button('Recognize Entities'):
        if rawtext.strip():  # Check if input text is not empty
            docs = nlp(rawtext)
            spt.visualize_ner(docs)
        else:
            st.warning("Please enter some text before recognizing entities.")
elif choice == 'Tokenizer':
    st.subheader('Tokenizer')
    rawtext = st.text_area("Enter Text", "Type here...")
    if st.button('Tokenize'):
        if rawtext.strip():  # Check if input text is not empty
            docs = nlp(rawtext)
            spt.visualize_tokens(docs)
        else:
            st.warning("Please enter some text before tokenizing.")

