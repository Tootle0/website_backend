import random

from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Payment
from .forms import PaymentForm
from .serializers import PaymentSerializer


@api_view(['POST'])
@transaction.atomic
def payment_view(request,pk):
    serializer = PaymentSerializer(data=request.data)

    if serializer.is_valid():
        payment = serializer.save()

        # Симуляция оплаты
        if payment.card_number.isdigit() and int(payment.card_number) % 2 == 0 and not payment.card_number.endswith('0'):
            payment.status = 'Оплата прошла успешно'
        else:
            payment.status = 'Ошибка оплаты'
            payment.error_message = 'Случайная ошибка оплаты.'

        payment.save()

        return JsonResponse({'message': 'Ждём подтверждения оплаты от платёжной системы'})
    else:
        return JsonResponse({'error': serializer.errors}, status=400)












# @api_view(['POST'])
# def payment_view(request, pk):
#     form_template = 'frontend/payment.html'
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#
#         if form.is_valid():
#             card_number = form.cleaned_data['card_number']
#             payment_type = form.cleaned_data['payment_type']
#
#             if payment_type == 'Онлайн со случайного чужого счёта':
#                 random_account_number = str(random.randint(10000000, 99999999))
#                 response_data = {'Случайный номер счёта': random_account_number}
#                 form_template = 'frontend/paymentsomeone.html'
#             elif int(card_number) % 2 == 0 and not card_number.endswith('0'):
#                 response_data = {'message': 'Ожидается подтверждение оплаты'}
#             else:
#                 response_data = {'error': 'Ошибка оплаты'}
#
#             Payment.objects.create(
#                 card_number=card_number,
#                 name=form.cleaned_data['name'],
#                 month=form.cleaned_data['month'],
#                 year=form.cleaned_data['year'],
#                 code=form.cleaned_data['code'],
#                 payment_type=payment_type,
#             )
#
#             return render(request, form_template, response_data)
#         else:
#             return JsonResponse({'error': form.errors}, status=400)
#     else:
#         form = PaymentForm()
#
#         return render(request, form_template, {'form': form})