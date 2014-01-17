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
    # print 'indicator_booleans ' + str(set(indicator_booleans)) 
    total_word_count = float(len(' '.join(sample).split(' ')))
    for class_boolean in list(set(indicator_booleans)):
      self._class_per[class_boolean] = 0
      self._class_counts[class_boolean] = {}
      self._priors[class_boolean] = {}

    for (string, class_boolean) in zip(sample, indicator_booleans):
      # print 'zipped: ' + str(zip(sample, indicator_booleans))
      num_items = len(string.split(' '))
      item_count += num_items 
      # print 'item_count: ' + str(item_count)
      self._class_per[class_boolean] += num_items
      # print "class_per_hash: " + str(self._class_per)

      self._fit_instance(string, class_boolean)
      # self._clean_hashes(class_boolean)

    # print 'total_word_count' + str(total_word_count)
    for key in self._class_per.keys():
      # print 'key:' + str(key)
      # print 'num_items ' + str(num_items)
      self._class_per[key] = self._class_per[key]/total_word_count
      # print '_class_per: ' + str(self._class_per)
    # print self._class_per
    self._fit_priors()

  def _fit_priors(self):
    """Set priors based on data"""
    boolean_set = self._class_per.keys()
    for class_boolean in boolean_set:
      for word in self._class_counts[class_boolean].keys():
        word_count = 0
        for sum_boolean in boolean_set:
          if self._class_counts[sum_boolean].get(word) is not None:
            word_count += self._class_counts[sum_boolean][word]
        self._priors[class_boolean][word] = (self._class_counts[class_boolean][word]/float(word_count)) / float(self._class_per[class_boolean])
        print ''
        print 'WordClassCount: ' + str(self._class_counts[class_boolean][word])
        print 'WordCount: ' + str(word_count)
        print 'Calculated val: ' + str(self._priors[class_boolean][word])
        print 'Class percentage: ' + str(self._class_per[class_boolean])

  def _fit_instance(self, field, class_boolean):
    for word in field.split(' '):
      if self._class_counts[class_boolean].get(word) is None:
        self._class_counts[class_boolean][word] = 1
        # print 'class_boolean: ' + str(class_boolean)
        # print 'word: ' + word
        # print str(self._class_counts[class_boolean][word])
      else:
        self._class_counts[class_boolean][word] += 1
        # print 'class_boolean: ' + str(class_boolean)
        # print 'word: ' + word
        # print str(self._class_counts[class_boolean][word])
    # print str(class_boolean)

  def _clean_hashes(self, class_boolean):
    self._class_counts[class_boolean]['a'] = 1
    self._class_counts[class_boolean]['the'] = 1
    self._class_counts[class_boolean]['this'] = 1
    self._class_counts[class_boolean]['are'] = 1

  def predict(self, X):
    print 'predict ' + str(X)
    return [self._predict_instance(x) for x in X]


  def predict_proba(self, X):
    print 'predict_proba ' + str(X)
    return [ self._predict_instance(instance) for instance in X ]

  def _predict_instance(self, instance):
    print '_predict_instance ' + str(instance)
    return [ self._compute_class_probability(instance, c) for c in self._class_per.keys()]

  def _prior_prob(self, c):
    return self._priors[c]

  def _compute_class_probability(self, instance, c):
    words = instance.split(' ')
    prob = 1
    # print self._priors
    for word in words:
      # print 'WORD: ' + word
      # print 'val: ' + str(self._priors[c][word])
      val = self._priors[c][word]
      if val != 0:
        prob = prob * self._priors[c][word]
    prob = prob / math.log(self._class_per[c])
    # print 'PROB: ' + str(prob)
    # return prob

if __name__ == '__main__':
  data = pd.read_csv('./train-utf8.csv')
  model = NaiveBayes()
  model.fit(list(data.Comment), list(data.Insult))
  print model.predict_proba(["This is not an insult", "You are a big moron"])