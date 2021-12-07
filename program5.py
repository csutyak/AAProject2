#imports
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

def program5():

    #Read in data
    ccdata = pd.read_csv('BankChurners.csv')

    #display column names
    #columns_names = ccdata.columns.tolist()
    #print("Columns names: ")
    #print(columns_names)

    #Display correlations
    #"df.corr() compute pairwise correlation of columns.Correlation shows how the two variables are related to each other.
    #Positive values shows as one variable increases other variable increases as well. Negative values shows as one variable 
    #increases other variable decreases.Bigger the values,more strongly two varibles are correlated and viceversa."
    correlation = ccdata.corr()
    #plt.figure(figsize=(10,10))
    #sns.heatmap(correlation, vmax=1, square = True, annot = True, cmap = 'cubehelix')

    #Existing = 0
    #Attrited = 1

    #Male = 0
    #Female = 1

    ccdata_drop = ccdata.drop(labels = ['Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category'], axis = 1)
    ccdata_drop.head()

    #reshapes the data, separating features
    X = ccdata_drop.iloc[:,0:16].values
    y = ccdata_drop.iloc[:,0].values

    #print(np.shape(y))
    #print(np.shape(X))

    #Standardizes the data
    from sklearn.preprocessing import StandardScaler
    X_std = StandardScaler().fit_transform(X)

    mean_vec = np.mean(X_std, axis=0)
    cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
    #print('Covariance matrix \n%s' %cov_mat)

    eig_vals, eig_vecs = np.linalg.eig(cov_mat)

    #print('Eigenvectors \n%s' %eig_vecs)
    #print('\nEigenvalues \n%s' %eig_vals)

    # Make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

    # Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs.sort(key=lambda x: x[0], reverse=True)

    # Visually confirm that the list is correctly sorted by decreasing eigenvalues
    #print('Eigenvalues in descending order:')
    #for i in eig_pairs:
    #    print(i[0])

    #Explained Variance
    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    #print(var_exp)

    #with plt.style.context('dark_background'):
    #    plt.figure(figsize=(6, 4))
    #
    #    plt.bar(range(16), var_exp, alpha=0.5, align='center',
    #            label='individual explained variance')
    #    plt.ylabel('Explained variance ratio')
    #    plt.xlabel('Principal components')
    #    plt.legend(loc='best')
    #    plt.tight_layout()

    matrix_w = np.hstack((eig_pairs[0][1].reshape(16,1), 
                        eig_pairs[1][1].reshape(16,1),
                        eig_pairs[2][1].reshape(16,1),
                        eig_pairs[3][1].reshape(16,1)
                    ))
    #print('Matrix W:\n', matrix_w)

    Y = X_std.dot(matrix_w)

    from sklearn.decomposition import PCA
    pca = PCA().fit(X_std)
    #plt.plot(np.cumsum(pca.explained_variance_ratio_))
    #plt.xlim(0,15,1)
    #plt.xlabel('Number of components')
    #plt.ylabel('Cumulative explained variance')

    #Another way to do PCA
    sklearn_pca = PCA(n_components=16)
    Y_sklearn = sklearn_pca.fit_transform(X_std)
    #print(Y_sklearn)
    #print(Y_sklearn.shape)

    print("Success")
