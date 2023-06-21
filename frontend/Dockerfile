FROM python:3.11

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY dashboard.py /app
COPY tests/test_dashboard.py /app/tests/test_dashboard.py

CMD streamlit run /app/dashboard.py


# docker build -t frontend_image .
# -t frontend_image tag the image frontend_image
# . use the Dockerfile in the current directory


# docker run -p 8501:8501 -v $(pwd)/static:/app/static --name frontend_container frontend_image
# -p 8080:8080 expose port 8080 to the host
# -v $(pwd)/frontend/static:/app/static mount the static folder to the container
# --name frontend_container name the container frontend_container
# frontend the image to use