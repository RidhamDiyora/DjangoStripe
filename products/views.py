from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY 
YOUR_DOMAIN = 'https://127.0.0.1:8000'

class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'
    
    def get_context_data(self, **kwargs):
        product = Product.objects.get(name='Test Product')
        context =  super(ProductLandingPageView.self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY" : settings.STRIPE_PUBLIC_KEY
        })
        return context

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
