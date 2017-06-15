# multiscorer
#### A module for allowing the use of multiple metric functions in scikit's `cross_val_score`.

As it has been discussed, Python's _SciKit_, while it contains a great functionality for computing evaluation metrics of estimators (using **cross_val_score**),
it seems to fail when it comes to computing multiple metrics for the same classifier without trainning it again.

The problem arises because of the `scoring` parameter of the function which accepts only a single metric name or a single callable.

Module _multiscorer_ of this repo, is a workaround for using any number of metrics in *cross_val_score*.


## Installation

To "install" the module simply download the source code and place it in your project's directory.  
(*Alternativelly, download and add to your project just **multiscorer.py** file*).

## Usage

From a Python script, you can write:
```Python
from multiscorer import MultiScorer

#Scikit's libraries for demonstration
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import cross_val_score
from numpy import average

scorer = MultiScorer({
  'accuracy': (accuracy_score, {}),
  'precision': (precision_score, {'average': 'macro'})
})

...

cross_val_score(clf, X, target, scoring=scorer )

results = scorer.get_results()

for metric in results.keys():
  print("%s: %.3f" % (metric, average(results[metric])))

```

## Notes
- You can get results only from specific metrics and/or specific folds ([see examples](https://github.com/StKyr/multiscorer/wiki/Examples) ).
- You can also use your own custom metric functions ([see how](https://github.com/StKyr/multiscorer/wiki/Examples#using-custom-metrics-in-multiscorer)).
- For a full documentation see [Wiki](https://github.com/StKyr/multiscorer/wiki).
- Original documentation of SciKit: http://scikit-learn.org/stable/

## Development and Contributing
This module was something I had the need for while working with Scikit's libraries and I just thought it might help somebody.  
For questions, bugs, suggestions etc, feel free to contact me or submit a Pull Request.
