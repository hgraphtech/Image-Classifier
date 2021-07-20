Demo implementation of an image classifier using Flask and pytorch/fastai.

The classifier model is trained using transfer learning to fine tune a resnet model using labelled dog breed classification data.

To view the classifier on Heroku: https://hgraph-classifier.herokuapp.com/

To launch the webserver on localhost in development mode, install the dependencies and run:
export FLASK_APP=app
export FLASK_ENV=development
flask run
