from flask import Flask, request
from rough import analyze_invoice  # Replace 'your_module' with the actual module where analyze_invoice is defined

app = Flask(__name__)

@app.route('/', methods=['GET'])
def analyze_invoice_route():
    try:
        url = request.args.get('url')
        if not url:
            return 'Missing URL parameter'

        results = analyze_invoice(url)

        response_str = ""
        for label, result in results:
            response_str += "{}: {}\n".format(label, result.value)

        return response_str
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
