import searchconsol
from pprint import pprint

sc_account = searchconsol.authenticate(client_config = 'client_secret.json')
web_property = sc_account['https://www.target.com/']
data = web_property.query.range('today', days=-14).dimension('query').get()
pprint(data.rows)































