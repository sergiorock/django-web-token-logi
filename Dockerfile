FROM python:3.9-bullseye

WORKDIR /usr/src/app/web_token_auth

# Expose the Django port
EXPOSE 8000

# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip install --upgrade pip 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./.docker/entrypoint.sh /docker/entrypoint.sh
# Dar permisos de ejecución al script
RUN chmod +x /docker/entrypoint.sh

# Configurar el script como entrypoint
ENTRYPOINT ["/docker/entrypoint.sh"]


