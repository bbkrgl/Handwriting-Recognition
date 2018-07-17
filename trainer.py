from sklearn import datasets, svm

dataset = datasets.load_digits()

n_samples = len(dataset.images)
X_train = dataset.images.reshape(n_samples, -1)
y_train = dataset.target

clf = svm.SVC()

clf.fit(X_train[:n_samples], y_train[:n_samples])


def predict(test):
    clf.predict(test)
