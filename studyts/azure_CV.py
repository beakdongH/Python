from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

prediction_endpoint= ""
prediction_key = ""
project_id= ""
model_name =  "Iteration1"
credentials =ApiKeyCredentials(in_headers={"Prediction-key":prediction_key})
predictor = CustomVisionPredictionClient(endpoint=prediction_endpoint,credentials=credentials)

image_file = ""
print('Detecting objects in ', image_file)
image = Image.open(image_file)
h,w,ch = np.array(image).shape
with open(image_file, mode="rb") as image_data:
    results = predictor.detect_image(project_id, model_name, image_data)
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))
fig = plt.figure(figsize =(8,8))
plt.axis('off')
draw = ImageDraw.Draw(image)
lineWidth = int(w/100)
color = 'magenta'

for prediction in results. predictions:
    if (prediction.probability*100) > 50:
        left = prediction.bounding_box.left * w
        top = prediction.bounding_box.top * h
        width = prediction.bounding_box.width * w
        height = prediction. bounding_box.height * h

        points =((left,top), (left+width,top),(left+width, top+height),(left,top+height),(left,top))
        draw.line(points, fill=color, width= lineWidth)
        plt.annotate(prediction.tag_name +'{0:2f}%'. format(prediction.probability * 100),(left,top),color=color)
    
plt.imshow(image)
outputfile = 'output.jpg'
fig. savefig(outputfile)
print('Results saved in', outputfile)
    
