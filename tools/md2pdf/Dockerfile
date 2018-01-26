FROM ubuntu:14.04.5
# Ubuntu 14.04.5 LTS Trusty Tahr Released:August 4, 2016 EOL:April 2019

# Taken from https://github.com/Fiware/tools.Md2pdf

ENV MD2PDF_VERSION 0.2.2

RUN apt-get update -qq
RUN apt-get upgrade -y
RUN apt-get install -y \
      texlive-xetex \
      texlive-fonts-recommended \
      texlive-latex-extra \
      texlive
RUN apt-get install -y \
      unzip \
      git \
      python \
      python-pip \
      wget \
      build-essential
RUN apt-get install -y \
      pdftk

RUN wget https://github.com/jgm/pandoc/releases/download/1.15.1/pandoc-1.15.1-1-amd64.deb \
    && dpkg -i pandoc-1.15.1-1-amd64.deb

RUN wget https://github.com/Fiware/tools.Md2pdf/archive/$MD2PDF_VERSION.zip \
 && unzip $MD2PDF_VERSION.zip \
 && cd tools.Md2pdf-$MD2PDF_VERSION \
 && python setup.py install \
 && cd

# TODO cleanup!

#ENTRYPOINT ["markdown_to_pdf"]

#CMD ["--help"]
