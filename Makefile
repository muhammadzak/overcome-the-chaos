.PHONY: all clean

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

all: data/raw/iris.csv

clean:
	rm -f data/raw/*.csv

data/raw/iris.csv:
	python src/data/download.py $(IRIS_URL) $@

