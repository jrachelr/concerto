FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files in your service's directory
# Modify these instructions to do that
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY another_file.py another_file.py

# Copy all of the subdirectories in your service's directory
# Modify these instructions to do that
COPY subdirectory_1 subdirectory_1
COPY subdirectory_2 subdirectory_2

RUN pip install -r requirements.txt
CMD uvicorn main:app --reload --host 0.0.0.0 --port $PORT
