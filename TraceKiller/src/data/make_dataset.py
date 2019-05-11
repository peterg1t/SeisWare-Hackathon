# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to create raw data (../data)
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    from __future__ import absolute_import, division, print_function

    import os
    import sys

    project_root = '/home/cchalc/Projects/seiswarehack/SeisWare-Hackathon/TraceKiller'
    data_folder = os.path.join(project_root, 'data')
    src_folder = os.path.join(project_root, 'src')
    sys.path.insert(0, src_folder)

    # Parameters
    input_size = 500

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, input_size, 1)
    y = np.random.gamma(2., 2., input_size)

    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv(os.path.join(data_folder, 'data.csv'))

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
