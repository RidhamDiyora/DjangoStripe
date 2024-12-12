from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY 
YOUR_DOMAIN = 'https://127.0.0.1:8000'

class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'
    

class CreateCheckoutSessionView(View):

    def post(self,request,*args,**kwargs):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'random',
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return JsonResponse({
            'id' : checkout_session.id,
        })
        
        
