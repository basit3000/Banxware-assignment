# Balance and Transactions API

## Intro

I have created a historical balance API for the company Banxware. The objective was to find overdraft through balances and transactions.
The implemented solution takes the two API provided by Banxware and then uses that information to generate the daily balance amount of users. I have used Django and rest framework.

1. To install python as a virtual environment use this command:
python -m venv venv 

2. This command is to activate that virtual environment:
venv\Scripts\Activate.bat

3. All of the required files will be installed with this command:
pip install -r requirements.txt

4. Open historical_balances or type in command prompt cd historical_balances

5. To run test cases we use:
python manage.py test
(There are some test cases incomplete)

6. And now we run the server by:
python manage.py runserver

7. Open localhost:8000/historical_balances or 127.0.0.1:8000/historical_balances for the main task

8. http://localhost:8000/swagger/schema/ for Swagger schema or http://localhost:8000/swagger.json for Swagger in JSON format.




Database information (not so important as it isn't used)

superuser
email : admin@admin.com
username: admin
password: admin
