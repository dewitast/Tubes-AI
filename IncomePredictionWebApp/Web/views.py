# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from sklearn.externals import joblib

# Create your views here.
def index(req):
	return render(req, 'Web/index.html', {})

def process(req):
	wcs = ['Federal-gov', 'Local-gov', 'Never-worked', 'Not-worked', 'Private', 'Self-emp-inc', 'Self-emp-not-inc', 'State-gov', 'Without-pay']
	edus = ['10th', '11th', '12th', '1th-4th', '5th-6th', '7th-8th', '9th', 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Doctorate', 'HS-grad', 'Masters', 'Preschool', 'Prof-school', 'Some-college']
	mss = ['Divorced', 'Married-AF-spouse', 'Married-civ-spouse', 'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed']
	ocs = ['Adm-clerical', 'Armed-Forces', 'Craft-repair',
		'Exec-managerial', 'Farming-fishing', 'Handlers-cleaners', 'Machine-op-inspct', 'None', 'Other-service', 'Priv-house-serv', 'Prof-specialty', 'Protective-serv', 'Sales',
		'Tech-support', 'Transport-moving']
	rels = ['Husband', 'Not-in-family', 'Other-relative', 'Own-child', 'Unmarried', 'Wife']
	rcs = ['Amer-Indian-Eskimo', 'Asian-Pac-Islander', 'Black', 'Other', 'White']
	sxs = ['Female', 'Male']
	ncs = ['Cambodia', 'Canada', 'China', 'Columbia', 'Cuba', 'Dominican-Republic', 'Ecuador', 'El-Salvador', 'England', 'France', 'Germany', 'Greece', 'Guatemala', 'Haiti',
		'Holand-Netherlands', 'Honduras', 'Hong', 'Hungary', 'India', 'Iran', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Laos', 'Mexico', 'Nicaragua', 'Other-country',
		'Outlying-US(Guam-USVI-etc)', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto-Rico', 'Scotland', 'South', 'Taiwan', 'Thailand', 'Trinadad&Tobago', 'United-States',
		'Vietnam', 'Yugoslavia']
	age = req.POST['age']
	fnlwgt = req.POST['fnlwgt']
	edunum = req.POST['education-num']
	gain = req.POST['capital-gain']
	loss = req.POST['capital-loss']
	hours = req.POST['hours-per-week']
	workclass = wcs.index(req.POST['workclass'])
	edu = edus.index(req.POST['education'])
	marital = mss.index(req.POST['marital-status'])
	occ = ocs.index(req.POST['occupation'])
	relationship = rels.index(req.POST['relationship'])
	race = rcs.index(req.POST['race'])
	sex = sxs.index(req.POST['sex'])
	native = ncs.index(req.POST['native-country'])
	inp = [int(age), int(fnlwgt), int(edunum), int(gain), int(loss), int(hours)]
	for i in range(0, 102):
		inp.append(0)
	inp[6 + workclass] = 1
	inp[15 + edu] = 1
	inp[31 + marital] = 1
	inp[38 + occ] = 1
	inp[53 + relationship] = 1
	inp[59 + race] = 1
	inp[64 + sex] = 1
	inp[66 + native] = 1
	model = joblib.load('model.pkl')
	pred = model.predict(inp)
	if (pred[0] == 0):
		return HttpResponse('<=50K')
	else :
		return HttpResponse('>50K')