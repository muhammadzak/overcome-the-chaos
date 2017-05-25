.PHONY: all clean

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

all: data/processed/featurized.pickle reports/figures/exploratory.png

clean:
	rm -f data/raw/*.csv
	rm -f data/interim/*.pickle
	rm -f data/interim/*.xlsx
	rm -f data/processed/*.pickle
	rm -f data/processed/*.xlsx
	rm -f reports/figures/*.png

data/raw/iris.csv:
	python src/data/download.py $(IRIS_URL) $@
	
data/interim/labeled.pickle: data/raw/iris.csv
	python src/data/label.py $< $@ --excel data/interim/labeled.xlsx

data/processed/featurized.pickle: data/interim/labeled.pickle
	python src/features/generate_features.py $< $@ --excel data/processed/featurized.xlsx
	
reports/figures/exploratory.png: data/interim/labeled.pickle
	python src/visualization/exploratory.py $< $@

