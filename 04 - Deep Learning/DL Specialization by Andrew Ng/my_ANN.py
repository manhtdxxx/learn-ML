import numpy as np


###
def initialize_params(units_each_layer: list[int]):
    np.random.seed(42)

    params = {}
    L = len(units_each_layer)  # number of layers
    for i in range(1, L):
        params[f'W{i}'] = np.random.randn(units_each_layer[i], units_each_layer[i-1]) * 0.01  # mean=0, std=0.01
        params[f'b{i}'] = np.zeros(shape=(units_each_layer[i], 1))
    return params


###
def sigmoid(Z):
    A = 1 / (1 + np.exp(-Z))
    cache = Z
    return A, cache

def relu(Z):
    A = np.maximum(0, Z)
    cache = Z
    return A, cache


###
def forward_linearly(A_prev, W, B):
    Z = W @ A_prev + B
    cache = (A_prev, W, B)
    return Z, cache


def forward_through_activation(A_prev, W, B, activation):
    if activation == 'sigmoid':
        Z, linear_cache = forward_linearly(A_prev, W, B)
        A, activation_cache = sigmoid(Z)
        
    elif activation == 'relu':
        Z, linear_cache = forward_linearly(A_prev, W, B)
        A, activation_cache = relu(Z)

    cache = (linear_cache, activation_cache)
    return A, cache


def forward(X, params):
    A = X  # X is the initial A
    L = len(params) // 2  # each layer linked with 2 params W, B
    
    caches = []
    
    # Forward Pass in Hidden Layers
    for i in range(1, L):
        A_prev = A
        W, B = params[f'W{i}'], params[f'B{i}']
        
        A, cache = forward_through_activation(A_prev, W, B, activation='relu')
        caches.append(cache)

    # Forward Pass in Output Layer
    W, B = params[f'W{L}'], params[f'B{L}']
    Y_pred, cache = forward_through_activation(A_prev, W, B, activation='sigmoid')
    caches.append(cache)

    return Y_pred, caches


###
def compute_cost(Y_pred, Y):  # Binary Cross-Entropy
    n_samples = Y.shape[1]
    cost = -(1/n_samples) * np.sum(Y * np.log(Y_pred) + (1-Y) * np.log(1-Y_pred))
    cost = np.squeeze(cost)  # turns [[cost]] into cost
    return cost


###
def backward_through_costFunc(Y, Y_pred, cost_func):
    """
    Y: (1, n_samples)
    Y_pred: (1, n_samples)
    """
    if cost_func == 'binary_cross_entropy':
        dY_pred = - (np.divide(Y, Y_pred) - np.divide(1-Y, 1-Y_pred))
    return dY_pred


def backward_through_activation(dA, activation_cache, activation):
    """
    dA: (n_features_out, n_samples)
    Z: (n_features_out, n_samples)
    """
    Z = activation_cache
    
    if activation == 'sigmoid':
        p = 1 / (1 + np.exp(-Z))
        dA_dZ = p * (1 - p)
        dZ = dA * dA_dZ

    elif activation == 'relu':
        dA_dZ = np.array(Z, copy=True)  
        dA_dZ[Z <= 0] = 0  # when Z <= 0, set dZ to 0
        dA_dZ[Z > 0] = 1  # when Z > 0, set dZ to 1
        dZ = dA * dA_dZ

    return dZ


def backward_linearly(dZ, linear_cache):
    """
    dZ: (n_features_out, n_samples)
    A_prev: (n_features_in, n_samples)
    W: (n_features_out, n_features_in)
    B: (n_features_out, 1)
    """
    A_prev, W, B = linear_cache
    
    n_samples = A_prev.shape[1]
    
    dW = (1/m) * (dZ @ A_prev.T)  # (n_features_out, n_samples) @ (n_samples, n_features_in)
    dB = (1/m) * np.sum(dZ, axis=1, keepdims=True)  # sum all samples each row of (n_features_out, n_samples)
    dA_prev = W.T @ dZ  # (n_features_in, n_features_out) @ (n_features_out, n_samples)

    return dA_prev, dW, dB


def backward_each_layer(dA, cache, activation):
    linear_cache, activation_cache = cache
    
    if activation == 'relu':
        dZ = backward_through_activation(dA, activation_cache, activation='relu')
    elif activation == 'sigmoid':
        dZ = backward_through_activation(dA, activation_cache, activation='sigmoid')

    dA_prev, dW, dB = backward_linearly(dZ, linear_cache)
    
    return dA_prev, dW, dB


def backward(Y, Y_pred, caches):  # Y shape (n_samples, )
    grads = {}
    L = len(caches)
    
    Y = Y.reshape(Y_pred.shape)  # Y and Y_pred must have the same shape (1, n_samples)
    dY_pred = backward_through_costFunc(Y, Y_pred, cost_func='binary_cross_entropy')
    
    last_cache = caches[-1]  # cache[L-1]
    dA_prev, dW, dB = backward_each_layer(dY_pred, last_cache, activation='sigmoid')
    grads[f'dA{L-1}'] = dA_prev
    grads[f'dW{L}'] = dW
    grads[f'dB{L}'] = dB

    for i in range(L-1, 0, -1):  # from L-1 to 1
        dA = dA_prev
        current_cache = caches[i-1]  # from cache[L-2] to cache[0]
        dA_prev, dW, dB = backward_each_layer(dA, current_cache, activation='sigmoid')
        grads[f'dA{i-1}'] = dA_prev  # to dA0
        grads[f'dW{i}'] = dW
        grads[f'dB{i}'] = dB

    return grads


###
def update_params(params, grads, learning_rate=0.01):
    L = len(params) // 2
    for i in range(1, L+1):
        params[f'W{i}'] = params[f'W{i}'] - learning_rate * grads[f'dW{i}']
        params[f'B{i}'] = params[f'B{i}'] - learning_rate * grads[f'dB{i}']

    return params
