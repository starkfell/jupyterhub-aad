#!/bin/bash

# Registering the FQDN using certbot.
certbot \
certonly \
--standalone \
-m EMAIL_ADDRESS \
-d LETS_ENCRYPT_REGISTER_FQDN \
--agree-tos \
-n
