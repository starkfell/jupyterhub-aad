#!/bin/bash

# Registering the FQDN using certbot. EMAIL_ADDRESS and LETS_ENCRYPT_REGISTER_FQDN are passed in as environment variables.
certbot \
certonly \
--standalone \
-m $EMAIL_ADDRESS \
-d $LETS_ENCRYPT_REGISTER_FQDN \
--agree-tos \
-n
