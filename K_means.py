import math
import random
import matplotlib.pyplot as plt
import numpy as np


points =  [(1.0,1.0),(1.0,2.0),(2.0,2.0),(2.0,3.0),(4.0,4.0),(4.0,5.0),(5.0,5.0),(5.0,4.0)]

def getInitialCentroids(centroids):
    for i in range(2):
        centroids.append(random.choice(points))
    print(centroids)
    return centroids

def euclidean(centroid, points):
    
    ls = []
    print("points: ", points)
    for point in points:
        print(centroid,point)
        t1 = (point[0]-centroid[0])*(point[0]-centroid[0]) 
        t2 =  (point[1]-centroid[1])*(point[1]-centroid[1])
        print(t1,t2)
        sum1 =  t1+t2
        print(sum1)
        ans =  math.sqrt(sum1)
        ls.append(ans)
        

    print(ls)
    return ls


centroids = []
# getInitialCentroids(centroids)
centroids = [(1,1),(2,3)]
# ans  = euclidean(centroids[0],points)


def pointsCloserToCentroid(dist1,dist2):
    ls = []
    for i in range(len(dist1)):
        dist_cent_1 = dist1[i]
        dist_cent_2 =  dist2[i]
        if dist_cent_1 < dist_cent_2:
            ls.append(0)
        else:
            ls.append(1)
    print(ls)
    return ls


def getClusters(ls,points):
    cluster1 = []
    cluster2 = []

    for i in range(len(ls)):
        if(ls[i]==0):
            cluster1.append(points[i])
        else:
            cluster2.append(points[i])

    clusters = []
    clusters.append(cluster1)
    clusters.append(cluster2)

    return clusters



dist1 =  euclidean(centroids[0],points)
dist2 =  euclidean(centroids[1],points)
ls = pointsCloserToCentroid(dist1,dist2)    
clusters = getClusters(ls,points) # now we have initial clusters



def getCentroids(cluster1,cluster2):
    sum_x = 0
    sum_y = 0
    for point in cluster1:
        sum_x =  sum_x + point[0]
        sum_y =  sum_y + point[1]
    centroid1 = ((sum_x/len(cluster1)) , (sum_y/len(cluster1)))
    

    sum_x = 0
    sum_y = 0
    for point in cluster2:
        sum_x =  sum_x + point[0]
        sum_y =  sum_y + point[1]
    centroid2 = ((sum_x/len(cluster2)) , (sum_y/len(cluster2)))

    centroids = []
    centroids.append(centroid1)
    centroids.append(centroid2)
    return centroids




for i in range(0,2):
    centroids = getCentroids(clusters[0],clusters[1])
    print(centroids)
    dist1 =  euclidean(centroids[0],points)
    dist2 =  euclidean(centroids[1],points)
    ls = pointsCloserToCentroid(dist1,dist2)    
    clusters = getClusters(ls,points) 
    print("clusters  :",clusters)


