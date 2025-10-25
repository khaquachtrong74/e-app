from flask import render_template, request

from eapp import app
import dao



@app.route('/')
def index():
    return render_template('index.html',
                           categories=dao.get_categories(),
                           products=dao.get_products(kw=request.args.get('kw'), category_id=request.args.get('category_id')))


if __name__ == '__main__':
    app.run(debug=True)
