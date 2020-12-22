#https://scikit-learn.org/stable/developers/develop.html

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import euclidean_distances

class classifiertemplate(BaseEstimator, ClassifierMixin):

    def __init__(self, demo_param='demo'):
        self.demo_param = demo_param

    def fit(self, X, y):

        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X_ = X
        self.y_ = y
        # Return the classifier
        return self

    def predict(self, X):

        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        closest = np.argmin(euclidean_distances(X, self.X_), axis=1)
        return self.y_[closest]

    def predict_proba(self, X):

        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        #closest = np.argmin(euclidean_distances(X, self.X_), axis=1)
        #return self.y_[closest]
        distances = euclidean_distances(X, self.X_)
        distances_sum = np.sum(distances,axis=0)
        #distances_normalized = distances/distances_sum.reshape((distances.shape(2),1))
        #bins = np.arange(1,np.unique(self.y_))
        distances_normalized = np.kron(np.ones((distances.shape[0],1)), distances_sum)
        
        #bins = np.arange(0,np.unique(self.y_).shape[0])
        #two classes
        bins = [0, 0.5, 1]

        labels = np.kron(np.ones((distances.shape[0],1)), self.y_)
        h=[]
        for i in range(0,distances_normalized.shape[0]):
            h.append( np.histogram(labels[i], bins, weights=distances_normalized[i])[0])
        h = np.asarray(h)
        return h

    def get_params(self, deep=True):
        # suppose this estimator has parameters "alpha" and "recursive"
        return {"alpha": self.alpha, "recursive": self.recursive}

    def set_params(self, **parameters):
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self