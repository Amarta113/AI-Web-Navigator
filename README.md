# Systems AI Assistant

An AI-powered conversational assistant for Systems Limited inc. built using **Streamlit**, **LangChain**, and **Mixtral LLM**. It leverages **retrieval-augmented generation (RAG)** by embedding and indexing website content into **Qdrant vector store** for contextual question answering.


## 🔍 Features

- Web scraping and chunking of pages using `WebBaseLoader` and `RecursiveCharacterTextSplitter`
- Embedding with `HuggingFace BAAI/bge-small-en`
- Vector storage using `Qdrant`
- Chat with memory using LangChain's `create_history_aware_retriever`
- Context-aware RAG chain for accurate responses
- Interactive UI with `Streamlit` and custom html, css template.
- Supports **Mixtral-8x7B LLM** using Groq API.

---

## 🚀 How It Works

1. Load and split content from a website.
2. Embed the content using HuggingFace embeddings.
3. Store embeddings in Qdrant.
4. Accept user queries via chat interface.
5. Use RAG to retrieve relevant context.
6. Generate accurate answers using Groq's LLM.

## ▶️ Watch the Demo 👇😀

[![Watch on LinkedIn](Images/thumbnail.png)](https://www.linkedin.com/posts/amarta-waghani-b6286229b_ai-rag-langchain-activity-7288130909071904768-sZGf?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEiQSfoBQfo16lgFb6bLPB8ih4mqdW0hwUw)

## What is RAG?

**Retrieval-Augmented Generation (RAG)** is an architecture that combines information retrieval with generative models. Instead of relying only on a language model's internal knowledge, RAG retrieves relevant information from an external knowledge base (like a vector database) and uses that context to generate more accurate and grounded responses.

This approach improves:
- **Accuracy**: Answers are based on real documents, not just model memory.
- **Freshness**: You can update the knowledge base without retraining the model.
- **Efficiency**: Smaller models can perform better with relevant context.

In this project, we use:
- **Qdrant** for storing and retrieving embedded chunks of website data
- **LangChain** to manage retrieval and generation flow
- **Mixtral LLM** to generate responses based on retrieved context


## 🧰 Tech Stack

| Component             | Technology                   |
|----------------------|------------------------------|
| UI                   | Streamlit                    |
| LLM                  | Mixtral via Groq API         |
| Embeddings           | HuggingFace `bge-small-en`   |
| Vector DB            | Qdrant                       |
| Backend Orchestration| LangChain                    |
| Env Variables        | python-dotenv                |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Amarta113/AI-Web-Navigator.git
2. **Install dependancies**
   ```bash
   pip install -r requirements.txt
3. **Set environment variable**
   
   Create a `.env` file and set your Qdrant credentials
   ```bash
   qdrant_url = YOUR-QDRANT-VECTORSTORE-URL
   qdrant_key = YOUR-QDRANT-API-KEY
5. **Run the app**
   ```bash
   steamlit run main.py

## 🔑 Required API Keys
   Groq API Key (input from sidebar at runtime)
   Qdrant API Key (via `.env`)
## 📝 Usage
  1.Open the app in your browser.
  
  2.Paste your Groq API key in the sidebar.
  
  3.Ask questions related to the indexed website.
  
  4.Get instant, context-aware answers.
## 🧩 Customize
-  **Target Website:** Replace the URL in `WebBaseLoader([ ... ])`
  
-  **Model Name:** You can switch from `bge-small-en` to another Hugging Face model based on your needs.
  
   Use the [Hugging Face MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) to select the best model for your use case.
  
-  **Groq Model:** Default is `mixtral-8x7b-32768`, changeable in the code
  
-  **Collection Name:** Change `collection` to anything relevant to your use case

## 🎨 UI Styling
The app uses custom HTML/CSS templates for chat styling. See:

`style.py` → contains `css`, `bot_template`, `user_template`

## 🙌 Acknowledgements

-  [LangChain](https://python.langchain.com/docs/introduction/)

-  [Qdrant]()

-  [Groq](https://groq.com/)

-  [Hugging Face Embeddings](https://huggingface.co/spaces/mteb/leaderboard)

