import numpy as np

def activation(x, func='sigmoid'):
    '''
    returns the activation of x depnding on the func type
    '''
    if func == 'sigmoid':
        return 1/(1+np.exp(-x))

    return 'Invalid activation Function'


def accuracy(Y, Y_pred):
    '''
    Returns the accuracy for the predictions
    '''
    return np.sum(Y == Y_pred) / len(Y)


def flatten(X):
    if X.shape[3] == 3:
        return X.reshape(X.shape[0], X.shape[1]*X.shape[2]*X.shape[3])

    return 'Cannot flatten'
