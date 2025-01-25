# Flask OpenAI API

This is a simple Flask application that provides an endpoint to interact with OpenAI's API.

## Project Structure

```
flask_openai_api/
├── app.py             # Flask app main script
├── .env.example       # Example file for environment variables
├── .gitignore         # Defines files to be ignored by Git
├── requirements.txt   # Python package dependencies
└── README.md          # Project documentation
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-repo/flask_openai_api.git
cd flask_openai_api
```

### 2. Create and activate a virtual environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env  # On Windows: copy .env.example .env
   ```
2. Open `.env` and set your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

### 5. Run the application
```bash
python app.py
```

You should see output like this:
```
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

### 6. Test the API endpoint

#### Using `curl`
```bash
curl -X POST http://127.0.0.1:5000/api/generate \
-H "Content-Type: application/json" \
-d '{"prompt": "Hello, how are you?"}'
```

#### Using Postman
1. Set the method to `POST`.
2. Set the URL to `http://127.0.0.1:5000/api/generate`.
3. Add the following JSON in the body:
   ```json
   {
     "prompt": "Hello, how are you?"
   }
   ```
4. Send the request.

#### Example Response
```json
{
  "response": "I'm doing well, thank you for asking!"
}
```

## File Descriptions

- `app.py`: Main application script that handles the API endpoint.
- `.env.example`: Template for environment variables.
- `.gitignore`: Specifies files to be ignored by Git.
- `requirements.txt`: Lists required Python packages.
- `README.md`: Documentation for the project.

## Notes

- Ensure your OpenAI API key is valid and has the necessary permissions.
- Use a virtual environment to avoid dependency conflicts.
- For production deployment, consider using a WSGI server like Gunicorn or deploying to a cloud platform.

## License

MIT
