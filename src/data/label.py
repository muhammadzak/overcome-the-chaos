import click
import pandas as pd


def label_data(dframe):
    dframe.columns = ['x0', 'x1', 'x2', 'x3', 'y']


@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True, dir_okay=False))
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
@click.option('--excel', type=click.Path(writable=True, dir_okay=False))
def label_data_command(input_file, output_file, excel):
    print('Labeling dataframe')

    dframe = pd.read_csv(input_file)
    label_data(dframe)

    dframe.to_pickle(output_file)
    if excel is not None:
        dframe.to_excel(excel)


if __name__ == '__main__':
    label_data_command()
