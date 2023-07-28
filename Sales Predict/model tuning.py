from sklearn.model_selection import GridSearchCV

# Example: Hyperparameter tuning for Random Forest
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
}

grid_search = GridSearchCV(estimator=random_forest_model, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

best_random_forest_model = grid_search.best_estimator_
