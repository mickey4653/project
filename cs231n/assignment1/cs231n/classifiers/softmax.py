from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    # get number of class and train
    num_train = X.shape[0]
    num_class = W.shape[1]
    # calculate the score
    scores = X.dot(W)  #N*C
    p = np.zeros_like(W)
    dW_each = np.zeros_like(W)
    # calculate soft max 
    scores_max = np.reshape(np.max(scores, axis=1), (num_train, 1))
    p = np.exp(scores - scores_max) / np.sum(np.exp(scores - scores_max), axis=1, keepdims=True) # N*C
    loss_selector = np.zeros_like(p)
    loss_selector[np.arange(num_train),y] = 1.0
    # calculate loss fiunction
    for i in xrange(num_train):
        for j in xrange(num_class):
            loss -= loss_selector[i,j] * np.log(p[i,j])
            dW_each[:, j] = -(loss_selector[i, j] - p[i, j]) * X[i, :].T
        dW = dW + dW_each
    # devide loss function and gradiants
    loss /= num_train
    # add regulization
    loss += 0.5 * reg * np.sum(W * W)
    dW /= num_train
    dW += reg * W
    # pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    # calculate the score
    num_train = X.shape[0]
    num_class = W.shape[1]
    scores = X.dot(W)  #N*C
    p = np.zeros_like(W)
    # calculate loss function
    scores_max = np.reshape(np.max(scores, axis=1), (num_train, 1))
    p = np.exp(scores - scores_max) / np.sum(np.exp(scores - scores_max), axis=1, keepdims=True) # N*C
    loss_selector = np.zeros_like(p) #N*C
    loss_selector[np.arange(num_train),y] = 1.0
    loss = - np.sum(loss_selector.dot(np.log(p.T))[0,:])
    # gradient and loss function
    dW = -(loss_selector - p).T.dot(X)
    dW = dW.T
    loss /= num_train
    # add reglization
    loss += 0.5 * reg * np.sum(W * W)
    dW /= num_train
    dW += reg * W
# pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
