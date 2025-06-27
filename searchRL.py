import streamlit as st
import chromadb

client = chromadb.PersistentClient(path="chroma_store")
collection = client.get_collection(name="book_versions")

st.title(" Search Final Book Versions")

query = st.text_input("Enter your search query")

if st.button("Search") and query:
    try:
        results = collection.query(
            query_texts=[query],
            n_results=3 
        )

        for i, doc in enumerate(results["documents"][0]):
            st.markdown(f"### 📘 Match #{i + 1}")
            st.write("**Content:**", doc)
            st.write("**Metadata:**", results["metadatas"][0][i])
            st.write("**Distance (lower is better):**", results["distances"][0][i])
            st.markdown("---")

    except Exception as e:
        st.error(f" Error during search: {e}")
