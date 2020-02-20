from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
from web_app.iris_stuff import classifier_model

"""has to be in a routs file.py"""
@new_routes.route("/iris")
def iris():
    X, y = load_iris(return_X_y=True)
    # print(X)
    # print(y)
    # clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X, y)
    clf = classifier_model(X, y)
    # print("CLASSIFIER", clf)
    results = clf.predict(X[:2, :])
    print("RESULTS", results)
    return str(results)
