# hd3
Django app to deploy ML models

Dataset: Heart Disease (https://archive.ics.uci.edu/ml/datasets/Heart+Disease)

This Jupyter Notebook contains the data preprocessing, model training, and model pickling.
https://github.com/hainesma/ML_models/blob/master/Heart_Disease_Pickling.ipynb

I used k-nearest neighbors to create the predictive model. It gives a binary classification.

I've exported the model with Pickle and HDF5. Still figuring out how to deploy the model in the Django app.

This repository contains the Django app itself. 
I'm following a few different tutorials:

First, the Django Girls tutorial for creating a Django app (https://tutorial.djangogirls.org/en/).

Second, this one on deploying ML models in Django by Piotr Płoński (https://www.deploymachinelearning.com/).

I'm currently working through the second tutorial, just copying what he's done using his ML model, and then I'm planning to figure out how to do it with my heart disease predictor.

The part I'm stuck at now is where he puts the ML code into the server (https://www.deploymachinelearning.com/#ml-code-in-the-server).
When I run the test at the end of that section, it fails.
