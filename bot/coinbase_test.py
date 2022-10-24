from coinbase_commerce.client import Client


def coinbase_payment_url(name="", desc="", usd_amount=0):
    client = Client(api_key="cd899649-126e-4270-bdbb-0de249a40367")
    domain_url = 'http://localhost:8000/'
    product = {
        'name': name,
        'description': desc,
        'local_price': {
            'amount': str(usd_amount),
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
    }
    charge = client.charge.create(**product)

    return charge.hosted_url


url = coinbase_payment_url("NAME", "lorem ipsum", usd_amount=10)
print(url)