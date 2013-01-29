from django.http import HttpResponse
from greendizer.oauth import OAuthClient
from greendizer.clients import BuyerClient

""" Form an OAuth client.

Keyword arguments:
client_type
client_id
client_secret
scope
redirect_uri
"""

oauth_client  = OAuthClient(client_type='buyers',
                            client_id='2343115',
                            client_secret='685d097c556f250162a517e89d08821df6d80a7d89c0a0e6104a2ec557a785fe',
                            scope='read_invoices read_account',
                            redirect_uri='http://localhost:8000/login/app/',)
"""
Views for the login and main page

"""
def auth_page(request):
    auth_url = oauth_client.get_authorize_url(redirect_uri="http://localhost:8000/login/app/")
    html = "<html><body>This is a Greendizer Boilerplate! </br><a href='%s'>Login</a></body></html>" % auth_url
    return HttpResponse(html)

def main_page(request):
    #get authorization code from http response
    #and exchange it with the access token
    
    credentials = oauth_client.obtain_token(code=request.GET.get('code'))
    access_token = credentials.oauth_token
    
    
    #access the settings and the invoices
    settings = BuyerClient(access_token).user.settings
    auth_user = BuyerClient(access_token).user
    email = auth_user.emails['amine.karmouche@greendizer.com']
    invoice_collection = email.invoices.all
    invoice_collection.populate()

    html = "<html><body>Welcome! </br> User's settings: </br>____Language: %s</br>____Region: %s</br>____Currency: %s</br>_______________________________</br>List of invoices:</br> %s </br></body></html>" % (settings.language, settings.region, settings.currency, str(invoice_collection.resources))
    return HttpResponse(html)