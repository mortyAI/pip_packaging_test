1.	Installation process
	- py -3.6 -m venv .venv
	- .venv\Scripts\activate
	- python -m pip install --upgrade pip
	- pip install -r requirements.txt

how to update version
Make changes
update the version in setup.py
make sure the dist folder is empty
run the commands

- pip install .
- python setup.py sdist
- twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbos

enter these credentials

username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZwIkYzI4NzE3ZTUtNDk3ZS00ZmU0LWIyODctOGY1YjhmOWQ2OWQzAAI5eyJwZXJtaXNzaW9ucyI6IHsicHJvamVjdHMiOiBbInNpa3JpLW1sIl19LCAidmVyc2lvbiI6IDF9AAAGIMwboR4aho0VKSDtwl2QkfshLbP-tB3ZWo36vBOSi_hb

you can download the package with 
- pip install -i https://test.pypi.org/simple/ sikri-ml

if there are errors run 
python setup.py check

remember to add new files to py_modules=["some_file"], in setup