from datetime import datetime
from random import random

import numpy as np
from django.http import HttpResponse
from django.views import View
from sklearn.cluster import KMeans


class MyView(View):
    def get(self, request, cpu):
        kmeans(cpu)

        return HttpResponse()


def kmeans(cpu=-1):
    print("start kmeans cpus: {}".format(cpu))
    X = []
    for i in range(100000):
        X.append([float("{0:.2f}".format(random())), float("{0:.2f}".format(random()))])

    X = np.array(X)
    start = datetime.now()
    print("INIT")
    kmeans = KMeans(n_clusters=100, n_jobs=cpu).fit(X)
    end = datetime.now()
    diff = (end - start).total_seconds()
    print("END time: {}".format(diff))
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return centroids
