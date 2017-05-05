

class MultiScorer():
	'''
	Use this class to encapsulate and/or aggregate multiple scoring functions so that it can be passed as an argument for scoring in scikit's cross_val_score function.
	Instances of this class are also callables, with signature as needed by cross_val_score.
	'''

	def __init__(self, metrics):
		'''
		Create a new instance of MultiScorer.


		Parameters
		----------
		metrics: dict
			The metrics to be used by the scorer.
			The dictionary must have as key a name (str) for the metric and as value a tuple containing the metric function itself and a dict literal of the additional named arguments to be passed to the function.
			The metric function should be one of the `sklearn.metrics` function or any other callable with the same signature: `metric(y_real, y, **kwargs)`.
		'''

		self.metrics = metrics
		self.results = {}
		self._called = False



	def __call__(self, estimator, X, y):
		'''
		To be called by for evaluation from sklearn's GridSearchCV or cross_val_score.
		Parameters are as they are defined in the respective documentation.

		Returns
		-------
			A dummy value of 0 just for compatibility reasons.
		'''

		yPred = estimator.predict(X)

		for key in self.metrics.keys():
			metric, kwargs = self.metrics[key]

			self.results[key] = metric(y, yPred, **kwargs)

		self._called = True

		return 0

	def get_metric_names(self):
		'''
		Get all the metric names as given when initialized

		Returns
		-------
		A list containing the given names (str) of the metrics 
		'''

		return self.metrics.keys()

	def get_results(self, metric=None):
		'''
		Get the results of a specific or all the metrics. This method should be called after the object itself has been called so that the metrics are applied.

		Parameters
		----------
		metric: str or None (default)
			The given name of a metric to return its result. If omitted the results of all metrics will be returned.

		Returns
		-------
		metric_result
			The result of the designated metric function, if `metric` parameter was not omitted.
			If  the value of `metric` does not correspond to a metric name, `None` will be returned.

		all_metric_results
			A dict having as keys the names of the metrics and as values their results.
			This will be returned only if `metric` parameter was omitted.

		Raises
		------
		UserWarning
			If this method is called before the instance is called for evaluation.
		'''

		if not self._called:
			raise UserWarning('Evaluation has not been performed yet.')

		if metric is not None:
			return self.results[metric]
		else:
			return self.results



