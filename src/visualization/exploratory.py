import click
import pandas as pd
import matplotlib

matplotlib.use('agg')
import seaborn as sns


def exploratory_visualization(dframe):
    return sns.pairplot(dframe, vars=['x0', 'x1', 'x2', 'x3'], hue='y')


@click.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
def exploratory_visualization_command(input_file, output_file):
    print('Plotting pairwise distribution...')

    dframe = pd.read_pickle(input_file)
    plot = exploratory_visualization(dframe)
    plot.savefig(output_file)


if __name__ == '__main__':
    exploratory_visualization_command()
