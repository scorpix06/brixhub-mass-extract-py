# Python Brixhub mass extract 

This python script aimed to extract data of a list of peoples base on a csv.

# Installation 

## Init project
```bash 
git clone https://github.com/scorpix06/brixhub-mass-extract-py
cd ./brixhub-mass-extract-py
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```
## CSV format 

```csv 
surname,name
John,Doe
Luc,Martin
```
# Launch script
```python 
python extract.py
```
The default data dir is ./data