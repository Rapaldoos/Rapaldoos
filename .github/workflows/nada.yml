name: FastAPI test

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  fastapi-run-test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.7'
    - name: Install Backend Dependencies
      run: |
        pip install pytest pytest-cov
    - name: Test with pytest
      run: pytest
