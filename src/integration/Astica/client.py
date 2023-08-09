class StripeClient:
    def __init__(self):
        self.api = ctx.get_session(
            'StripeClient',
            host='https://api.stripe.com/v1/',
            headers={
                'Authorization': f'Bearer {config.stripe.api_key}',
            },
        )
