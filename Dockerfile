FROM debian:bookworm

ENV DEBIAN_FRONTEND=noninteractive

# Dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    python3 \
    python3-pip \
    xvfb \
    wget \
    && apt-get clean

# Install Selenium recent (latest stable)
RUN pip3 install --break-system-packages --upgrade pip && \
    pip3 install --break-system-packages selenium videodrone

ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# Fake video folder
ENV VDPATH=VideoDrone
ENV VD_Y4M=/$VDPATH/y4ms/

RUN mkdir -p $VD_Y4M
WORKDIR $VD_Y4M

# Sample Y4M
RUN wget https://media.xiph.org/video/derf/y4m/stefan_cif.y4m

WORKDIR /$VDPATH
CMD ["bash"]

