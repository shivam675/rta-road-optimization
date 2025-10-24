# Contributing to RTA Road Optimization

Thank you for your interest in contributing to this project!

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/rta-road-optimization.git
   cd rta-road-optimization
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   make install-dev
   # or
   pip install -r requirements.txt
   pip install -e .
   ```

## Making Changes

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure they follow the project's code style:
   ```bash
   make format  # Format code
   make lint    # Check code style
   ```

3. Add tests for your changes in the `tests/` directory

4. Run tests to ensure everything works:
   ```bash
   make test
   ```

5. Commit your changes:
   ```bash
   git commit -m "Add description of your changes"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request on GitHub

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep line length to maximum configured in `.flake8` and `pyproject.toml` (currently 100 characters)
- Use meaningful variable and function names

## Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting a PR
- Aim for good test coverage

## Questions?

Feel free to open an issue if you have questions or need help!
