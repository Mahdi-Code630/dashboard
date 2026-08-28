# How to Run

First, you need to install the dependencies. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

Then, run the following command to export the environment variables in the main repo directory:

```bash
source .env
```

Run the following command to add the current directory to the Python path:

```bash
export PYTHONPATH=${PWD}
```

Build Django migrations by running the following commands:

```bash
python src/manage.py makemigrations db
python src/manage.py migrate
```

Then, you can run the dashboard by running the following command:

```bash
streamlit run src/app.py
```