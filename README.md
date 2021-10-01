# Django-Online-Business-Database-Project

* this project is still in progress 

Overview of Website 
-------------------------
This website serves as an online database (hosted via SQLLite) for fictional businesses in the area to store contact information (name, email, phone number, etc.) for fictional customers. The information in the database is entirely fake. Businesses have the option of sending a daily promotional email (made possible via the Google Email client), to everyone in the database. Businesses can have the option to further customize this by being able to pre-add email templates and choosing them from a drop down list when sending the daily email. 

Brief Tutorial of Website Functions
-------------------------

Adding Customerss
------------------ 

1. Go to "Manage Customers & Email" and select "Create New Customer", a form to add the customer data with required fields will be generated.  
2. If the addition is succesful, the website will redirect to the main database view to show the new customer. 

Managing The Database
---------------
Businesses also have options to amend the database such as deleting, adding, or editing customers and their information. Click on the appropriate fields in "Manage Customers & Email > Manage Customers" to execute the required action.  

- Selecting which customer to manage can be done via the provided search field on each page. 

Sending Emails 
------------
Businesses have the option of sending a daily promotional email (made possible via the Google Email client), to everyone in the database. A status of either "S" (Sent) or "U" (Unsent) will be reflected in the "Email Status" column on the main database page. Business can have the option to further customize this by being able to pre-add email templates and choosing them from a drop down list when sending the daily email. 

- Sending individual emails to customers on demand is also possible, and if choosing the "mass send" option to send the email in the case a new customer is entered after the daily email has been sent, previous customers will not recieve another email in order to prevent spamming. This is done via a Python loop to check if the daily email has already been sent. Though, this can be oviredden by just sending an email to that individual customer you wish to send a second email to. 

-------------

Inquiries: kasiditpaul@gmail.com
 
