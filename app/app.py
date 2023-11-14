from flask import Flask, request, render_template
from rough import analyze_invoice  # Replace 'your_module' with the actual module where analyze_invoice is defined

app = Flask(__name__)

@app.route('/', methods=['GET'])
def analyze_invoice_route():
    try:
        url = request.args.get('url')
        if not url:
            return render_template('result.html', error='Missing URL parameter')

        results = analyze_invoice(url)

        return render_template('result.html', results=results)
    except Exception as e:
        return render_template('result.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
