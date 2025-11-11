# Contributing to HR Suite

First off, thank you for considering contributing to HR Suite! It's people like you that make HR Suite such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples**
* **Describe the behavior you observed**
* **Explain which behavior you expected to see instead**
* **Include screenshots if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and explain the behavior you expected**
* **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code lints
5. Issue that pull request!

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/hr_suite.git
cd hr_suite

# Install dependencies
pip install -e .

# Install to a test site
bench --site test.local install-app hr_suite
```

## Coding Style

* Follow PEP 8 for Python code
* Use meaningful variable and function names
* Add comments for complex logic
* Write docstrings for all functions and classes

### Python Style Guide

```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
    # Your code here
    pass
```

### JavaScript Style Guide

```javascript
function functionName(param1, param2) {
    // Use camelCase for function names
    // Add comments for complex logic
    return result;
}
```

## Testing

Before submitting a pull request, make sure all tests pass:

```bash
bench --site test.local run-tests --app hr_suite
```

## Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Example:
```
Add employee onboarding workflow

- Implement automated email sending
- Add welcome email template
- Update documentation

Fixes #123
```

## Documentation

When adding new features, please update the documentation:

* Update README.md if needed
* Add docstrings to new functions
* Update user documentation if applicable

## Additional Notes

### Issue and Pull Request Labels

* `bug` - Something isn't working
* `enhancement` - New feature or request
* `documentation` - Improvements or additions to documentation
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed

## Questions?

Feel free to open an issue with your question or contact the maintainers.

Thank you for contributing! 🚀