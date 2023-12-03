from django.http import HttpResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DepositProductOptionSerializer, DepositProductSerializer, SavingProductOptionSerializer, SavingProductSerializer, FilterSavingOptionSerializer, FilterOptionSerializer
from .models import DepositProducts, FilteringSavingOptions, SavingProducts, DepositOptions, SavingOptions, FilteringOptions 

# @api_view(['GET'])
# def deposits (request):
#     res = requests.get('https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth=72624f4493711e1a4b021f735bffa37e&topFinGrpNo=020000&pageNo=1')
#     baselist = res.json()['result']['baseList']
#     optionlist = res.json()['result']['optionList']

#     for li in baselist:
#         save_data = {
#             'fin_prdt_cd': li.get('fin_prdt_cd'),
#             'fin_co_no': li.get('fin_co_no'),
#             'kor_co_nm': li.get('kor_co_nm'),
#             'fin_prdt_nm': li.get('fin_prdt_nm'),
#             'etc_note' : li.get('etc_note'),
#             'join_deny' : li.get('join_deny'),
#             'join_member' : li.get('join_member'),
#             'join_way' : li.get('join_way'),
#             'spcl_cnd' : li.get('spcl_cnd'),
#             'mtrt_int': li.get('mtrt_int'),
#         }

#         serializer = DepositProductSerializer(data=save_data)
#         if serializer.is_valid():
#             serializer.save()

#     for li in optionlist:
#         save_data = {
#             'product' : li.get('product'),
#             'fin_prdt_cd' : li.get('fin_prdt_cd'),
#             'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
#             'intr_rate' : li.get('intr_rate'),
#             'intr_rate2' : li.get('intr_rate2'),
#             'save_trm' : li.get('save_trm'),
#         }

#         serializer = DepositOptionSerializer(data = save_data)

#         if serializer.is_valid(raise_exception=True):
#             product = DepositProducts.objects.get(fin_prdt_cd = save_data.get('fin_prdt_cd'))
#             serializer.save(product=product)

#     return Response(serializer.data)

# @api_view(['GET'])
# def savings(request):
#     res = requests.get('https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth=72624f4493711e1a4b021f735bffa37e&topFinGrpNo=020000&pageNo=1')
#     baselist = res.json()['result']['baseList']
#     optionlist = res.json()['result']['optionList']


#     for li in baselist:
#         save_data = {
#             'fin_prdt_cd': li.get('fin_prdt_cd'),
#             'fin_co_no': li.get('fin_co_no'),
#             'kor_co_nm': li.get('kor_co_nm'),
#             'fin_prdt_nm': li.get('fin_prdt_nm'),
#             'etc_note' : li.get('etc_note'),
#             'join_deny' : li.get('join_deny'),
#             'join_member' : li.get('join_member'),
#             'join_way' : li.get('join_way'),
#             'spcl_cnd' : li.get('spcl_cnd'),
#             'mtrt_int': li.get('mtrt_int'),
#         }

#         serializer = SavingProductSerializer(data=save_data)
#         if serializer.is_valid():
#             serializer.save()

#     for li in optionlist:
#         save_data = {
#             'product' : li.get('product'),
#             'fin_prdt_cd' : li.get('fin_prdt_cd'),
#             'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
#             'intr_rate' : li.get('intr_rate'),
#             'intr_rate2' : li.get('intr_rate2'),
#             'save_trm' : li.get('save_trm'),
#             'rsrv_type_nm' : li.get('rsrv_type_nm'),
#         }

#         serializer = SavingOptionSerializer(data = save_data)

#         if serializer.is_valid(raise_exception=True):
#             product = SavingProducts.objects.get(fin_prdt_cd = save_data.get('fin_prdt_cd'))
#             serializer.save(product=product)

#     return Response(serializer.data)

# def hocheol(request):
#     for product in DepositProducts.objects.all():
#         options = DepositOptions.objects.filter(product=product.pk)
#         new_table_data = {
#             'kor_co_nm': product.kor_co_nm,
#             'fin_prdt_nm': product.fin_prdt_nm,
#             'fin_prdt_cd': product.fin_prdt_cd,
#             'save_trm6': options.filter(save_trm=6).first().intr_rate if options.filter(save_trm=6).exists() else None,
#             'save_trm12': options.filter(save_trm=12).first().intr_rate if options.filter(save_trm=12).exists() else None,
#             'save_trm24': options.filter(save_trm=24).first().intr_rate if options.filter(save_trm=24).exists() else None,
#             'save_trm36': options.filter(save_trm=36).first().intr_rate if options.filter(save_trm=36).exists() else None,
#         }
#         FilteringOptions.objects.create(**new_table_data)

#     return HttpResponse()

# def hocheol2(request):
#     for product in SavingProducts.objects.all():
#         options = SavingOptions.objects.filter(product=product.pk)
#         new_table_data = {
#             'kor_co_nm': product.kor_co_nm,
#             'fin_prdt_nm': product.fin_prdt_nm,
#             'fin_prdt_cd': product.fin_prdt_cd,
#             'save_trm6': options.filter(save_trm=6).first().intr_rate if options.filter(save_trm=6).exists() else None,
#             'save_trm12': options.filter(save_trm=12).first().intr_rate if options.filter(save_trm=12).exists() else None,
#             'save_trm24': options.filter(save_trm=24).first().intr_rate if options.filter(save_trm=24).exists() else None,
#             'save_trm36': options.filter(save_trm=36).first().intr_rate if options.filter(save_trm=36).exists() else None,
#         }
#         FilteringSavingOptions.objects.create(**new_table_data)

#     return HttpResponse()

@api_view(['GET'])
def filteredOptions(request):
    deposit = FilteringOptions.objects.all()
    serializer = FilterOptionSerializer(deposit, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filteredSavingOption(request):
    saving = FilteringSavingOptions.objects.all()
    serializer = FilterSavingOptionSerializer(saving, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit(request):
    deposit = DepositProducts.objects.all()
    serializer = DepositProductSerializer(deposit, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving(request):
    deposit = SavingProducts.objects.all()
    serializer = SavingProductSerializer(deposit, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ddd(request):
    deposit = DepositOptions.objects.all()
    serializer = DepositProductOptionSerializer(deposit, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dddd(request):
    deposit = SavingOptions.objects.all()
    serializer = SavingProductOptionSerializer(deposit, many=True)
    return Response(serializer.data)