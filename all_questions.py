# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative is less sensitive to outliers \
        and make less assumptions about the shape of the clusters. K-means"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "k-means is randomly initialized, agglomerative are not"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Not necessarily, and not always. There are some fast agglomerative methods."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "It will decrease"

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Yes, it means the total variance in the distances of all the points in a centroid have decreased."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "Yes - that's what ssb measures, the distance between the centroids."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Yes, k-mmeans knows nothing about cohesion and separation, only variance, and may improve one metric and not the other."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE + BSS is the total sum of squares, which is dependent on the data, not the clustering"

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Yes, as SSE + SSB must always be equal to the total sum of squares."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Clearly the global minimum for two points and especially given the placement of the initial centroids is at the center of the two circles"

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Each cluster will have some points from the tips of the other crescents, and the centroids won't be in the true center of each crescent due to this."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The middle point will be too far away from the other points (which will be closer to the other two centroids)"

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "2*4*(R**2+(R/2)**2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "A and C will become part of the leftmost and rightmost centroids, and as such the centroids will eventually converge to the centers of each circle"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "C will become part of the rightmost centroid, and will drag the centroid over towards its center, after which the middle centroid will converge onto B."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Leftmost centroid will be between A and B, the right two will split C evenly."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set(["Group A","Group B"])

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "They are the closest and share structural similarities (contiguity)"

    # type: set
    answers["(b)"] = set(["Group A","Group C"])

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "They have the closest furthest points"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set(["C","E","B","F","I","J","L","M"])

    # type: set
    answers["(a) boundary"] = set(["G","D"])

    # type: set
    answers["(a) noise"] = set(["A","H"])

    # type: set
    answers["(b) cluster 1"] = set(["F","E","C","B","D","G"])

    # type: set
    answers["(b) cluster 2"] = set(["I","J","L","M"])

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set(["C","E","B","F","I","J","L","M","D","G"])

    # type: set
    answers["(c)-a boundary"] = set(["A","H"])

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set(["F","E","C","B","D","G","A"])

    # type: set
    answers["(c)-b cluster 2"] = set(["I","J","L","M","H"])

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Most evenly distributed across all classes"

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "More pure (mostly water)"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Bluer colors in the middle two indicate higher cohesion, as in B, C"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "More uniformity of the colors indicates good cohesion in all of the clusters. Distances correspond nicely with the distances shown on the graph"

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "lower cohesion in A and D is clearly shown in lesser-uniformity of squares."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "distances increase as we go to bottom left and upper right corner, indicating the row clusters from A - D."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "A lot less cohesion in A and D, differentiating it from Dataset Z. Similar cohesion however in B and C."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Similar distances between adjacent clusters, shown by the cyan squares. Far distances reflected by B-D, A-B,A-D, C-D, and C-B."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Each value increases in distance, suggesting it is A or D. It is A because the second entry is more cohesive than the third, correspondent to B"

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Given the conclusions from the first row, this must be B, as it is more cohesive than C, and less cohesive than A."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Given the conclusions from the first row, this must be C, as it is more cohesive than D, and less cohesive than B."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Given the conclusions from the first row, this must be D, as it is less cohesive than A, and less cohesive than C."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical','Overlapping','Partial']

    # type: list
    answers["(b)"] = ['Partitional','Exclusive','Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'Fuzzy', 'Complete']

    # type: list
    answers["(d)"] = ['Hierarchical', 'Overlapping', 'Partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "dbscan finds highly dense structures, which figure a is lacking in the eyes, nose, and mouth. On the other hand, figure b is dense in the eyes, nose, and mouth relative to the rest of the data."
    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "With the right K, the clusters would certainly center on the facial features in figure b, but not a due to lack of dense structures in the facial features."

    # type: string
    answers["(c)"] = "use the inverse density and use kmeans with k=4 or dbscan."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
