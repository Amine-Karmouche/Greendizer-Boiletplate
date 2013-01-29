Welcome to Greendizer Boilerplate

#Contents
This is a Django starter project using OAuth for authentication.
This boilerplate enables you to start your first django-powered Greendizer application.
The Greendizer library is used to:
	Display your settings
	List all the invoices you received as a buyer
	
Greendizer is a new kind of invoicing system.
It turns the invoices sent with it to an extremely rich source of data for business intelligence and process automation.

Check out [the Greendizer website](https://www.greendizer.com/) for more information.

#About authentication
The OAuth flow used is the "Authorization Code Grant" for client/server applications
In order to perform authentication, please modify the credentials by the ones provided to you upon registration of your application; namely:
	client_id
	client_secret
	email

#Database setup
Please modify your database name and path in the settings.py file

#About the Library
The library exposes the resources of the Greendizer API in a simple yet powerful way. It allows developers to create applications for Greendizer quickly and efficiently. For a detailed documentation about how to use it, you can check out our [Libraries Cookbook](https://www.greendizer.com/docs/libraries/).

We also offer a number of other libraries in [other popular programming languages](https://www.greendizer.com/docs/libraries/downloads/) on our website.