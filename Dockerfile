# FROM python:3-alpine
FROM python:3.9.16-bullseye

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN python -m venv myenv

RUN . myenv/bin/activate

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 8501
CMD [ "streamlit", "run","app.py"]