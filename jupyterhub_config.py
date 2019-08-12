import os
import jwt

from oauthenticator.azuread import AzureAdOAuthenticator
c.JupyterHub.authenticator_class = AzureAdOAuthenticator

c.Application.log_level = 'DEBUG'

c.JupyterHub.hub_port = 8000
c.JupyterHub.port = 80

c.AzureAdOAuthenticator.tenant_id = os.environ.get('AAD_TENANT_ID')
c.AzureAdOAuthenticator.oauth_callback_url = os.environ.get('OAUTH_CALLBACK_URL')
c.AzureAdOAuthenticator.client_id = os.environ.get('APP_CLIENT_ID')
c.AzureAdOAuthenticator.client_secret = os.environ.get('APP_CLIENT_SECRET')
