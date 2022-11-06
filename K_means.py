import math
import random
import matplotlib.pyplot as plt
import numpy as np


def getInitialCentroids(centroids, points):
    for i in range(2):
        centroids.append(random.choice(points))
    print(centroids)
    return centroids

def euclidean(centroids, point):
    ls = []
    # print("points: ", points)
    for centroid in centroids:
        # print(centroid,point)
        t1 = (point[0]-centroid[0])*(point[0]-centroid[0])  # (x2-x1)^2
        t2 =  (point[1]-centroid[1])*(point[1]-centroid[1]) # (y2-y1)^2
        # print(t1,t2)
        sum1 =  t1+t2 # (x2-x1)^2 + (y2-y1)^2
        # print(sum1)
        ans =  math.sqrt(sum1)
        ls.append(ans)
        
    return ls

# Generalising the approach to fit 'n' number of clusters
def clusterAssignmentDecisionAndPopulation(n, distances, points):
    
    # Array of Arrays having points in each cluster
    clusters = dict()    
    for i in range(len(distances)):
        clusters[i] = []
    for i in range(len(distances)):
        # Check which centroid is the point closest to -
        minDist = min(distances[i]) 
        for j in range(0, len(distances[i])):
            if(distances[i][j]==minDist):
                # print("HERE - ", type(clusters.get(j)))
                # print("Point", type(points[i]))
                array = clusters.get(j)
                array.append(points[i])
                clusters[j] = array
                # print("Value", clusters.get(j))
    return clusters

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


# MAIN METHOD - 
points =  [(1.0,1.0),
           (1.0,2.0),
           (2.0,2.0),
           (2.0,3.0),
           (4.0,4.0),
           (4.0,5.0),
           (5.0,5.0),
           (5.0,4.0),
           (4.0,1.0),
           (4.0,2,0),
           (5.0,1.0),
           (5.0,2,0),
           ]

centroids = []
# getInitialCentroids(centroids)
centroids = [(1,1),(2,3)]

distances = []
for i in points:
    distances.append(euclidean(centroids, i))

clusters = clusterAssignmentDecisionAndPopulation(3, distances, points)

for i in range(0,2):
    centroids = getCentroids(clusters[0],clusters[1])
    distances = []
    for i in points:
        distances.append(euclidean(centroids, i))
    clusters = clusterAssignmentDecisionAndPopulation(3, distances, points)
    
for i in range(0, 8):
    if clusters.get(i) != []:
        print("Elements in cluster ", i, " are", clusters.get(i))
