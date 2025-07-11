    # ETL Project
    
    A Python-based ETL pipeline with CI/CD, developed in VS Code.
    
    ## Setup
    1. Create virtual environment: `python -m venv venv`
    2. Activate: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
    3. Install dependencies: `pip install -r requirements.txt`
    4. Run pipeline: `python run_pipeline.py`
    5. Run tests: `pytest tests/`
    
    ## Structure
    - `src/`: ETL modules
    - `tests/`: Unit tests
    - `data/`: Input/output data
    - `config/`: Configuration files
    - `logs/`: Log files