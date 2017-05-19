import luigi
from src.data.download import download_file

class DownloadDataset(luigi.Task):
    url = luigi.Parameter(default='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    filename = luigi.Parameter(default='data/raw/iris.csv')

    def output(self):
        return luigi.LocalTarget('data/raw/iris.csv')

    def run(self):
        with self.output().open('wb') as ofile:
            ofile.write(download_file('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'))

class Make(luigi.Task):

    def requires(self):
        return [DownloadDataset()]

if __name__ == '__main__':
    luigi.run()