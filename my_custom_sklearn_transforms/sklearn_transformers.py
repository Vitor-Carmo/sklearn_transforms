from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')


    
class AvgColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
       

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        for column in self.columns:
            data[column].fillna(data[column].mean(), inplace=True)
        return data
    

class FillNaNColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns, fill=0):
        self.columns = columns
        self.fill = fill

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        for column in self.columns:
            data[column].fillna(self.fill, inplace=True)
        return data




class FixColumnsOverTen(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        for column in self.columns:
            data.loc[data[column] > 10, column] = 10
        return data
        
 
