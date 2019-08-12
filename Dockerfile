# Pulling from the official jupyterhub repo on Docker Hub.
FROM jupyterhub/jupyterhub:latest

RUN apt-get update && apt-get install -y git curl vim wget jq net-tools python3-pip

RUN pip install oauthenticator PyJWT

# Setting up jupyterhub.
WORKDIR /srv/jupyterhub
EXPOSE 8000
EXPOSE 443

# Adding in the OAuth Configuration.
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

LABEL org.jupyter.service="jupyterhub"

CMD ["jupyterhub"]
