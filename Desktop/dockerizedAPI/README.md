# Simple API with Django REST, Nginx and Docker Compose

**Key components of the project**

+ Creating the **API** using **Python** and **Django REST**.
+ Configuring **Dockerfile**.
+ Configuring **Nginx** for **Proxy passing** and **TLS Termination**.
+ Configuring **Docker Compose** to dockerize the API.

<ins>**Make sure you have installed Docker and Docker Compose of the latest versions!**</ins>

<ins>**Also my API is based on cars, so you can make changes based on your demands!**</ins>

## Instructions

### 1. Create the API with Python and Django REST

So first of all, head to the **[API code](./carAPI/)** folder and make some changes based on your needs. Make sure to specify the required packages in **[requirements.txt](requirements.txt)** file.

Also if you don't know how to manyally specify the required packages for the project to work properly, you can use this command.
```
# Use pip3 for Mac
pip freeze > requirements.txt
```

And the most important, make sure you create .env from **[.env.example](.env.example)** file. In the .env file will be specified the variables for the **Database credentials** from the Django app, and also from the **Docker Compose** configuration file. Make sure to make the changes for your needs.


### 2. Create a Dockerfile

So before configuring Docker Compose, at first we need to configure and create our **[Docker image](Dockerfile)** with the actual API code in it. Also I wanted to mention, that I created a **[bash script](py.sh)** that contains 3 main commands that Django container will run. You can also find the image in my **[Docker Hub](https://hub.docker.com/repository/docker/dejurniy/pythonapi/general)**, if in some case you don't want to build the image by yourself.
```
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

```

### 3. Configure Nginx
So in this project we use **[Nginx](django_nginx.conf)** mainly for TLS Termination and domain name. Also I configured proxy pass, because Django already has its own WSGI server, so we can just proxy pass to that server. 
```
server {
      listen 80;
      listen [::]:80;
      server_name <your_domain>.com www.<your_domain>.com;
      return 301 https://$server_name$request_uri;

  }


server {
      listen 443 ssl;

      ssl_certificate /path/to/your/certificate;
      ssl_certificate_key /path/to/your/key;

      server_name <your_domain>.com www.<your_domain>.com;
      access_log /var/log/nginx/access.log;
      error_log /var/log/nginx/errors.log;


      location / {
          # Because we use docker compose and this is how we proxy pass to django, by the service name that you specified in docker compose config file
          proxy_pass https://django:8000; 
    	  proxy_set_header Host $host;
    	  proxy_set_header X-Real-IP $remote_addr;
    	  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    	  proxy_set_header X-Forwarded-Proto $scheme;
          index index.html index.htm;
      }
  }

```

### 4. Configure Docker Compose
