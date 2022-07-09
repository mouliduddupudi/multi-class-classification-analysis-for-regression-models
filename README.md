# Multiclass Classification Analysis For Regression Models

After doing a regression analysis on a dataset using different models, there is need to know in what range of values the each model is performing better
than the other. Each model captures patterns in the data differently. So, each model may predict different value for the same sample. 

To check these ranges, the multliclassification on the regression predictions has to be done. 
The main advantage of doing this is to know which model is able to capture/ perform well on what range of values. If one model is doing good on certain range
and another model on the other, then ensembling the models may result in predicting all the values correctly.

A keen analysis on which model is performing good on what range of values will helps in understanding of the model and in finalizing it. 

# Example

![An example inference result](LogPgenTrain.png)


Here the results are normalized to look the percentages, If you want to see actual number of values in that range, please remove np.sum in the code.

**If you find any mistakes or disagree with any of the explanations, please do not hesitate to submit an issue. I welcome any feedback, positive or negative!**
