from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
from ModelEvaluation import tryParameters
from VisualizeData import featureImportance, featuresCorrelation


def getPredictions(df, features, target):
    # Y
    target = df[target]
    # X

    df = df[features]

    trainFeatures, valFeatures, trainPredictionTarget, valPredictionTarget = train_test_split(
        df, target, random_state=0)

    # Only for evaluation, START
    # tryParameters(trainFeatures, valFeatures,
    #              trainPredictionTarget, valPredictionTarget)
    # Only for evaluation, END

    trainedModel = RandomForestRegressor(
        random_state=1477)

    trainedModel.fit(trainFeatures, trainPredictionTarget)

    # Test which features affect the prediction target the most
    #featureImportance(trainedModel, trainFeatures, 7)
    #featuresCorrelation(df, trainFeatures, trainPredictionTarget)

    modelPredictions = trainedModel.predict(
        valFeatures)

    return modelPredictions, valPredictionTarget, trainedModel
