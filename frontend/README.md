# ClaudeUI

ClaudeUI is a chat interface for interacting with Claude, an AI assistant created by Anthropic. This project uses Python with Flask for the backend and React with Vite for the frontend.

## Project Structure

```
claudeui/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Features

- Real-time chat interface
- Markdown rendering for Claude's responses
- Ability to delete chat history
- Responsive design

## Prerequisites

- Python (v3.7 or later)
- Node.js (v14 or later)
- npm or yarn

## Setup and Installation

### Backend

1. Navigate to the backend directory:

   ```
   cd backend
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```
   python app.py
   ```

The backend will be available at `http://localhost:5000`.

### Frontend

1. Navigate to the frontend directory:

   ```
   cd frontend
   ```

2. Install dependencies:

   ```
   npm install
   ```

   or

   ```
   yarn install
   ```

3. Start the development server:
   ```
   npm run dev
   ```
   or
   ```
   yarn dev
   ```

The frontend will be available at `http://localhost:5173`.

## Usage

1. Ensure the backend server is running.
2. Start the frontend development server.
3. Open your browser and go to `http://localhost:5173`.
4. Start chatting with Claude by typing your message and pressing Enter or clicking the Send button.
5. Claude's responses will be displayed with markdown formatting.
6. To clear the chat history, click the "Delete Chat History" button.

## API Endpoints

- `/api/chat` (POST): Send a message to Claude and receive a response.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [React](https://reactjs.org/)
- [Vite](https://vitejs.dev/)
- [Anthropic](https://www.anthropic.com/) for creating Claude
