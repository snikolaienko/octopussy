context = {}


def update_context(key, value):
    param = {key: value}
    context.update(param)


def get_context(key):
    return context.get(key)
