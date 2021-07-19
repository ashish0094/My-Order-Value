
# Django API 

This project evaluates total amount for the incoming order details 
sent via post request by client.



  Requirements:
    Python3 and Django framework is used in this project.
    Install rest_framework package using
     
     pip3 install rest_framework.

Installation of the project on your system:

1. Clone this repository on to your local system. You can follow this link to know more

https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository

2. Go to shopping cart folder through terminal where manage.py file exists.


3. After sucessfully installing packages mentioned in Requirements, run this command to run a local server.
    
        python3 manage.py runserver

if you see something like- "Starting development server at http://127.0.0.1:8000/" then your local server in running.

4. I have used POSTMAN as the client to send the data to this URL -
        http://127.0.0.1:8000/totalordervalue/total_amount.

The format of the data sent is json. You can follow below example to send the test data-

        {
            "order_items": [
            {
                "name": "bread",
                "quantity": 2,
                "price": 2200
            },
            {
                "name": "butter",
                "quantity": 1,
                "price": 5900
            }],
            "distance": 1200,
            "offer": 
            {
                "type": "FLAT",
                "offerValue": 1000
            }
        }

5. Once you send the data you should get the total amount of the order you have placed.
something like this :
        
        {'order_total':14300}
    
