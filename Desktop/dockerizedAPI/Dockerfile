FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt /app/
COPY py.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/py.sh
RUN python -m pip install --upgrade pip; pip install -r /app/requirements.txt
RUN pip install mysqlclient

# Copy the project files into the container
COPY ./carAPI /app

# Set the working directory
WORKDIR /app

# Expose the port 8000
EXPOSE 8000

# Run the script as the default CMD
CMD ["/usr/local/bin/py.sh"]
