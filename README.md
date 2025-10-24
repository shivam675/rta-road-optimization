# rta-road-optimization

This repository contains code for RTA's road traffic flow optimization.

## Setup

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shivam675/rta-road-optimization.git
cd rta-road-optimization
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Usage

Run the main application:
```bash
python -m rta_road_optimization.main
```

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
# Format code with black
black src/ tests/

# Sort imports with isort
isort src/ tests/
```

### Code Quality Checks
```bash
# Linting with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/
```

## Project Structure

```
rta-road-optimization/
├── src/
│   └── rta_road_optimization/  # Main package
│       ├── __init__.py
│       └── main.py
├── tests/                       # Test files
│   ├── __init__.py
│   └── test_main.py
├── .flake8                      # Flake8 configuration
├── .gitignore                   # Git ignore rules
├── pyproject.toml              # Project configuration
├── requirements.txt            # Project dependencies
├── LICENSE                     # License file
└── README.md                   # This file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
