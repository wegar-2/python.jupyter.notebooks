# import matplotlib.pyplot as plt
import pandas as pd

from src.datasets_generator import DatasetsGenerator
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import PredefinedSplit, GridSearchCV


if __name__ == "__main__":

    indep_df, dep_df = DatasetsGenerator.get_generic_regression_dataset(only_continuous_indep=True)
    sample_split = PredefinedSplit(test_fold=[0] * 1500 + [-1] * 500)

    dt_param_grid = {
        "max_depth": [2, 3, 5],
        "min_samples_split": [2, 5, 10, 20],
        "min_samples_leaf": [2, 5, 10]
    }

    # create grid search instance - put the components prepared above together
    # (1) use the mean absolute error as the scoring function
    # (2) use user-defined sample split (cf. above: first 1500 obs are the train set, other 500: test set)
    # (3) use the dictionary of hyperparameters defined above
    gs_cv = GridSearchCV(
        estimator=DecisionTreeRegressor(),
        param_grid=dt_param_grid,
        scoring="neg_mean_absolute_error",
        return_train_score=True,
        cv=sample_split,
        n_jobs=5
    )

    # run the grid search
    gs_cv.fit(X=indep_df, y=dep_df)

    # display info on the best model found in the grid search procedure
    best_model = gs_cv.best_estimator_
    print(isinstance(best_model, DecisionTreeRegressor))
    print(f"Best model's MAE: {-gs_cv.best_score_}")
    plot_tree(best_model)

    # plot predictions of the best models against real values
    y_hat_df = pd.DataFrame(data=best_model.predict(X=indep_df.loc[1500:, :])).rename(columns={0: "y_hat"})
    y_df = dep_df[1500:].reset_index(drop=True).rename(columns={"Y_1": "y"})
    predictions_df = pd.concat([y_df, y_hat_df], axis=1)
    predictions_df.plot.scatter(x="y", y="y_hat")

    # display info on the cross validation
    cv_results_df = pd.DataFrame(data=gs_cv.cv_results_)
