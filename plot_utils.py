import matplotlib.pyplot as plt
import numpy as np

def plot_all_and_first_points(X, N):
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(X)
    ax[0].set_xlabel('T')
    ax[0].set_title('All time series')
    ax[1].plot(X[:N])
    ax[1].set_xlabel('T')
    ax[1].set_title("First {} time points".format(N))
    plt.tight_layout()
    plt.show()

def plot_gc_graphs(actual, est):

    def calc_falsePositives(actual, est):
        counter = 0
        for i in range(actual.shape[0]):
            for j in range(actual.shape[1]):
                if actual[i, j] == 0 and est[i, j] == 1:
                    counter+=1
        return counter

    def calc_falseNegatives(actual, est):
        counter = 0
        for i in range(actual.shape[0]):
            for j in range(actual.shape[1]):
                if actual[i, j] == 1 and est[i, j] == 0:
                    counter+=1
        return counter

    def calcTruePositves(actual, est):
        counter = 0
        for i in range(actual.shape[0]):
            for j in range(actual.shape[1]):
                if actual[i, j] == 1 and est[i, j] == 1:
                    counter+=1
        return counter

    print('True variable usage = %.2f%%' % (100 * np.mean(actual)))
    print('Estimated variable usage = %.2f%%' % (100 * np.mean(est)))
    print('Accuracy = %.2f%%' % (100 * np.mean(actual == est)))
    pre = (100 * calcTruePositves(actual, est) / (calcTruePositves(actual, est) + calc_falsePositives(actual, est)))
    rec = (100 * calcTruePositves(actual, est) / (calcTruePositves(actual, est) + calc_falseNegatives(actual, est)))
    f1 = (2*pre*rec)/(pre+rec)
    print('Precision = %.2f%%' % pre)
    print('Recall = %.2f%%' % rec)
    print('F1 Score = %.2f%%' % f1)

    # Make figures
    fig, axarr = plt.subplots(1, 2, figsize=(16, 5))
    axarr[0].imshow(actual, cmap='Blues')
    axarr[0].set_title('GC actual')
    axarr[0].set_ylabel('Affected series')
    axarr[0].set_xlabel('Causal series')
    axarr[0].set_xticks([])
    axarr[0].set_yticks([])

    axarr[1].imshow(est, cmap='Blues', vmin=0, vmax=1, extent=(0, len(est), len(est), 0))
    axarr[1].set_title('GC estimated')
    axarr[1].set_ylabel('Affected series')
    axarr[1].set_xlabel('Causal series')
    axarr[1].set_xticks([])
    axarr[1].set_yticks([])

    # Mark disagreements
    for i in range(len(est)):
        for j in range(len(est)):
            if actual[i, j] != est[i, j]:
                rect = plt.Rectangle((j, i-0.05), 1, 1, facecolor='none', edgecolor='red', linewidth=1)
                axarr[1].add_patch(rect)

    plt.show()
