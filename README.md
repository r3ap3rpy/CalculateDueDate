### Welcome

This is a repo for the homework assignment from emarsys.

In order to install the module naviagate to the folder and install with the following.

``` bash
cd CalculateDueDate
python setup.py install
```

Example usage:

``` python
from CalculateDueDate import *
>>> CalculateDueDate(datetime(2021, 12, 3, 13, 10, 55),16)
datetime.datetime(2021, 12, 7, 13, 10, 56)
```


In order to run the tests do the following!

``` bash 
pip install pytest
pytest -vvv
```