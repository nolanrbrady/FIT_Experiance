import datetime
from haystack import indexes
from portal.core.fit.models import Resource


class LibraryResourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    dimension = indexes.CharField(model_attr='dimension__name')
    subcategory = indexes.CharField(model_attr='subcategory__text', faceted=True)
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')

    def get_model(self):
        return Resource

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created__lte=datetime.datetime.now())
