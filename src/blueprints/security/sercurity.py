

def auth(request):
    access_token = None
    try:
        access_token = request.headers['Authorization']
    except:...

    if not access_token:
        return {'message': 'Access-Token não encontrado'}, 401
    try:
        ...
    except:
        return {'message': 'Access-Token inválido'}, 401
