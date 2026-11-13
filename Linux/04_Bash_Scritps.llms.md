# Bash Scripts

Bash Scripts

Author

Benedict Thekkel

## Basics of Bash Scripting

### Creating a Bash Script

``` python
!touch script.sh
```

### Make the script executable:

``` python
!chmod +x script.sh
```

### Open the file in a text editor and start with the shebang (#!)

> Tells the system to use bash to execute the script:

``` python
!echo '#!/bin/bash' > script.sh
```

``` python
!cat script.sh
```

    #!/bin/bash

### Add commands to your script:

``` python
!echo 'echo "Hello, World!"' >> script.sh
```

### Run the script:

``` python
!./script.sh
```

    Hello, World!

## Variables

``` sh
#!/bin/bash
name="John"
echo "Hello, $name!"
```

## Conditionals

``` sh
#!/bin/bash
if [ "$1" -gt 10 ]; then
  echo "The number is greater than 10"
else
  echo "The number is 10 or less"
fi
```

## Loops

``` sh
#!/bin/bash
for i in {1..5}; do
  echo "Iteration $i"
done
```

## Functions

``` sh
#!/bin/bash
greet() {
  echo "Hello, $1!"
}

greet "Alice"
greet "Bob"
```

## Command Line Arguments

``` sh
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
```

### Run the script with arguments:

``` sh
./script.sh arg1 arg2
```

## Error Handling

``` sh
#!/bin/bash
set -e  # Exit on error

trap 'echo "Error occurred on line $LINENO"' ERR

# Command that might fail
cp non_existent_file.txt destination/
```

## Examples

### Update and Upgrade System

``` sh
#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get autoremove -y
```

### Example Script for Setting Up a Django Project with PostgreSQL

``` sh
#!/bin/bash

# Variables
PROJECT_NAME="myproject"
DB_NAME="mydatabase"
DB_USER="myuser"
DB_PASSWORD="mypassword"

# Update and install dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl

# Set up PostgreSQL
sudo -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
ALTER ROLE $DB_USER SET client_encoding TO 'utf8';
ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DB_USER SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

# Create a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install Django and psycopg2
pip install django psycopg2-binary

# Create Django project
django-admin startproject $PROJECT_NAME

# Configure Django settings
cd $PROJECT_NAME/$PROJECT_NAME
sed -i "s/ENGINE': 'django.db.backends.sqlite3/ENGINE': 'django.db.backends.postgresql/g" settings.py
sed -i "s/NAME': BASE_DIR / 'db.sqlite3/NAME': '$DB_NAME'/g" settings.py
sed -i "/'ENGINE': 'django.db.backends.postgresql/a \        'USER': '$DB_USER',\n        'PASSWORD': '$DB_PASSWORD',\n        'HOST': 'localhost',\n        'PORT': ''," settings.py

# Run migrations
cd ..
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Back to top
