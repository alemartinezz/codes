# Law app 2.0 -- Udacity (Full-Stack Nanodegree)

As part of the Full-Stack Nanodegree program, I developed this web app in which you can see lawyer's cases, according to the Uruguay's legal system.

- The cases are divided by category, just as it was required for this project.
- API endpoints: The JSON request will be available for each case and category as an option.
- CRUD: All the CRUD operations are implemented with form validation and authorization check/redirect.
- Authentication and Authorization: Depending on whether or not the user is logged in, you will be able to add new items, edit them or even delete. You can perform the login with your Google account.
- Extra functionality: I also added a functions to see what percentage of cases a category occupies in the total of cases. You can see how it changes after you add or delete a case.
- Code Quality: All the python code has been formatted with pyCodeStyle according to the PEP8 requirements, as well as the HTML code.
- Responsive: The app was made thank to [Argon Dashboard Template](https://www.creative-tim.com/product/argon-dashboard) so it is made with Bootstrap 4 and fully responsive.
- Documentation: The instructions for running this project in your PC will be available in the repo. 

### Technologies used:
- Vagrant (CentOS 7)
- Python 3.6
- Flask Framework
- SQLAlchemy (ORM)
- PostgreSQL
- BootStrap 4 (Argon Dashboard template)
- JavaScript
- Google OAuth

## Requisites

### 1. Install Required software
For running this project in your local machine, you will need to have python3.6 installed in your system/virtual machine, as well as postgresql and flask.

You can download the VM provided by udacity, an Ubuntu virtual machine already provided with all the software needed. (All this is done by git interface).
[Udacity Fullstack Nanodegree Ubuntu VM](https://github.com/udacity/fullstack-nanodegree-vm)

For this project you will need PYTHON 3.6 whether you are using ubuntu or centos.
```
sudo apt-get install python3.6
```

If you are using CentOS, install with the following commands:
```
sudo yum install https://centos7.iuscommunity.org/ius-release.rmp -y
sudo yum install python36u python36u-libs python36u-devel python36u-pip -y
sudo pip3.6 install --upgrade pip
```

Install PostgreSQL and follow the commands provided in the web for your system.
```
postgresql.org/download
```

Install flask (ignore this if you are using udacity vm)
```
sudo pip3.6 install -U flask -y

sudo pip3.6 install oauth2client redis passlib flask-httpauth -y

sudo pip3.6 install sqlalchemy requests psycopg2-binary bleach -y
```

### 2. Populate the Database

Then create the user and database manually:
```
sudo su postgresql-c 'createuser -dRS vagrant'

psql

CREATE DATABASE law;
```

Populate the database: Download this project and locate in your VM by cd command. Then run the `orm_setup.py` file and `database_setup.py` file. Be careful and do not do this twice because the records will be duplicated.
```
python3.6 orm_setup.py
```
```
python3.6 database_setup.py
```

Then check the password in the string of connection in the `run.py` and `orm_setup` file.

### 3. Finally, get the credentials from the google api 
- This application will require an OAuth 2.0 client ID from the Google API dashboard.
- Log into Google.
- Navigate to the [Google Cloud Platform APIs credentials page](https://console.cloud.google.com/apis/credentials).
- Click `Create credentials` and follow the prompts.
  - OAuth Client ID
  - Web application
  - Set a name. I set mine as "law-app-udacity".
  - Restrictions: Add `http://localhost:8000` to the Authorized JavaScript origins and Redirects.
- Download JSON credentials and save in application directory as *client_secrets.json*.

### 4. Running the project

After all the previous steps, you are ready to run the app. Move to the project folder and run the `run.py` file with the commands.

```
cd /path/project/

python3.6 run.py
```

Now is ready to use. (The run.py file was configured to run on port 8000). You can change it by editing the `run.py` file.
```
http://localhost:8000
```

## Author

* [Alejandro Martinez](https://github.com/alemartinezz)

## License

[MIT License](https://opensource.org/licenses/MIT) for more details.