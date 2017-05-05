# multiscorer
#### A module for allowing the use of multiple metric functions in scikit's `cross_val_score`.

As it has been discussed, Python's _SciKit_, while it contains a great functionality for computing evaluation metrics of estimators (using cross_val_score),
it seems to fail when it comes to computing multiple metrics for the same classifier without trainning it again

The problem arises because of the `scoring` parameter of the function which accepts only a single metric name or a single callable.

Module _multiscorer_ of this repo, is a workaround for using any number of metrics in _cross_eval_score_.


## Installation

To "install" the module simply download the source code and place it in your project's directory.
(Alternativelly, download and add to your project just _multiscorer.py_ file.

## Usage

From a Python script, you can write:
```Python
from multiscorer import MultiScorer

#Scikit's libraries for demonstration
from sklearn.metrics import *
from sklearn.model_selection import cross_val_score

scorer = MultiScorer({
  'accuracy': (accuracy_score, {}),
  'precision': (precision_score, {'average': 'macro'})
})

cross_val_score(clf, X, target, scoring=scorer )

results = scorer.getResults()

for metric in results.keys():
  print("%s: %.3f" % (metric, results[metric]))

```

## Notes
- You can also use your own custom metric functions.
- For a full documentation see Wiki
- Original documentation of SciKit: 
