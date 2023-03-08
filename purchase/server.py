from chrome import chrome_purchase as cPurchase
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/purchase', methods=['POST'])
def purchase_event():
	print(request.form)
	url = request.form.get('url')
	if url is not None:
		sPurchase = cPurchase.ChromePurchase()
		msg = sPurchase.addToShoppingCard(url)
		return Response(msg)
	else:
		return "Not purchase URL", 400	

	

if __name__ == "__main__":
	app.run(host='0.0.0.0', threaded=True, port = 5001)
