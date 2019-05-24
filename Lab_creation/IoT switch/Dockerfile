FROM python:3

WORKDIR /usr/local/bin

RUN echo "root:admin" | chpasswd && echo $'pts/0\npts/1\npts/2\npts/3\npts/4\npts/5\npts/6\npts/7' >> /etc/securetty && pip install paho-mqtt

COPY mqttswitch.py .

CMD apt-get update && apt-get install -y telnetd && apt-get install -y xinetd && service xinetd start && python mqttswitch.py $var
