<b> Bucketlist Application </b>

This is a web application created using python, java script, HTML, css and bootstrap. It is an application that consumes flaskApi to do simple fuctionalities like creating a bucketlist, editing, deleting and adding items to it. 

<b> Basic fuctionalities </b>

   User Login/ Registration.
   
   User creating bucketlist.
   
   User can view the bucketlist created immediately after creating it.
   
   User adding items to the specific bucketlist.
   
   User editing/deleting the bucketlist.
   
   User can edit and delete the items they added to a particular bucketlist.
   
   User can search a specific bucketlist.

<b> Installation </b>

1. Create a folder.

2. Clone the repository into the given folder: 
   https://github.com/johnmusiu/bucketlist.git

3. Navigate to the project folder: 
   Bucketlist

4. Install project dependencies in your virtual environment.
    pip install -r requirements.txt
    
5. Set up project development. Run db migrations.
    python manage.py db init python manage.py db migrate python manage.py db upgrade 
6. Run the server.
    python manage.py runserver
