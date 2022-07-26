# Structure/Thoughts/Papers
1. Differences in Causal Discovery Algorithms
1. General Introduction to Granger Causality
1. Bivariate Linear Granger Methods
1. Multivariate Linear Granger Methods
1. Multivariate Nonlinear Granger Methods

Link to papers in the notebook is always included after I cited/copied text or code from it.

Statsmodels python module is the most common way to perform a granger test [link](https://www.statsmodels.org/dev/generated/statsmodels.tsa.stattools.grangercausalitytests.html). However, only supports bivariate linear data. Other approaches are implemented from the teams that published the paper.

The models folder contains the different implementations of granger methods, copied from the papers github repos. Each file/method has a link to the corresponding github repo in its first line.

The dataset_utils.py is for generating synthetic data, plot_utils.py offers plotting support and test_utils.py contains non granger tests. Note: these files are mostly copied from different sources and adapted to own needs.


Here is an overview of the papers/github repos I cited:
* Granger causality in the frequency domain: derivation and applications [Paper](https://www.scielo.br/j/rbef/a/m4LwwHLvk7YwPNMhngNJQwp/?lang=en) [Github](https://github.com/ViniciusLima94/pyGC)
* TCDF: Temporal Causal Discovery Framework [Paper](https://www.mdpi.com/2504-4990/1/1/19) [Github](https://github.com/M-Nauta/TCDF)
* A MATLAB toolbox for Granger causal connectivity analysis
[Paper](https://www.sciencedirect.com/science/article/pii/S0165027009006189)
* Is there a relationship between popularity of a given technology on Stack Overflow (SO) and Hacker News (HN) [Github](https://github.com/dgwozdz/HN_SO_analysis)
* Temporal Causal Modeling with Graphical Granger Methods [Paper](https://www.andrewoarnold.com/frp781-arnold.pdf) [Github](https://github.com/arahatashun/Granger-causality-python )
* Interpretable Models for Granger Causality Using Self-explaining Neural Networks [Paper](https://openreview.net/forum?id=DEa4JdMWRHp)
* Neural Granger Causality [Paper](https://arxiv.org/abs/1802.05842) [Github](https://github.com/iancovert/Neural-GC)
* Granger causality test with nonlinear neural-network-based methods [Paper](https://www.sciencedirect.com/science/article/pii/S0169260722000542)
