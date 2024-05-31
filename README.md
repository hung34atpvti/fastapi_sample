# Example-fastapi
Example of FastAPI CRUD with postgres, OAuth2 with Password (and hashing), Bearer with JWT tokens

## Getting Started
1. Install dependencies
```zsh
pip install -r requirements.txt
```
2. Config

- Base on .env.example, create your .env and set up your database
- Database: Postgres
- Example: 
```sh
cp .env.example .env
```
 
3. Start Server
```zsh
python main.py
```
4. Open local API docs [http://localhost:8000/docs](http://localhost:8000/docs)