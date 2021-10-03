from .apps.v1.views.welcome import Welcome


def initialize_routes(api):
    api.add_resource(Welcome, '/')