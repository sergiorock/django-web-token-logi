python manage.py migrate

echo "Running seed"
python manage.py seed

# Start server
echo "Starting server..."

python manage.py runserver 0.0.0.0:8000