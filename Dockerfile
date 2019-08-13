# Pulling from the official jupyterhub repo on Docker Hub.
FROM jupyterhub/jupyterhub:latest

RUN apt-get update && apt-get install -y \
git curl vim wget jq lsb-release net-tools software-properties-common python3-pip && \
add-apt-repository -y universe && \
add-apt-repository ppa:certbot/certbot -y && \
apt-get update && \
apt-get install -y certbot

RUN pip install oauthenticator PyJWT jupyterhub-ldapauthenticator

# Setting up jupyterhub.
WORKDIR /srv/jupyterhub
EXPOSE 8000
EXPOSE 443

# Adding in the register-fqdn-with-certbot.sh Script.
ADD register-fqdn-with-certbot-and-run-jupyterhub.sh /srv/jupyterhub/register-fqdn-with-certbot-and-run-jupyterhub.sh
RUN chmod -R 775 /srv/jupyterhub/*.sh

# Adding in the OAuth Configuration.
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

LABEL org.jupyter.service="jupyterhub"

CMD ["/srv/jupyterhub/register-fqdn-with-certbot-and-run-jupyterhub.sh"]
