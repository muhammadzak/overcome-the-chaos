.PHONY: all clean

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

all: data/processed/preprocessed.pickle reports/figures/exploratory.png

clean:
	rm -f data/raw/*.csv
	rm -f data/processed/*.pickle
	rm -f data/processed/*.xlsx
	rm -f reports/figures/*.png

data/raw/iris.csv:
	python src/data/download.py $(IRIS_URL) $@
	
data/processed/preprocessed.pickle: data/raw/iris.csv
		python src/data/preprocess.py $< $@ --excel data/processed/preprocessed.xlsx
	
reports/figures/exploratory.png: data/interim/labeled.pickle
	python src/visualization/exploratory.py $< $@

