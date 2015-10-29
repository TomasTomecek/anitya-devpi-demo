FROM fedora:22
# cffi>=1.1.0->cryptography->fedmsg->-r
RUN dnf install -y gcc python-devel libffi-devel openssl-devel git gcc-c++

RUN git clone -b anitya-devpi-demo https://github.com/TomasTomecek/anitya.git /src
WORKDIR /src

# in Fedora we have ancient cffi atm
# RUN dnf install -y python-cffi
RUN pip install --user -r requirements.txt
RUN python createdb.py
EXPOSE 5000
COPY anitya.cfg /etc/anitya.cfg
ENV "ANITYA_WEB_CONFIG"="/etc/anitya.cfg"

CMD ./runserver.py
