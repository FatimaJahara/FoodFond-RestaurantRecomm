from django.shortcuts import render
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Recommend
from . forms import RecommendForm
from . serializers import RecommendSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

import numpy as np
import seaborn as sns
import nltk
import string
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords 
from nltk.tokenize import WordPunctTokenizer

class RecommendView(viewsets.ModelViewSet):
	queryset = Recommend.objects.all()
	serializer_class = RecommendSerializers
	

def text_process(mess):
	nltk.download('stopwords')
	stop = []
	nopunc = [char for char in mess if char not in string.punctuation]
	nopunc=''.join(nopunc)
	for word in stopwords.words('english'):
		s = [char for char in word if char not in string.punctuation]
		stop.append(''.join(s))
	return " ".join([word for word in nopunc.split() if word.lower() not in stop])



#@api_view(["POST"])
def Recommendations(words):
	try:
		df_business = pd.read_csv('F:\DjangoAPI_new\MyAPI\yelp_academic_dataset_business.csv', dtype='object')
		df = pd.read_csv('F:\DjangoAPI_new\MyAPI\yelp_academic_dataset_review.csv',dtype='object')
		df = df.loc[1:3000]
		df_business = df_business.loc[1:10000]
		R=[]
		S=[]
		T=[]
		with open('F:\DjangoAPI_new\MyAPI\yelp_recommendation_model_8.pkl', 'rb') as pickle_file:
			R=pickle.load(pickle_file)
			S=pickle.load(pickle_file) 
			T=pickle.load(pickle_file) 

		test_df= pd.DataFrame([words], columns=['text'])
		test_df['text'] = test_df['text'].apply(text_process)
		test_vectors = T.transform(test_df['text'])
		test_v_df = pd.DataFrame(test_vectors.toarray(), index=test_df.index, columns=T.get_feature_names())

		predictItemRating=pd.DataFrame(np.dot(test_v_df.loc[0],S.T),index=S.index,columns=['Rating'])
		topRecommendations=pd.DataFrame.sort_values(predictItemRating,['Rating'],ascending=[0])[:7]

		Name = []
		category = []
		Rating = []
		Review_count = []
		Reviews = []

		for i in topRecommendations.index:
			n = str(df_business[df_business['business_id']==i]['name'].iloc[0])
			Name.append(n)
			category.append(df_business[df_business['business_id']==i]['categories'].iloc[0])

			Rating.append(str(df_business[df_business['business_id']==i]['stars'].iloc[0]))
			Review_count.append(str(df_business[df_business['business_id']==i]['review_count'].iloc[0]))
			Reviews.append(str(df[df['business_id']==i]['text'].iloc[0]))

		
		result = list(zip(Name, category, Rating, Review_count, Reviews))                        
		show_result = pd.DataFrame(result, columns = ['Name','Category','Rating','Review_count','Review'])
		return (show_result)
	
	except ValueError as e:
		return (e.args[0])


def userpreferenceForm(request):
	if request.method == 'POST':
		form = RecommendForm(request.POST)
		if form.is_valid():
			userpreference = form.cleaned_data['userpreference']
			DataFrame = Recommendations(userpreference)
			print(DataFrame)
			#messages.success(request,f'{DataFrame}')
			return render(request,'recommender/dataframe.html',  {'DataFrame': DataFrame })

	else:
		form=RecommendForm()

	return render(request, 'recommender/preferenceform.html', {'form': form })