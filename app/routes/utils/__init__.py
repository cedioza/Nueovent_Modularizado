import flask


utils=flask.Blueprint('utils',__name__)

# error 404
@utils.errorhandler(404) 
def invalid_route(e): 
    return flask.jsonify({'Message' : 'Error 404 Ruta no encontrada intenta nuevamente'})

# error 405
@utils.errorhandler(405) 
def invalid_route(e): 
    return flask.jsonify({'Message' : f'Error 405 Metodo {request.method} no esta permitido '})