import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob


def main():
    # plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    # in a boxplot

    cdir = os.getcwd()
    tdir = glob.glob(f'{cdir}/mia-result/*')[0]
    data = pd.read_csv(f'{tdir}/results.csv', delimiter=';')
    results = pd.DataFrame(data)
    results.boxplot(column='DICE', by='LABEL', grid=False)
    plt.suptitle('')
    plt.title("Comparison of DICE for the different labels")
    plt.xlabel('')
    plt.ylabel('DICE coefficient')
    plt.savefig(f'{tdir}/DICE_boxplot.png')


if __name__ == '__main__':
    main()
