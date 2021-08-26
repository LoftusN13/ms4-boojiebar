from django.http import HttpResponse


class StripeWH_Handler:
    # handles stripe webhooks
    def __init__(self, request):
        self.request = request

    # handles generic/unknown/unexpected webhook
    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
