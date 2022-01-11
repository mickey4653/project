from builtins import range
from builtins import object
import numpy as np

from ..layers import *
from ..layer_utils import *


class FullyConnectedNet(object):
    """Class for a multi-layer fully connected neural network.

    Network contains an arbitrary number of hidden layers, ReLU nonlinearities,
    and a softmax loss function. This will also implement dropout and batch/layer
    normalization as options. For a network with L layers, the architecture will be

    {affine - [batch/layer norm] - relu - [dropout]} x (L - 1) - affine - softmax

    where batch/layer normalization and dropout are optional and the {...} block is
    repeated L - 1 times.

    Learnable parameters are stored in the self.params dictionary and will be learned
    using the Solver class.
    """

    def __init__(
        self,
        hidden_dims,
        input_dim=3 * 32 * 32,
        num_classes=10,
        dropout_keep_ratio=1,
        normalization=None,
        reg=0.0,
        weight_scale=1e-2,
        dtype=np.float32,
        seed=None,
    ):
        """Initialize a new FullyConnectedNet.

        Inputs:
        - hidden_dims: A list of integers giving the size of each hidden layer.
        - input_dim: An integer giving the size of the input.
        - num_classes: An integer giving the number of classes to classify.
        - dropout_keep_ratio: Scalar between 0 and 1 giving dropout strength.
            If dropout_keep_ratio=1 then the network should not use dropout at all.
        - normalization: What type of normalization the network should use. Valid values
            are "batchnorm", "layernorm", or None for no normalization (the default).
        - reg: Scalar giving L2 regularization strength.
        - weight_scale: Scalar giving the standard deviation for random
            initialization of the weights.
        - dtype: A numpy datatype object; all computations will be performed using
            this datatype. float32 is faster but less accurate, so you should use
            float64 for numeric gradient checking.
        - seed: If not None, then pass this random seed to the dropout layers.
            This will make the dropout layers deteriminstic so we can gradient check the model.
        """
        self.normalization = normalization
        self.use_dropout = dropout_keep_ratio != 1
        self.reg = reg
        self.num_layers = 1 + len(hidden_dims)
        self.dtype = dtype
        self.params = {}

        ############################################################################
        # TODO: Initialize the parameters of the network, storing all values in    #
        # the self.params dictionary. Store weights and biases for the first layer #
        # in W1 and b1; for the second layer use W2 and b2, etc. Weights should be #
        # initialized from a normal distribution centered at 0 with standard       #
        # deviation equal to weight_scale. Biases should be initialized to zero.   #
        #                                                                          #
        # When using batch normalization, store scale and shift parameters for the #
        # first layer in gamma1 and beta1; for the second layer use gamma2 and     #
        # beta2, etc. Scale parameters should be initialized to ones and shift     #
        # parameters should be initialized to zeros.                               #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        # size of 3072*hidden_dims*class
        parameters=[input_dim]+hidden_dims+[num_classes]
        # calculate the length(input layer+hidden+output)
        lx=len(parameters)
        # assign param for each layer
        for i in range(1,lx):
            LayerW='W'+str(i)
            LayerBias='b'+str(i)
            # set bias to radndom
            # Weights should be initialized from a normal distribution 
            # centered at 0 with standard deviation equal to weight_scale.
            self.params[LayerW]=np.random.randn(parameters[i-1],parameters[i])*weight_scale
            # set bias to zeros
            self.params[LayerBias]=np.zeros(parameters[i])
        # When using batch normalization, store scale and shift parameters for the 
        # first layer in gamma1 and beta1; for the second layer use gamma2 and     
        # beta2, etc. Scale parameters should be initialized to ones and shift     
        # parameters should be initialized to zeros.*/                  
        if self.normalization=="batchnorm":
            # go through each layer
            for i in range(1,lx-1):
                #  store scale and shift parameters for the 
                # first layer in gamma1 and beta1
                LayerGama='gamma'+str(i)
                LayerBeta='beta'+str(i)
                self.params[LayerGama]=np.ones(parameters[i])
                self.params[LayerBeta]=np.zeros(parameters[i])
        # pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        # When using dropout we need to pass a dropout_param dictionary to each
        # dropout layer so that the layer knows the dropout probability and the mode
        # (train / test). You can pass the same dropout_param to each dropout layer.
        self.dropout_param = {}
        if self.use_dropout:
            self.dropout_param = {"mode": "train", "p": dropout_keep_ratio}
            if seed is not None:
                self.dropout_param["seed"] = seed

        # With batch normalization we need to keep track of running means and
        # variances, so we need to pass a special bn_param object to each batch
        # normalization layer. You should pass self.bn_params[0] to the forward pass
        # of the first batch normalization layer, self.bn_params[1] to the forward
        # pass of the second batch normalization layer, etc.
        self.bn_params = []
        if self.normalization == "batchnorm":
            self.bn_params = [{"mode": "train"} for i in range(self.num_layers - 1)]
        if self.normalization == "layernorm":
            self.bn_params = [{} for i in range(self.num_layers - 1)]

        # Cast all parameters to the correct datatype.
        for k, v in self.params.items():
            self.params[k] = v.astype(dtype)

    def loss(self, X, y=None):
        """Compute loss and gradient for the fully connected net.
        
        Inputs:
        - X: Array of input data of shape (N, d_1, ..., d_k)
        - y: Array of labels, of shape (N,). y[i] gives the label for X[i].

        Returns:
        If y is None, then run a test-time forward pass of the model and return:
        - scores: Array of shape (N, C) giving classification scores, where
            scores[i, c] is the classification score for X[i] and class c.

        If y is not None, then run a training-time forward and backward pass and
        return a tuple of:
        - loss: Scalar value giving the loss
        - grads: Dictionary with the same keys as self.params, mapping parameter
            names to gradients of the loss with respect to those parameters.
        """
        X = X.astype(self.dtype)
        mode = "test" if y is None else "train"

        # Set train/test mode for batchnorm params and dropout param since they
        # behave differently during training and testing.
        if self.use_dropout:
            self.dropout_param["mode"] = mode
        if self.normalization == "batchnorm":
            for bn_param in self.bn_params:
                bn_param["mode"] = mode
        scores = None
        ############################################################################
        # TODO: Implement the forward pass for the fully connected net, computing  #
        # the class scores for X and storing them in the scores variable.          #
        #                                                                          #
        # When using dropout, you'll need to pass self.dropout_param to each       #
        # dropout forward pass.                                                    #
        #                                                                          #
        # When using batch normalization, you'll need to pass self.bn_params[0] to #
        # the forward pass for the first batch normalization layer, pass           #
        # self.bn_params[1] to the forward pass for the second batch normalization #
        # layer, etc.                                                              #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ##############################################################
        # reshape x
        N,D=X.shape[0],np.prod(X.shape[1:])
        scores=X.reshape(N,D)
        # store scores in list
        list_x_in={}
        list_x_in['x'+str(0)]=scores
        for i in range(1,self.num_layers):
            xa,wa,ba=scores,self.params['W'+str(i)],self.params['b'+str(i)]
            if self.normalization=="batchnorm" and self.use_dropout:
                # get gamma beta
                gamma,beta=self.params['gamma'+str(i)],self.params['beta'+str(i)]
                 # get score and cache with drop and natchnorm and drop
                scores,cache=affine_bn_relu_drop_forward(xa,wa,ba,gamma,beta,self.bn_params[i-1],self.dropout_param)
            elif self.normalization=='batchnorm':
                gamma,beta=self.params['gamma'+str(i)],self.params['beta'+str(i)]
                # get score and cache with drop and natchnorm 
                scores,cache=affine_bn_relu_forward(xa,wa,ba,gamma,beta,self.bn_params[i-1])
            elif self.use_dropout:
                # get score and cache with drop
                # scores,cache=affine_relu_forward(xa,wa,ba,self.dropout_param)
                scores,cache=affine_relu_dropout_forward(xa,wa,ba,self.dropout_param)
            else:
                 # get score and cache without drop
                 scores,cache=affine_relu_forward(xa,wa,ba)
            # store cache
            list_x_in['x'+str(i)]=cache
        # last layer dont use relu
        xa,wa,ba=scores,self.params['W'+str(self.num_layers)],self.params['b'+str(self.num_layers)]
        # get and store scores and cache
        scores,cache=affine_forward(xa,wa,ba)
        list_x_in['x'+str(self.num_layers)]=cache
        #########################################
        
         # pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        # If test mode return early.
        if mode == "test":
            return scores

        loss, grads = 0.0, {}
        ############################################################################
        # TODO: Implement the backward pass for the fully connected net. Store the #
        # loss in the loss variable and gradients in the grads dictionary. Compute #
        # data loss using softmax, and make sure that grads[k] holds the gradients #
        # for self.params[k]. Don't forget to add L2 regularization!               #
        #                                                                          #
        # When using batch/layer normalization, you don't need to regularize the   #
        # scale and shift parameters.                                              #
        #                                                                          #
        # NOTE: To ensure that your implementation matches ours and you pass the   #
        # automated tests, make sure that your L2 regularization includes a factor #
        # of 0.5 to simplify the expression for the gradient.                      #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        # ToBeDone
        # backward pass
        # add L2 regularization! 
        # get loss
        loss,dout=softmax_loss(scores,y)
        for i in range(self.num_layers):
            # L2 loss
            loss=loss+0.5*self.reg*np.sum(np.square(self.params['W'+str(i+1)]))
        # get local gradient
        cache=list_x_in['x'+str(self.num_layers)]
        dout,dw,db=affine_backward(dout,cache)
        # first layer gradient
        grads['W'+str(self.num_layers)],grads['b'+str(self.num_layers)]=dw+self.reg*self.params['W'+str(self.num_layers)],db
        
        # go through layers and get gradient
        for id in range(self.num_layers-1,0,-1):
            cache=list_x_in['x'+str(id)]
            
            if self.normalization=="batchnorm" and self.use_dropout:
                # back proporgation with batchnorm and drop
                dout,dw,db,dgamma,dbeta=affine_bn_relu_drop_backward(dout,cache)
                grads['gamma'+str(id)],grads['beta'+str(id)]=dgamma,dbeta
            elif self.normalization=='batchnorm':
                # back proporgation with batchnorm 
                dout,dw,db,dgamma,dbeta=affine_bn_relu_backward(dout,cache)
                grads['gamma'+str(id)],grads['beta'+str(id)]=dgamma,dbeta
            elif self.use_dropout:
                # back proporgation with  drop
                dout,dw,db=affine_relu_dropout_backward(dout,cache)
            else:
                # normal back proporgation 
                dout,dw,db=affine_relu_backward(dout,cache)
            
            grads['W'+str(id)],grads['b'+str(id)]=dw+self.reg*self.params['W'+str(id)],db
        ########################################################
        
        # pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        return loss, grads
