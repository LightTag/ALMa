# ALMa - An Active Leanring (data) Manager

ALMa elimiates the need for bookkeeping when using Active Learning. Read the blog post
on [Active Learning with ALMa](https://www.lighttag.io/blog/active-learning-manager/)
 
Made with heart by LightTag - The Text Annotation Tool For Teams. 
We use ALMa to facilitate multi annotator active learning. Originally developed as a contribution for [Modal](https://github.com/modAL-python/modAL)
 but moved to it's own library 


## Install
```
pip install ALMa
```

## Use
Check out the full [example for text classification]('./examples/text_text_classification_with_modAL')
 
```python
from ALMa import ActiveLearningManager
manager = ActiveLearningManager(my_featurized_data, sources=optional_original_data)
learner = #...some active learning learner
for index in range(N_QUERIES):
    index_to_label, query_instance = learner.query(manager.unlabeld)
    original_ix = manager.get_original_index_from_unlabeled_index(index_to_label)
    y = original_labels_train[original_ix]
    label = (index_to_label, y)
    manager.add_labels(labels)
    learner.teach(X=manager.labeled, y=manager.labels)

```

