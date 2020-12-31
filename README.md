# House_Renting_Website
A House Renting Website with Vue+Django



#### 1. Environment Configuration 

+ **Django Installation**

  Install Django in Python:

  ```bash
  pip install django
  ```

  My Project uses Django Version 3.1.

  

+ **Django Project Configuration**

  Find setting files in ***backend/backend/settings.py***, modify the database information:

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'Your Data BaseName',
          'USER': 'Your User Name',
          'PASSWORD': 'Your Password',
          'HOST': '127.0.0.1', # Run locally
          'PORT': '3306',
      }
  }
  ```

+ **Node Installation**

  Install Node.js through official website https://nodejs.org/zh-cn/download/.

  My Project uses Node Version v12.18.3.

  

+ **Back-End Running**

  Enter the ***/backend*** directory where you can find a ***manage.py*** file, enter the command in the shell:

  ```bash
  python manage.py runserver
  ```

  Then, the back-end is running on local host at port 8000.

  

+ **Front-End Running**

  Enter the ***/frontend*** directory, enter the commands below in the shell:

  ```bash
  npm install
  npm run dev
  ```

  Then, the front-end is running on the local host at port 8080.



#### 2. Function and Description 

+ **Login Function**

  The whole project starts from a login interface, where I let the user enter the account and password to determine the user type, and direct them to different pages according to their user type.

+ **Tenant Search Function**

  If the user's type is a tenant, it will be directed to the user search page. On this page, users can select the rental room they need to know according to different conditions. At the same time, different types of information in the room can be displayed.

+ **Landlord Information View & Modification Function**

  If your user type is landlord, you will be directed to the landlord's personal information page. According to the user ID, the back-end will do the query and return the corresponding data.

  Now, if you want to modify your personal information, you can click on the ***Pen Icon***, then updating your ***Name*** and ***Introduction***. After the submission is completed, whether the update is successful or failed will be displayed. If successful, the corresponding information in the database will be modified.

+ **Future functions**

  Due to the lack of time, I have not made a page related to the platform manager at present. In the future, I will continue to improve our project. The manager page will manage and query a series of information about landlords, including the evaluation of landlords and the comparison and screening of their scores.