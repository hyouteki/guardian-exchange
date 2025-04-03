### Set up Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Copy environment variables
Since the `.env` file is in a private repository, manually copy its contents from <https://github.com/Talkative-Banana/Guardian_Exchange_Env/blob/main/.env> into `.env` file.

> TODO: Automate this in the future using: 
> ```bash
> wget https://raw.githubusercontent.com/Talkative-Banana/Guardian_Exchange_Env/refs/heads/main/.env?token=<token>
> ```

### Run migrations
```bash
python manage.py migrate
```
