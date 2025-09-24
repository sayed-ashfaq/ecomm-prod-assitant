import importlib.metadata

packages= ['langchain', 
           'pydantic',
           'streamlit',
           'fastapi', 
           'openai', 
           'requests', 
           'numpy', 
           'pandas', 
           'scikit-learn', 
           'tqdm', 
           'beautifulsoup4', 
           'lxml']

for package in packages:
    try:
        version = importlib.metadata.version(package)
        print(f"{package}== {version}")
    except importlib.metadata.PackageNotFoundError:
        version = "not installed"
        print(f"{package} ({version})")