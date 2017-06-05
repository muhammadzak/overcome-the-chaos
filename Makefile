.PHONY: all clean

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

all: data/processed/processed.pickle reports/figures/exploratory.png

clean:
	rm -f data/raw/*.csv
	rm -f data/processed/*.pickle
	rm -f data/processed/*.xlsx
	rm -f reports/figures/*.png

data/raw/iris.csv:
	python src/data/download.py $(IRIS_URL) $@
	
data/processed/processed.pickle: data/raw/iris.csv
		python src/data/preprocess.py $< $@ --excel data/processed/processed.xlsx
	
reports/figures/exploratory.png: data/processed/processed.pickle
	python src/visualization/exploratory.py $< $@

reports/evaluation.json: data/processed/processed.pickle
	python src/evaluation/evaluate.py $@ $<
