import matplotlib.pyplot as plt
import pandas as pd
import os
import glob


def main():
    # plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    # in a boxplot

    cdir = os.getcwd()
    subdirs = [ f.path for f in os.scandir(f'{cdir}/mia-result') if f.is_dir() ]
    for dirs in subdirs:
        if not os.path.exists(f'{dirs}/DICE_boxplot.png'):
            data = pd.read_csv(f'{dirs}/results.csv', delimiter=';')
            results = pd.DataFrame(data)
            results.boxplot(column='DICE', by='LABEL', grid=False)
            plt.suptitle('')
            plt.title("Comparison of DICE for the different labels")
            plt.xlabel('')
            plt.ylabel('DICE coefficient')
            plt.savefig(f'{dirs}/DICE_boxplot.png')




if __name__ == '__main__':
    main()
