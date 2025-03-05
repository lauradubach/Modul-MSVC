# file: Dockerfile

# Base python package
FROM python:3.13.2

# Working directory
WORKDIR /app

# Copy the dependencies
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

COPY . .

# Executable commands
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

