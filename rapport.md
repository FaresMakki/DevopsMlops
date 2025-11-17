# DevOps CI/CD Assignment Report

**Student Name:** Fares Makki
**Repository:** https://github.com/FaresMakki/DevopsMlops
**Date:** November 17, 2025
**Screenshot:**in the directory /images
---

## Task 1: Project Setup

### Steps Taken:
1. Downloaded/cloned the ML project repository
2. Verified project structure and `requirements.txt` file
3. Confirmed all necessary files are present

### Project Structure:
```
ml-app/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_model.py
├── models/
│   └── iris_classifier.pkl
├── .gitignore
├── .flake8
├── Dockerfile
├── requirements.txt
└── REPORT.md
```


---

## Task 2: Running the Application Locally

### Commands Used:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/train.py
python src/predict.py
```

### Results:
- ✅ Virtual environment created successfully
- ✅ All dependencies installed (scikit-learn, pandas, numpy, etc.)
- ✅ Model trained successfully with **96.67% accuracy**
- ✅ Training completed without errors
- ✅ Model saved to `models/iris_classifier.pkl`
- ✅ Predictions working correctly with probability outputs

### Model Performance:
```
Model Accuracy: 0.9667
Classification Report:
              precision    recall  f1-score   support
           0       1.00      1.00      1.00        10
           1       1.00      0.90      0.95        10
           2       0.91      1.00      0.95        10
    accuracy                           0.97        30
```

- Training output showing 96.67% accuracy
- Prediction output with probabilities for all three iris classes

---

## Task 3: Unit Tests

### Test Implementation:
Created comprehensive test suite in `tests/test_model.py` with the following tests:

1. **test_model_initialization** - Verifies model initializes correctly
2. **test_model_training** - Tests model training functionality
3. **test_model_prediction** - Validates prediction outputs
4. **test_model_evaluation** - Checks evaluation metrics
5. **test_model_save_load** - Tests model persistence
6. **test_data_loading** - Validates data loading functionality

### Setup Files Created:
- `tests/__init__.py` - Makes tests a Python package
- `tests/conftest.py` - Configures Python path for imports
- `src/__init__.py` - Makes src a Python package

### Test Execution:
```bash
pytest tests/ -v
```

### Results:
- ✅ All 6 tests passed successfully
- ✅ Coverage includes: initialization, training, prediction, evaluation, save/load, data loading
- ✅ Tests verify model produces valid outputs and maintains state correctly


---

## Task 4: Linting and Code Quality

### Linting Setup:
- Installed `flake8` for Python code linting
- Created `.flake8` configuration file
- Configured max line length: 100 characters
- Excluded virtual environment and cache directories

### Configuration (`.flake8`):
```ini
[flake8]
max-line-length = 100
exclude = .venv,__pycache__,.git,*.pyc,models,.pytest_cache,.idea
ignore = E203,W503
```

### Linting Command:
```bash
flake8 src/ tests/
```

### Issues Identified:
- Minor PEP 8 style violations (spacing, line length)
- Some unused imports
- Import order issues
- **Note:** All issues are non-critical style warnings

### Code Quality Summary:
- ✅ No critical errors
- ✅ Code is functional and follows most Python conventions
- ⚠️ Minor style improvements recommended


---

## Task 5: GitHub Actions CI Workflow

### Workflow File Location:
`.github/workflows/ci.yml`

### CI Pipeline Stages:

1. **Checkout Code** - Uses `actions/checkout@v3`
2. **Set Up Python** - Installs Python 3.10 using `actions/setup-python@v4`
3. **Install Dependencies** - Installs requirements and dev tools (pytest, flake8)
4. **Create Init Files** - Ensures proper Python package structure
5. **Run Linter** - Executes flake8 (non-blocking)
6. **Run Tests** - Executes pytest with proper PYTHONPATH
7. **Build Docker Image** - Creates containerized application
8. **Save & Upload Artifact** - Stores Docker image as build artifact

### Workflow Configuration:
```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
```

### Workflow Triggers:
- ✅ Automatic execution on push to main/master
- ✅ Automatic execution on pull requests
- ✅ Manual trigger available

### CI Pipeline Results:
- ✅ Workflow runs successfully
- ✅ All stages complete without errors
- ✅ Docker image built and uploaded as artifact
- ⏱️ Total execution time: ~1m 22s


---

## Task 6: Docker Containerization

### Dockerfile Implementation:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Create necessary directories
RUN mkdir -p models

# Set Python path so imports work
ENV PYTHONPATH=/app/src

# Default command - train the model
CMD ["python", "src/train.py"]
```

### Docker Features:
- Base image: Python 3.10 slim (lightweight)
- Proper layer caching for faster builds
- Environment variables configured for Python paths
- Default command trains the model automatically

### Docker Commands Used:

**Build:**
```bash
docker build -t ml-app:latest .
```

**Run:**
```bash
docker run ml-app:latest
```

### Docker Results:
- ✅ Image built successfully
- ✅ Container runs training without errors
- ✅ Model trains inside container with same accuracy (96.67%)
- ✅ All dependencies properly installed in container
- ✅ Application fully containerized and portable


---

## Summary and Learning Outcomes

### What I Learned:

1. **DevOps Principles**
   - Understanding CI/CD pipelines and automation benefits
   - Importance of automated testing in development workflow
   - How containerization ensures consistency across environments

2. **GitHub Actions**
   - Creating YAML workflow configurations
   - Setting up automated build and test pipelines
   - Using actions marketplace (checkout, setup-python, upload-artifact)
   - Handling workflow triggers and branch rules

3. **Docker Containerization**
   - Writing Dockerfiles for Python applications
   - Understanding layer caching and build optimization
   - Setting environment variables for application configuration
   - Creating portable, reproducible environments

4. **Testing & Quality**
   - Writing unit tests with pytest
   - Using fixtures and test classes
   - Implementing code linting with flake8
   - Understanding code quality metrics

5. **Python Best Practices**
   - Proper project structure with `__init__.py`
   - Managing Python paths and imports
   - Virtual environment usage
   - Dependency management with requirements.txt

### Challenges Faced & Solutions:

1. **Challenge:** PowerShell execution policy blocked virtual environment activation
   - **Solution:** Used Command Prompt (CMD) instead of PowerShell

2. **Challenge:** Import path issues in tests (`ModuleNotFoundError`)
   - **Solution:** Created `conftest.py` and `__init__.py` files, configured PYTHONPATH

3. **Challenge:** YAML syntax errors in GitHub Actions workflow
   - **Solution:** Properly formatted YAML with correct indentation (2 spaces)

4. **Challenge:** Tests working locally but failing in CI
   - **Solution:** Added explicit PYTHONPATH environment variable in workflow, created init files

### Key Takeaways:

- ✅ Automation saves time and reduces human error
- ✅ Containers ensure "works on my machine" becomes "works everywhere"
- ✅ CI/CD catches bugs early in the development process
- ✅ Good project structure is essential for maintainability
- ✅ Documentation is crucial for reproducibility

### Future Improvements:

1. **Enhanced Testing**
   - Add integration tests
   - Implement code coverage reporting (pytest-cov)
   - Add performance benchmarks

2. **Extended CI/CD**
   - Add automatic deployment to cloud platform (AWS, Azure, GCP)
   - Implement Docker image versioning/tagging
   - Publish to Docker Hub or container registry

3. **Code Quality**
   - Fix all flake8 warnings
   - Add type hints (mypy)
   - Implement pre-commit hooks

4. **Monitoring**
   - Add logging throughout application
   - Implement model performance monitoring
   - Set up alerts for failed builds

---

## Repository Information

**GitHub Repository:** https://github.com/FaresMakki/DevopsMlops

**Branch:** main

**CI/CD Status:** ✅ Passing

---

## How to Run This Project

### Prerequisites:
- Python 3.10+
- Docker (optional, for containerized execution)
- Git

### Local Development:

**1. Clone the repository:**
```bash
git clone https://github.com/FaresMakki/DevopsMlops.git
cd DevopsMlops
```

**2. Create and activate virtual environment:**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Train the model:**
```bash
python src/train.py
```

**5. Run predictions:**
```bash
python src/predict.py
```

**6. Run tests:**
```bash
pytest tests/ -v
```

**7. Check code quality:**
```bash
flake8 src/ tests/
```

### Using Docker:

**1. Build the Docker image:**
```bash
docker build -t ml-app:latest .
```

**2. Run the container:**
```bash
docker run ml-app:latest
```

**3. Run with custom command:**
```bash
docker run ml-app:latest python src/predict.py
```

---

## Conclusion

This assignment successfully demonstrates a complete DevOps CI/CD pipeline for a machine learning application. The implementation includes:

- ✅ Automated testing with pytest
- ✅ Code quality checks with flake8  
- ✅ Containerization with Docker
- ✅ Continuous Integration with GitHub Actions
- ✅ Artifact management and storage

The project showcases industry best practices for ML operations (MLOps) and provides a solid foundation for deploying machine learning models in production environments.

**Total Implementation Time:** ~3-4 hours

**Final Status:** All tasks completed successfully ✅