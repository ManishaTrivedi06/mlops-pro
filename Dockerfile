FROM centos:7
MAINTAINER maze9***@gmail.com
RUN yum install net-tools -y
RUN yum install python36 -y
RUN yum install epel-release -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install pillow
