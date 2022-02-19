# aiocovidapi

An asynchronous COVID-19 statistics API wrapper

Somewhat usable but not fully featured. This project is still under development.

### To install the latest commit, type this in terminal: 

`pip3 install git+https://github.com/Kyuunex/aiocovidapi.git@main`

### It's recommended to install a release instead from the "releases" section

# Quick example:
```python
from aiocovidapi import COVID19APIClient

api = COVID19APIClient()

result = await api.summary() 

print(result.Date)
# 2022-02-19 17:25:00.924000+00:00

print(result.Global.TotalConfirmed)
# 421106678
```
