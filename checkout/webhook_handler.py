from django.http import HttpResponse


class StripeWH_Handler:
    # handles stripe webhooks
    def __init__(self, request):
        self.request = request

    # handles generic/unknown/unexpected webhook
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # handles payment_intent_succeeded webhook
    def handle_payment_intent_succeeded(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # handles payment_intent_payment_failed webhook
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
