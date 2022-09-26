# self-driving

## Setup

``` bash
# Install Python dependencies
sudo pip3 install -r requirements.txt

# Install Linux dependencies
chmod +x packages.bash # Make script executable
sudo ./packages.bash

# Run Server (http://localhost:8080)
flask run

# Run Server on all connections
flask run --host=0.0.0.0


gunicorn --bind 0.0.0.0:8080 wsgi:app
```