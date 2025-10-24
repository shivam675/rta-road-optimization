# Quick Setup Guide

This guide will help you get started with the RTA Road Optimization project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- git

## Quick Start

```bash
# Clone the repository
git clone https://github.com/shivam675/rta-road-optimization.git
cd rta-road-optimization

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
make install-dev
# or manually:
pip install -r requirements.txt
pip install -e .
```

## Common Commands

```bash
make help         # Show all available commands
make test         # Run tests
make lint         # Check code style
make format       # Auto-format code
make clean        # Clean build artifacts
```

## Project Structure

```
rta-road-optimization/
├── src/rta_road_optimization/  # Main application code
├── tests/                       # Test files
├── pyproject.toml              # Project configuration
├── requirements.txt            # Dependencies
├── Makefile                    # Common commands
└── README.md                   # Full documentation
```

## Next Steps

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
2. Check [README.md](README.md) for detailed documentation
3. Start coding!

## Getting Help

- Open an issue on GitHub for bugs or feature requests
- Check existing issues for known problems or questions
