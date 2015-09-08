Qiita API V2 wrapper for Python
===========

Description
--------------------
Qiita web api wrapper.

Detail is https://qiita.com/api/v2/docs.

installation
--------------------
```
pip install qiita-api-wrapper
```

preparation
------------------
You must register qiita and get access_token from [this page](https://qiita.com/settings/applications).

usage
-------------------
```python
from qiita import Qiita

qiita = Qiita(<your access_token>)
qiita.get_items()
```
