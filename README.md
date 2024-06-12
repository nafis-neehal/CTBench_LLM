# CTBench_LLM
This repository contains the CT-Repo and CT-Pub datasets and demo codes to run the benchmark. 

# Steps to run 
1. Create a separate virtual environment in Python3. Let's name it 'my_venv'.
```
python3 -m venv my_venv
```
Then activate the virtual environment - 
```
source my_venv/bin/activate
```
2. Install the requirements from requirements.txt
```
pip3 install -r requirements.txt 
```
3. Run the demo_scripts.ipynb notebook and explore the examples.

# Data (Version 1.0)
1. [CT-Pub Dataset (including 3 examples for three-shot setting) - 103 Trials](data/CT-Pub-With-Examples.csv)
2. [CT-Repo Dataset (including 3 examples for three-shot setting) without any pre-processing - 1798 Trials](data/CT-Repo-With-Examples-Full-Version.csv)
3. [CT-Repo Dataset (including 3 examples for three-shot setting) after pre-processing - 1693 Trials](data/CT-Repo-With-Examples-Processed-Version.csv)
