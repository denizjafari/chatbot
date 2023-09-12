# used for GUI development
import streamlit as st

# needed to load .env file
from dotenv import load_dotenv

# used to read the pdf files
from PyPDF2 import PdfReader

# used to create the embeddings, storing all the text from the pdfs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        # create a pdf reader object
        pdf_reader = PdfReader(pdf)
        # get the text from the pages of the pdf 
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text


def main():
    load_dotenv()
    st.set_page_config(page_title="Virtual Upper Limb Rehab Assistant", page_icon=":robot_face:")
    st.header("Virtual Upper Limb Rehab Assistant :robot_face:")

    st.text_input("How are you feeling today?")
    # use with to add content to the sidebar
    with st.sidebar:
        st.subheader('Your exercises')
        pdf_docs = st.file_uploader("Upload your exercise plan and click on Submit", accept_multiple_files=True)
        # true only when the button is clicked
        if st.button("Submit"):

            # while the program is running, show the spinner to make it more user friendly
            with st.spinner("Processing"):
                # get the pdf text 
                # single string with all the text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

            # get the text chunks


            # create the embeddings for the text chunks and the vector store
    

if __name__ == "__main__":
    main()

