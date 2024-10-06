

FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal

RUN apt-get update && apt-get -y install --no-install-recommends \
   python3.8-venv \
   gcc 
   
ARG USER="codespace"
ARG VENV_PATH="/home/${USER}/venv"
COPY requirements.txt /tmp/
COPY Makefile /tmp/
RUN su $USER -c "/usr/bin/python3 -m venv /home/${USER}/venv" \
   && su $USER -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
   && rm -rf /tmp/requirements.txt 
