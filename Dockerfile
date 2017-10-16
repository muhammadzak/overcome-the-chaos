FROM conda/miniconda3:latest
ENTRYPOINT ["/bin/bash", "-c"]
EXPOSE 5000
COPY environment.yml /app/

RUN conda env create -f /app/environment.yml -n chaos

COPY . /app

WORKDIR /app

ENTRYPOINT [ "/bin/bash", "-c", "source activate chaos && python api.py" ]
