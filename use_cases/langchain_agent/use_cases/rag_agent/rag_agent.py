from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Load and split documents
loader = TextLoader("sample.txt")  # Add your file here
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# Embed and store
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(split_docs, embeddings)

# Build RAG chain
retriever = db.as_retriever()
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask a question
query = "What is this document about?"
answer = qa_chain.run(query)
print("Answer:", answer)

