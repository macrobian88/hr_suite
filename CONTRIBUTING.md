# Contributing to HR Suite

Thank you for considering contributing to HR Suite! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/macrobian88/hr_suite/issues)
2. If not, create a new issue using the bug report template
3. Provide as much detail as possible:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment details
   - Screenshots if applicable

### Suggesting Features

1. Check if the feature has already been requested
2. Create a new issue using the feature request template
3. Explain:
   - What problem does it solve?
   - How should it work?
   - Any alternative solutions you've considered

### Code Contributions

#### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/hr_suite.git
cd hr_suite

# Add upstream remote
git remote add upstream https://github.com/macrobian88/hr_suite.git

# Create a new branch
git checkout -b feature/your-feature-name
```

#### Development Workflow

1. **Make your changes**
   - Follow Frappe coding standards
   - Write clean, readable code
   - Add comments where necessary

2. **Test your changes**
   ```bash
   # Install in a test site
   bench --site test-site install-app hr_suite
   
   # Test thoroughly
   # - Manual testing
   # - Check for errors in console
   # - Verify all features work
   ```

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add amazing new feature"
   ```

   Use conventional commit messages:
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `style:` - Code style changes (formatting, etc.)
   - `refactor:` - Code refactoring
   - `test:` - Adding tests
   - `chore:` - Maintenance tasks

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Wait for review

#### Code Style Guidelines

**Python:**
- Follow PEP 8
- Use descriptive variable names
- Add docstrings to functions
- Maximum line length: 100 characters

```python
def send_welcome_email(employee):
    """
    Send welcome email to new employee
    
    Args:
        employee (Document): Employee document
    """
    # Implementation
```

**JavaScript:**
- Use ES6+ syntax
- Use camelCase for variables
- Add JSDoc comments

```javascript
/**
 * Get HR statistics
 * @returns {Object} HR stats object
 */
function getHRStats() {
    // Implementation
}
```

#### Documentation

- Update README.md if you add new features
- Add inline comments for complex logic
- Update docstrings
- Add examples where helpful

### Pull Request Process

1. **Before submitting:**
   - Test your changes thoroughly
   - Update documentation
   - Check for any console errors
   - Ensure code follows style guidelines

2. **PR Description should include:**
   - What changes were made
   - Why the changes were made
   - How to test the changes
   - Screenshots (if UI changes)
   - Related issue numbers

3. **After submitting:**
   - Respond to review comments
   - Make requested changes
   - Keep the PR updated with main branch

### Testing

#### Manual Testing Checklist

- [ ] Installation works correctly
- [ ] All default data is created
- [ ] Employee creation triggers automation
- [ ] Leave allocation works
- [ ] Email templates function
- [ ] Scheduled tasks run without errors
- [ ] No console errors
- [ ] All links work
- [ ] Responsive design (if UI changes)

#### Testing in Different Scenarios

- Test with fresh installation
- Test with existing ERPNext installation
- Test with different Frappe/ERPNext versions
- Test with different browsers

### Documentation Contributions

Documentation improvements are always welcome!

- Fix typos
- Improve clarity
- Add examples
- Translate to other languages
- Create tutorials
- Record video guides

### Community Guidelines

- Be respectful and inclusive
- Help others when you can
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)

### Getting Help

- **Questions:** Use [GitHub Discussions](https://github.com/macrobian88/hr_suite/discussions)
- **Bugs:** Open an [Issue](https://github.com/macrobian88/hr_suite/issues)
- **Chat:** Join our community chat (link TBD)

## Recognition

Contributors will be:
- Listed in the CONTRIBUTORS.md file
- Mentioned in release notes
- Credited in the documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to HR Suite! 🎉
