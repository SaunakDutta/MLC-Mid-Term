# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir notebook==6.5.2 && \
    pip install --no-cache-dir speechrecognition==3.10.1 pydub==0.25.1 pyttsx3==2.90

# Expose the port Jupyter Notebook runs on
EXPOSE 8888

# Run Jupyter Notebook when the container launches
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
