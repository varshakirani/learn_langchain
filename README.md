In this project, we learn about multiple parts of LangChain ecosystem.   

<img src="resources/langchain_framework.png" width="400">

The parts that are introduced in this project are:  
1. LangChain  
2. LangSmith  
3. LangServe

The LLM models used are:  
1. OpenAI gpt-3.5-turbo
2. llama2 via Ollama integration

### Environment setup

```
## create conda virtual environment
conda create -n chatbot_langchain_env python=3.10 -y

## activate virtual env
conda activate chatbot_langchain_env

## install all required packages from requirement
pip install -r requirements.txt
```

## ChatBot

### Using OpenAI
In the project, [openai_tutorial.py](chatbot/openai_tutorial.py) file contains simple tutorial to use OpenAI LLM model gpt-3.5-turbo with Langchain and can be traced on [LangSmith UI](https://smith.langchain.com/). 

Step 1: In order to use OpenAI LLM models, you need to load money in OpenAI website and get an OPENAI API key. Based on the token size, the usage is calculated and it will be charged.   
Step 2: Along with `langchain_core` package, `langchain_openai` package is required.  
Step 3: In order to see the activity of the chatbot on Langsmith, LangSmith API key needs to be saved along with setting the variable `LANGCHAIN_TRACING_V2` to "true". 
Step 4: The streamlit client can be run using the command `streamlit run openai_tutorial.py`  

### Using Ollama
Ollama is a platform where multiple open source LLM models can be run directly on local machine. Refer [locallamma_tutorial.py](chatbot/locallamma_tutorial.py) file.

Step 1: Ollama needs to be downloaded from [link](https://ollama.com/).  
Step 2: After downloading Ollama on local machine, run the application and test on terminal if it is successfully installed ``` ollama --version ```.  
Step 3: Download the LLM model locally in Ollama. ``` ollama run llama2```.  
Step 4: In Langchain, to use Ollama, we need ```langchain_community``` package.   
Step 5: The streamlit client can be run using the command `streamlit run openai_tutorial.py`  

Note: It takes lots of time to get response from llama2 model based on the local machine configuration.  

## API

Using Langserve, the chatbots can be deployed as API. Langserve is integrated with FastAPI.  
* [app.py](api/app.py) file contains application to add different routes to generate poem or haiku. When locally deployed, the swagger of the api can be accessed at http://localhost/8080/docs.  
* [client.py](api/client.py) has frontend to pass topic for poem and haiku generation. For the frontend, streamlit is used. This file needs to run with command `streamlit run client.py` inside api folder.

## RAG

 For LLM models to perform better, providing context along with query is important. One way to provide context is by explicitly injecting the information along with query. Another way is to fetch relevant information and patch it up with query. 

 Using RAG interface, information from different data sources can be retrieved, like PDFs, text files, websites etc

 ### Vector Stores
 For fast and efficiently retrieval of data, the data loaded from different data sources are embedded into vector embeddings using any AI models. These embeddings are later stored in vetor stores like ChromaDB, FAISS DB, Lance DB etc. 

The basic process is: 
* **Load** data from data source,
* **Transform** the data into different chunks, 
* **Embedd** the chunks into vector embeddings and 
* **Store** in vector store.

Every vector store, indexes the embeddings for quick response. When query is passed to vector store, the db can perform similarity search and respond with most relevant information.

[rag_playground.ipynb](rag/rag_playground.ipynb) notebook contains basic tutorial of similarity search in Vector Stores.

### Retrieval Chain

Using LCEL(LangChain Expressive Language), 2 runnables (objects that contains invoke()) can be chained together into sequence. Output of the previous runnable's invoke() will be passed on as input to next runnable using pipe(). The resulting RunnableSequence is in tuen runnable i.e. invoked, streamed or further chained with other runnables. Main advantage of chaining is efficient streaming i.e. output is streamed as soon as it is available.

Retriever is an interface which provides relevant documents for the unstructured query. It is more general than vector store. i.e. Retrievers can use vector store as backbone - refer [retriever.ipynb](chain/retriever.ipynb) file. But it can also perform web serach (Exa search) and Amazon Kendra (search engine by Amazon).