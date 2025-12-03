FROM alpine:3.12.1
MAINTAINER Giuseppe De Marco <giuseppe.demarco@unical.it>

RUN apk update && \
    apk add --no-cache \
        chromium \
        chromium-chromedriver \
        xvfb \
        py-pip

ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# Install Selenium < 4.10
# NO because selenium >= 4.10 is a dep of videodrone
# RUN pip install "selenium<4.10"

RUN pip install videodrone

ENV VDPATH=VideoDrone
ENV VD_Y4M="/$VDPATH/y4ms/"

RUN mkdir -p $VD_Y4M
WORKDIR $VD_Y4M
RUN wget https://media.xiph.org/video/derf/y4m/stefan_cif.y4m

WORKDIR /$VDPATH

