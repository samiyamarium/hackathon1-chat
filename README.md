# Docusaurus Chatbot

This project integrates a Gemini-powered RAG chatbot into a Docusaurus website.

## Setup and Installation

You have two main components to set up: the **Docusaurus frontend** and the **Python backend**.

### 1. Docusaurus Frontend

The frontend is a Docusaurus website.

**A. Install Dependencies:**
Navigate to the `docusaurus-chatbot` directory and install the necessary npm packages.

```bash
cd docusaurus-chatbot
npm install
```

### 2. Python Backend

The backend is a Python-based chatbot module with a Flask API.

**A. Install Dependencies:**
Navigate to the `chatbot-module` directory and install the required Python packages.

```bash
cd ../chatbot-module 
# (If you are in the docusaurus-chatbot directory)

pip install -r requirements.txt
```

**B. Set up the Environment File:**
   - In the `chatbot-module` directory, you will find a file named `.env`.
   - Open this file and replace `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key.

   ```
   GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   ```

**C. Ingest the Knowledge Base:**
Before you can start chatting, you need to create the vector store from your documentation.

Run the `ingest.py` script from within the `chatbot-module` directory:

```bash
python ingest.py
```

**Important Note:** The free tier of the Gemini API is very restrictive. If you encounter a `429 ResourceExhausted` error, you may need to upgrade to a paid plan or run the script on a smaller subset of your documents.

## Running the Chatbot

To run the chatbot, you need to have **both** the backend API and the frontend Docusaurus server running simultaneously.

### Step 1: Run the Backend API

Open a terminal, navigate to the `chatbot-module` directory, and run the Flask server:

```bash
cd chatbot-module
python api/server.py
```

The API server will start on `http://localhost:5001`.

### Step 2: Run the Docusaurus Frontend

Open a **second** terminal, navigate to the `docusaurus-chatbot` directory, and start the Docusaurus development server:

```bash
cd docusaurus-chatbot
npm run start
```

The Docusaurus site will open in your browser at `http://localhost:3000`.

You should now see your Docusaurus site with a chat button in the bottom-right corner. You can click it to start interacting with your chatbot.
