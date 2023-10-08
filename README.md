# chatgpt-faq-bot

## To start the app:

1. Create .env file with the following keys:

   OPENAI_API_KEY=your_api_key
   APPLICATION_X_TOKEN=abc # just a sample token for the front end

2. Create env:

   python3.11 -m env venv
   source env/bin/activate
   pip install -r requirements.txt

3. Run the following command:

   uvicorn app:app --reload

### A few notes on the question answering implementation:

- The chat is based on the data provided. I have processed it into the following form:
  Question: <sample question>
  Answer: <sample answer>
  I did not include the data in the repository to avoid public disclosure

- Then I have created an index based on this data.
  It is stored in src/chat/chroma_db and is loaded from there each time the server starts
