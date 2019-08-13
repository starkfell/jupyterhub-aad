import os
import jwt

from oauthenticator.azuread import AzureAdOAuthenticator
c.JupyterHub.authenticator_class = AzureAdOAuthenticator

c.Application.log_level = 'DEBUG'

c.JupyterHub.hub_port = 8000
c.JupyterHub.port = 443

c.LetsEncryptRegisterFqdn = os.environ.get('LETS_ENCRYPT_REGISTER_FQDN')

c.JupyterHub.ssl_key = '/etc/letsencrypt/live/{}/privkey.pem'.format(c.LetsEncryptRegisterFqdn)
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/{}/fullchain.pem'.format(c.LetsEncryptRegisterFqdn)

c.AzureAdOAuthenticator.tenant_id = os.environ.get('AAD_TENANT_ID')
c.AzureAdOAuthenticator.oauth_callback_url = os.environ.get('OAUTH_CALLBACK_URL')
c.AzureAdOAuthenticator.client_id = os.environ.get('APP_CLIENT_ID')
c.AzureAdOAuthenticator.client_secret = os.environ.get('APP_CLIENT_SECRET')
