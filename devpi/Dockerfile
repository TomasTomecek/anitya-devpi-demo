FROM fedora:22

RUN dnf install -y python-pip git

RUN pip install devpi-server devpi-client

EXPOSE 80
# VOLUME ["/var/lib/devpi"]

VOLUME /project

#ENTRYPOINT ["devpi-server", "--serverdir=/var/lib/devpi"]
ENTRYPOINT ["devpi-server"]
CMD ["--host=0.0.0.0", "--port=5001"]
