<h1>A REST API BUILT WITH FLASK</h1>

<p>This is a REST Api that accepts GET, PUT, DELETE AND
POST requests. It is built on top of a database containing different
names of people and other information about them</p>

<h3>How does it work</h3>
<p><b>GET request</b>: 
The GET request enables you to get all users and their metadata
from the database</p>

<p><b>POST request</b>: This enables you to create new users and add to the database. You also get
an api_key for authentication purposes</p>

<p><b>PUT/UPDATE request</b>: To perform a put request, you need to 
authenticate yourself by providing your api key, which you got during registration</p>

<p><b>DELETE request</b>: This enables you to delete a user by providing the user's api_key.</p>

<br>
<h5>Clone the repository by running this in the terminal</h5>

```
git clone https://github.com/Omotunde2005/REST_API_with_FastApi.git
```

<br>
<br>
<h5>Run the app in the terminal via</h5> 

```
python uvicorn main:app
```
