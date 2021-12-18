# TestProject

Project launch:

1) Clone repo `git clone https://github.com/Praezid/TestProject`
2) Go to the project folder `cd TestProject` 
3) Install the virtual enviroment `virtualenv env`
4) Run the virtual enviroment `.\env\Scripts\activate`
5) Update pip `python -m pip install --upgrade pip`
6) Install in the virtual enviroment the dependencies for the project `python -m pip install --no-cache-dir -r requirements.txt`
7) Fill in the data of the model 'Product' `python manage.py loaddata db.json`
8) Start the local server `python manage.py runserver`