from bottle import get, post, route, run, template, view, static_file

@view('index')
@get('/')
def example():
    return template('index')

# Let's add some code to serve jpg images from our static images directory.
@post('/images/<filename:re:.*\.jpg>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

# Let's add some code to serve jpg images from our static images directory.
@get('/images/<filename:re:.*\.jpg>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

# Let's add some code to serve png images from our static images directory.
@post('/images/<filename:re:.*\.png>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/png')

# Let's add some code to serve png images from our static images directory.
@get('/images/<filename:re:.*\.png>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/png')

# Code for serving css stylesheets from /css directory.
@route('/css/<filename:re:.*.css>')
def serve_css(filename):
    return static_file(filename, root='css', mimetype='text/css')

run(host='localhost', port=8080, debug=True)
