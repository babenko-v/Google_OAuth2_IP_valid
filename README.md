# Google OAuth2 and IP middleware

## Technology Stack
+ Django, DRF
+ SQLite

## Instruction to run a project on local PC

The first thing you need to do is make sure you have Python and pip installed. The project is tested on Python version 3.10.

Next you need to copy the project from GitHub using the 
```
git clone
```
Then in the root folder of the project you need to create a virtual environment and activate it.
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```
The next step is to install all dependencies from the file 
```
pip install -r requirements.txt
```
You must go to [_Google Console Cloud_](https://console.cloud.google.com) website and create OAuth 2.0 Client IDs, 
after all the settings you will have ___CLIENT_SECRET___ and ___CLIENT_ID___ available to 
you. These should be placed in the .example.env file, which in turn will pass 
these variables to the settings file
```
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
```
What remains is to apply the migrations to work with the database
```bash
python manage.py migrate
```
After following all the instructions, all you have to do is follow the link http://127.0.0.1:8000/