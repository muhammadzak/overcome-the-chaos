import click
import pandas as pd


def generate_features(dframe):
    dframe['gx01'] = dframe['x0'] * dframe['x1']
    dframe['gx12'] = dframe['x1'] * dframe['x2']
    dframe['gx23'] = dframe['x2'] * dframe['x3']
    dframe['gx30'] = dframe['x3'] * dframe['x0']


@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True, dir_okay=False))
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
@click.option('--excel', type=click.Path(writable=True, dir_okay=False))
def generate_features_command(input_file, output_file, excel):
    print('Generating features')

    dframe = pd.read_pickle(input_file)
    generate_features(dframe)

    dframe.to_pickle(output_file)
    if excel is not None:
        dframe.to_excel(excel)


if __name__ == '__main__':
    generate_features_command()
