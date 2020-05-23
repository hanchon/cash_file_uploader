FROM python:3.8.2-buster
RUN apt-get update && \
    apt-get install git wget curl -y && \
    apt-get install python3-pyqt5 python3-pyqt5.qtsvg -y && \
    apt-get install python3-setuptools -y  && \
    apt-get install libtool automake -y

WORKDIR /data
RUN git clone "https://github.com/Electron-Cash/Electron-Cash.git" && \
    cd Electron-Cash && \
    ./contrib/make_secp && \
    python3 setup.py install

