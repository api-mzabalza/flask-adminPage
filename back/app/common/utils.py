
def validator(schema, params):
    errors = schema().validate(params)
    if errors:
        return {'message': 'Error','Error': errors}
    return f(*args, **kwargs)

