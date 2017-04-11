# University_API
Simple REST API using django-rest-framework


To register an application, go to "http://localhost:8000/o/applications/"


I registered an application named Fuad_APP with
Client id: Rr4oAn4nVAEZ2D65pvedKTyVHvmAhCuYyfREbrtu
Client secret: tKsJY4SH54djspuRqB1AYFxKA73nBjytNlgddkBd5SCCT5AV9fduPKGUW0uo0dafPw5Yr9zzItAuVmZNdWiIDLhLLkWaUdbyHVF4AQFbvIcsueplIopluIYBM1sXHwoU
So you can use that for getting a token.


To get a token you can use curl:

curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/

In the case of the application that I created (Fuad_APP) it's as following:

curl -X POST -d "grant_type=password&username=fuad&fuadfuad" -u"Rr4oAn4nVAEZ2D65pvedKTyVHvmAhCuYyfREbrtu:tKsJY4SH54djspuRqB1AYFxKA73nBjytNlgddkBd5SCCT5AV9fduPKGUW0uo0dafPw5Yr9zzItAuVmZNdWiIDLhLLkWaUdbyHVF4AQFbvIcsueplIopluIYBM1sXHwoU" http://localhost:8000/o/token/

admin_name - fuad
password - fuadfuad


After that, you will be given access and refresh tokens.
To get, for example, all universities in the database, make following curl:

curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/universities

To get a specific student:

curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/students/1
