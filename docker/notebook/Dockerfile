FROM sn-app:dev


RUN python3 -m pip install --upgrade pip
RUN pip install jupyter pygments Tornado django-print-sql --force-reinstall

RUN mkdir -p /root/.ipython/profile_default/startup/

COPY ./docker/notebook/startup_notebook.py /root/.ipython/profile_default/startup/
COPY ./docker/notebook/notebook.sh /

RUN chmod o+x /notebook.sh

ENTRYPOINT ["/notebook.sh"]
EXPOSE 8899
