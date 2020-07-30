FROM continuumio/miniconda2

RUN mkdir -p /usr/src/code/
WORKDIR /usr/src/code/

COPY . /usr/src/code/

RUN conda env update -n base -f conda.yml

ENTRYPOINT ["python", "nspdk.py"]
