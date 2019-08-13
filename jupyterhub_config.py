import os
import sys
import subprocess
import jwt

from oauthenticator.azuread import AzureAdOAuthenticator
c.JupyterHub.authenticator_class = AzureAdOAuthenticator

c.Application.log_level = 'DEBUG'

c.JupyterHub.hub_port = 8000
c.JupyterHub.port = 443

LetsEncryptRegisterFqdn = os.environ.get('LETS_ENCRYPT_REGISTER_FQDN')

c.JupyterHub.ssl_key = '/etc/letsencrypt/live/{}/privkey.pem'.format(LetsEncryptRegisterFqdn)
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/{}/fullchain.pem'.format(LetsEncryptRegisterFqdn)

c.AzureAdOAuthenticator.tenant_id = os.environ.get('AAD_TENANT_ID')
c.AzureAdOAuthenticator.oauth_callback_url = os.environ.get('OAUTH_CALLBACK_URL')
c.AzureAdOAuthenticator.client_id = os.environ.get('APP_CLIENT_ID')
c.AzureAdOAuthenticator.client_secret = os.environ.get('APP_CLIENT_SECRET')

# ----- BELOW IS UNSTABLE ----- Refer to https://github.com/jupyterhub/ldapauthenticator/issues/54
config_dir = os.path.dirname(os.path.abspath(__file__)) 

# Extend the LDAPAuthenticator with a custom add_user method
# add_user.sh should be in the same directory as jupyterhub_config.py
# (mostly by @minrk)

from ldapauthenticator import LDAPAuthenticator 
class MyAuthenticator(LDAPAuthenticator):      
    def add_user(self, user):             
	super().add_user(user)
        script_path = os.path.join(config_dir, "add_user.sh")      
        subprocess.check_call(['bash', script_path, user.name])
                                  
# Use the custom authenticator; no quotes!
c.JupyterHub.authenticator_class = MyAuthenticator            

# see issue #32
# you can also use c.LDAPAuthenticator for all of these (matter of style)
c.MyAuthenticator.server_address = 'myadserver'                   
c.MyAuthenticator.bind_dn_template = '{username}'         
c.MyAuthenticator.lookup_dn = True          
c.MyAuthenticator.use_ssl = False                
c.MyAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
c.MyAuthenticator.lookup_dn_search_user = 'ldapsearchuser'          
c.MyAuthenticator.lookup_dn_search_password = 'ldapsearchpassword'  
c.MyAuthenticator.user_attribute = 'sAMAccountName'             
c.MyAuthenticator.user_search_base = 'ou=Org users,dc=domainorg,dc=local' 
c.MyAuthenticator.lookup_dn_user_dn_attribute = 'cn'
c.MyAuthenticator.admin_users = {'adminuser'}          
          
c.Spawner.notebook_dir = '~/notebooks'
