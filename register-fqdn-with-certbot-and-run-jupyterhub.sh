#!/bin/bash

# Registering the FQDN using certbot. EMAIL_ADDRESS and LETS_ENCRYPT_REGISTER_FQDN are passed in as environment variables.
echo "--- [Registering the FQDN - $LETS_ENCRYPT_REGISTER_FQDN using certbot] ---"
certbot \
certonly \
--standalone \
-m $EMAIL_ADDRESS \
-d $LETS_ENCRYPT_REGISTER_FQDN \
--agree-tos \
--quiet

sleep 5

# Starting Jupyterhub
echo "--- [Starting Jupyterhub] ---"
jupyterhub
