import numpy as np
import math

class NaiveBayes():


  def __init__(self):

    """ Setup useful datastructures
        Feel free to change this
    """

    self._word_counts = {}
    self._class_counts = {}
    self._priors = {}


  def fit(self, sample, indicator_booleans):
     """Fit a Multinomial NaiveBayes model from the training set (X, y).

        Parameters
        ----------
        X : array-like of shape = [n_samples]
            The training input samples.

        y : array-like, shape = [n_samples]

        Returns
        -------
        self : object
            Returns self.
      """
      for string in sample:
        words = string.split(' ')
        for word in word:
          if self._word_counts[word] is None:
            self._word_counts = 1
          else:
            self._word_counts[word] += 1

      for (string, class_boolean) in zip(sample, class_booleans):
        self._fit_instance(string, class_boolean)

      self._fit_priors()

  def _fit_priors(self):
    """Set priors based on data"""
    for word in self._word_counts.keys:
      for class_boolean in self._word_class_counts:
        if self._priors[class_boolean][word] is None:
          self._priors[class_boolean][word] = self._class_counts[class_boolean][word] / self._word_counts[word]

  def _fit_instance(self, field, class_boolean):
    """Train based on single samples       

     Parameters
        ----------
        instance : string = a line of text or single document
                   instance =  "This is not an insult"
                   instance = "You are a big moron"
        y : int = class of instance
                = 0 , 1 , class1, class2

      """
      for word in string.split(' '): 
        if self_class_counts[class_boolean][word] is None:
          self_class_counts[class_boolean][word] = 1
       else:
         self_class_counts[class_boolean][word] += 1



  def predict(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[int] = class per sample
    """

    return [self._predict_instance(x) for x in X]


  def predict_proba(self, X):
    """ Return array of class predictions for samples
      Parameters
      ----------
        X : array-like of shape = [n_samples]
            The test input samples.

        Returns
        -------
          : array[array[ float, float ... ], ...] =  class probabilities per sample 
    """

    return [ self._predict_instance(instance) for instance in X ]

  def _predict_instance(self, instance):
        """ Return array of class predictions for samples
      Parameters
      ----------
        instance : string = a line of text or single document

        Returns
        -------
          : array[ float, float ... ] =  class probabilities 
    """
    return [ self._compute_class_probability(instance, c) for all_classes]

  def _prior_prob(self, c):
    return self._priors[c]

  def _compute_class_probability(self, instance, c):
      """ Compute probability of instance under class c
        Parameters
        ----------
        instance : string = a line of text or single document

        Returns
        -------
          p : float =  class probability

      HINT : Often times, multiplying many small probabilities leads to underflow, a common numerical tricl
      is to compute the log probability.

      Remember, the log(p1 * p2 * p3) = log p1 + log p2 + log p3

      """

    words = instance.split(' ')
    prob = 0
    for word in words:
      prob += log(self._priors[c][word])
    return prob

if __name__ == '__main__':
  data = pd.read_csv('./train-utf8.csv')
  model = NaiveBayes()
  model.fit(data.Comment, data.Insult)

  print model.predict_proba(["This is not an insult", "You are a big moron"])