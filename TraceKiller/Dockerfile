FROM python:3.7.3-jessie

COPY requirements.txt /home/cchalc/Projects/seiswarehack/SeisWare-Hackathon/TraceKiller

# will be overwriten should `docker run` pass a proper env
ENV EXECUTION_ID 111111

# match the name of jupyter's kernel where necessary
RUN pip install virtualenv
RUN virtualenv -p python3 swhack
RUN /bin/bash -c "source /home/cchalc/.virtualenvs/swhack/bin/activate"

RUN pip install -r /home/cchalc/Projects/seiswarehack/SeisWare-Hackathon/TraceKiller/requirements.txt
RUN ipython kernel install --user --name=swhack

RUN mkdir notebook/output

COPY Example01.ipynb ./notebook/Exmample01_outt.ipynb
COPY params.yaml ./notebook/parameters/params.yaml
COPY run.sh ./src/run.sh

WORKDIR notebook
ENTRYPOINT ["bash", "./run.sh"]
