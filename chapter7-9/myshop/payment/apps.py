from django.apps import AppConfig


class PaymentConfig(AppConfig):
    # for computer
    name = 'payment'

    # for human reading 
    verbose_name = 'Payment'

    def aready(self, ):
        # import signal handlers
        import payment.signals
