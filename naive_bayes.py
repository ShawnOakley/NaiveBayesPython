import numpy as np
import math
import pandas as pd

class NaiveBayes():

  def __init__(self):
    self._class_per = {}
    self._class_counts = {}
    self._priors = {}

  def fit(self, sample, indicator_booleans):
    item_count = 0
    for class_boolean in set(indicator_booleans):
      self._class_per[class_boolean] = 0
      self._class_counts[class_boolean] = {}
      self._priors[class_boolean] = {}

    for (string, class_boolean) in zip(sample, indicator_booleans):
      num_items = len(string.split(' '))
      item_count += num_items 
      self._class_per[class_boolean] += num_items

      self._fit_instance(string, class_boolean)

    for key in self._class_per.keys():
      self._class_per[key] = self._class_per[key]/num_items
    self._fit_priors()

  def _fit_priors(self):
    """Set priors based on data"""
    for class_boolean in self._class_counts.keys():
      for word in self._class_counts[class_boolean].keys():
        self._priors[class_boolean][word] = self._class_counts[class_boolean][word] / self._class_per[class_boolean]

  def _fit_instance(self, field, class_boolean):
      for word in field.split(' '): 
        if self._class_counts[class_boolean].get(word) is None:
          self._class_counts[class_boolean][word] = 1
        else:
          self._class_counts[class_boolean][word] += 1

  def predict(self, X):
    return [self._predict_instance(x) for x in X]


  def predict_proba(self, X):
    return [ self._predict_instance(instance) for instance in X ]

  def _predict_instance(self, instance):
    return [ self._compute_class_probability(instance, c) for c in self._class_per.keys()]

  def _prior_prob(self, c):
    return self._priors[c]

  def _compute_class_probability(self, instance, c):
    words = instance.split(' ')
    prob = 0
    for word in words:
      print word
      val = self._priors[c][word]
      print val
      if val != 0:
        prob += math.log(self._priors[c][word])
    prob -= math.log[self._class_per[c]]
    return prob

if __name__ == '__main__':
  data = pd.read_csv('./train-utf8.csv')
  model = NaiveBayes()
  model.fit(list(data.Comment), list(data.Insult))
  print model.predict_proba(["This is not an insult", "You are a big moron"])