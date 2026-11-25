# Olist Data Processing Project

## Project Overview
This project processes the Olist dataset using Python and Jupyter Notebooks. It includes data handling, validation, logging, configuration and file processing.

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd python-git
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Install Jupyter
```bash
pip install jupyter
```

## Running the Notebooks

1. Open the project in VS Code.
2. Install the Python and Jupyter extensions.
3. Select the virtual environment as the notebook kernel.
4. Navigate to the `tasks` folder.
5. Open the required notebook (e.g., `day14.ipynb`).
6. Run the cells in order using **Run All**.

## Project Structure

```text
python-git/
├── config.yaml
├── customers.csv
├── orders.csv
├── order_items.csv
├── manifest.json
├── requirements.txt
├── tasks/
│   ├── day11.ipynb
│   ├── day12.ipynb
│   ├── day13.ipynb
│   └── day14.ipynb
└── README.md
```

## Features
- Python-based data processing
- Configuration-driven processing
- Logging
- CSV and JSON output
- Manifest-based file tracking
- Data validation and handling

