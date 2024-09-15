# Variables
VENV = venv
REQUIREMENTS = requirements.txt
PYTHON = python3
DB_CONTAINER_NAME = estacio_python
DB_PORT = 5432
DB_USER = postgres
DB_PASSWORD = postgres
DB_NAME = estacio_python

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

# Install dependencies and set up the database
install: venv
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r $(REQUIREMENTS)
	@echo "Dependencies installed."
	make db_setup

# Set up the PostgreSQL database using Docker
db_setup:
	@echo "Setting up PostgreSQL database container..."
	docker run --name $(DB_CONTAINER_NAME) \
		-e POSTGRES_USER=$(DB_USER) \
		-e POSTGRES_PASSWORD=$(DB_PASSWORD) \
		-e POSTGRES_DB=$(DB_NAME) \
		-p $(DB_PORT):5432 \
		-d postgres:latest
	@echo "PostgreSQL container started."

# Remove the database container
db_remove:
	@echo "Stopping and removing the database container..."
	docker stop $(DB_CONTAINER_NAME)
	docker rm $(DB_CONTAINER_NAME)
	@echo "Database container removed."

# Clean up environment
clean:
	rm -rf $(VENV)
	@echo "Virtual environment removed."
	make db_remove

# Activate the virtual environment (reminder only)
activate:
	@echo "To activate the virtual environment, run: source $(VENV)/bin/activate"

# Deactivate the virtual environment (reminder only)
deactivate:
	@echo "To deactivate the virtual environment, run: deactivate"

