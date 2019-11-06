from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import random
from tensorflow.keras.models import load_model
from PIL import Image
import os


def uploadFile(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return context


def imreadx(url, img_name):
    img = io.imread(url)
    outimg = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(img_name, outimg)

    return outimg


def imshowx(img, title='B2DL'):
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 12
    fig_size[1] = 4
    plt.rcParams["figure.figsize"] = fig_size

    plt.axis('off')
    plt.title(title)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


def imshowgrayx(img, title='BD2L'):
    plt.axis('off')
    plt.title(title)
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    plt.show()

def cropAndDetectTrafficSign(context):
    currentPythonFilePath = os.getcwd()
    modelUrl = currentPythonFilePath+'/static/model/model.h5'
    url = currentPythonFilePath + context['url']

    imageType = url.split('.')[1]
    tds_img = 'lastimage.'+imageType

    img = imreadx(url, tds_img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_r1 = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
    mask_r2 = cv2.inRange(hsv, (160, 100, 100), (180, 255, 255))
    mask_r = cv2.bitwise_or(mask_r1, mask_r2)
    target = cv2.bitwise_and(img, img, mask=mask_r)
    gblur = cv2.GaussianBlur(mask_r, (9, 9), 0)
    edge_img = cv2.Canny(gblur, 30, 150)
    img2 = img.copy()
    itmp, cnts, hierarchy = cv2.findContours(
        edge_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2, cnts, -1, (0, 255, 0), 2)
    img2 = img.copy()
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if(area < 1000):
            continue
        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(img2, ellipse, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(cnt)
        a, b, c, d = x, y, w, h
        cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 3)
    crop = img[b:b+d, a:a+c]

    model = load_model(modelUrl)
    data = []
    image_from_array = Image.fromarray(crop, 'RGB')
    crop = image_from_array.resize((30, 30))
    data.append(np.array(crop))
    X_test = np.array(data)
    X_test = X_test.astype('float32')/255
    prediction = model.predict_classes(X_test)
    return prediction

def detectTrafficSign(request):
    context = uploadFile(request)
    prediction = cropAndDetectTrafficSign(context)
    context['traffictrainid'] = prediction[0]
    return context
