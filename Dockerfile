FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

# Create the SQLite database file if it doesn't exist
# In a real production setup, you wouldn't use SQLite in the container like this usually,
# or you would mount a volume.
# For this practice, we will let the app create it on startup via SQLAlchemy.

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
