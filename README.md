# RESTful-Server

## To Get Started

```
$ git clone https://github.com/YiiChoong/RESTful-Server.git
$ cd cd RESTful-Server/restAPI
$ py -m venv venv
$ ./venv/Scripts/activate
$ pip install -r requirements.txt
$ cd myproject
$ py manage.py createsuperuser
$ py manage.py runserver
```

### Copy Server Link
http://127.0.0.1:8000/

### Download Postman
https://www.postman.com/downloads/?utm_source=postman-home

- Open a new workspace and paste the server link 
![image](https://user-images.githubusercontent.com/72157216/209271203-a6c5e61a-7f7d-4e4e-8eb5-f142018daa83.png)

- Go to **Body** -> change method to **POST** -> select **form-data** -> enter username and password
![image](https://user-images.githubusercontent.com/72157216/209272382-92f9abaf-1f4e-4959-97a4-9b5ea403cb6e.png)

- Set Authorazation type to **OAuth 2.0**
![image](https://user-images.githubusercontent.com/72157216/209272788-b1089853-2fe3-41ba-95c0-292814e52ea8.png)

- Enter the token to the **Header**
![image](https://user-images.githubusercontent.com/72157216/209272943-62bf3ef5-2f90-4be3-a0f7-5cd508af0c64.png)

### Path: **/cars** &emsp; Method: **GET**
![image](https://user-images.githubusercontent.com/72157216/209277172-4a52a7f0-1e04-4e3a-9045-35aada27f96a.png)

### Path: **/cars/:id** &emsp; Method: **GET**
![image](https://user-images.githubusercontent.com/72157216/209277246-8c1053fd-0739-4aeb-8e4b-7e5b47ba424f.png)

### Path: **/cars/:id** &emsp; Method: **PUT**
- Go to **Body** -> **raw** -> change to **JSON** -> paste the object, make changes and **Send**
![image](https://user-images.githubusercontent.com/72157216/209277350-528b5233-1087-4779-896e-54cc74e42f8c.png)

### Path: **/cars/:id** &emsp; Method: **DELETE**
![image](https://user-images.githubusercontent.com/72157216/209401503-4d8d7114-2477-4dc4-8f12-99d074644b1f.png)

