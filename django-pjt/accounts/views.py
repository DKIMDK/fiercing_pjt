from django.shortcuts import get_list_or_404, get_object_or_404
from banks.models import DepositProducts, SavingProducts
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import numpy as np
import pandas as pd
from .models import User
from .serializers import RecommendSerializer, SavingSerializer
from implicit.als import AlternatingLeastSquares
from sklearn.preprocessing import LabelEncoder
from scipy.sparse import csr_matrix
from banks.models import DepositProducts
from banks.models import SavingProducts
from .serializers import RecommendSerializer
from collections import Counter
import json
from rest_framework.decorators import api_view
from sklearn.cluster import KMeans

@api_view(['POST'])
def get_recommended_deposit_products (request):
    user_data = request.data
    # user_data = {'age' : 30, 'salary': 52000000, 'asset': 200000000}
    print(request.data)
    user_df = pd.DataFrame([user_data])

    users = User.objects.all()
    serializer = RecommendSerializer(users, many=True)
    serialized_data = serializer.data
    df = pd.DataFrame.from_records(serialized_data)
    df.drop(['saving_products'], axis=1, inplace=True)

    df = pd.concat([df,user_df])

    X = df[['age','asset','salary']].values
    print(X)
    NUM_CLUSTERS = 100
    kmeans = KMeans(n_clusters=NUM_CLUSTERS)
    clusters = kmeans.fit_predict(X)
    df['group'] = clusters

    user_cluster = df.iloc[-1]['group']

    users_in_cluster = df[df['group'] == user_cluster].dropna()

    # recommended_products = users_in_cluster['deposit_products'].tolist()

    recommended_products = [product for products in users_in_cluster['deposit_products'] for product in products]

    # Count occurrences of each product
    product_counts = Counter(recommended_products)

    # Get the top 5 most common products
    top_products = [product for product, count in product_counts.most_common(7)]

    deposit_products_ids = top_products
    deposit_products_info = DepositProducts.objects.filter(id__in=deposit_products_ids).values('kor_co_nm', 'fin_prdt_nm')    
    deposit_products_info_list = list(deposit_products_info)
    response_data = {'recommended_deposit_products_info': deposit_products_info_list}
    

   
    
    return JsonResponse(response_data)



@api_view(['POST'])
def get_recommended_saving_products (request):
    user_data = request.data
    # user_data = {'age' : 30, 'salary': 52000000, 'asset': 200000000}
    user_df = pd.DataFrame([user_data])

    users = User.objects.all()
    serializer = RecommendSerializer(users, many=True)
    serialized_data = serializer.data
    df = pd.DataFrame.from_records(serialized_data)
    df.drop(['deposit_products'], axis=1, inplace=True)

    df = pd.concat([df,user_df])

    X = df[['age','asset','salary']].values
    print(X)
    NUM_CLUSTERS = 100
    kmeans = KMeans(n_clusters=NUM_CLUSTERS)
    clusters = kmeans.fit_predict(X)
    df['group'] = clusters

    user_cluster = df.iloc[-1]['group']

    users_in_cluster = df[df['group'] == user_cluster].dropna()

    # recommended_products = users_in_cluster['deposit_products'].tolist()

    recommended_products = [product for products in users_in_cluster['saving_products'] for product in products]

    # Count occurrences of each product
    product_counts = Counter(recommended_products)

    # Get the top 5 most common products
    top_products = [product for product, count in product_counts.most_common(7)]

    saving_products_ids = top_products
    saving_products_info = DepositProducts.objects.filter(id__in=saving_products_ids).values('kor_co_nm', 'fin_prdt_nm')    
    saving_products_info_list = list(saving_products_info)
    response_data = {'recommended_saving_products_info': saving_products_info_list}
    

   
    
    return JsonResponse(response_data)


@api_view(['POST'])
def databaseSaving(request, saving_pk):
    isTrue = request.data['isTrue']
    user = User.objects.get(username=request.user)
    deposit_option = SavingProducts.objects.get(fin_prdt_cd=saving_pk)
    if isTrue == 1:
        user.saving_products.add(deposit_option)
    else:
        user.saving_products.remove(deposit_option)
    return HttpResponse()

@api_view(['POST'])
def databaseDeposit(request, deposit_pk):
    isTrue = request.data['isTrue']
    user = User.objects.get(username=request.user)
    depoosit_option = DepositProducts.objects.get(fin_prdt_cd=deposit_pk)
    if isTrue == 1:
        user.deposit_products.add(depoosit_option)
    else:
        user.deposit_products.remove(depoosit_option)
    return HttpResponse()

@api_view(['GET'])
def savingsend(request):
    user = get_list_or_404(User, username=request.user)
    serializer = SavingSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def depositsend(request):
    user = get_list_or_404(User, username=request.user)






