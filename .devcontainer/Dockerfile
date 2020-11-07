FROM python:3.6-stretch
USER root

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && \
    apt-get -y install --no-install-recommends apt-utils dialog 2>&1 && \
    apt-get -y install git iproute2 procps lsb-release autoconf automake libtool
    
RUN apt-get -y install locales && \
    mkdir /code && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    apt-get install -y sudo && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

WORKDIR /workspace/auto_shutter
RUN apt-get update -y && \
    apt-get -y install build-essential checkinstall cmake unzip pkg-config qt5-default yasm && \
    apt-get -y install git gfortran python3-dev python3-numpy && \
    apt-get -y install libjpeg62-turbo-dev libpng-dev libavcodec-dev libavformat-dev \
                       libswscale-dev libdc1394-22-dev libxine2-dev libv4l-dev && \
    apt-get -y install libjpeg-dev libpng-dev libtiff-dev libtbb-dev && \
    apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev \
                       libxvidcore-dev libx264-dev libgtk-3-dev

WORKDIR /usr/local/src
RUN git clone https://github.com/opencv/opencv.git && \
    git clone https://github.com/opencv/opencv_contrib.git

WORKDIR /usr/local/src/opencv_contrib
RUN git checkout -b 3.4.3 refs/tags/3.4.3
WORKDIR /usr/local/src/opencv
RUN git checkout -b 3.4.3 refs/tags/3.4.3 && \
    mkdir /build

WORKDIR /usr/local/src/opencv/build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_FFMPEG=ON -D BUILD_opencv_python2=ON \
          -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON \
          -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules .. \
          -D WITH_CUBLAS=ON -D CUDA_NVCC_FLAGS="-D_FORCE_INLINES" .. && \
    make -j7 && \
    make install && \
    echo /usr/local/lib > /etc/ld.so.conf.d/opencv.conf && \
    ldconfig -v && \
    apt-get update

WORKDIR /workspace/auto_shutter
RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt