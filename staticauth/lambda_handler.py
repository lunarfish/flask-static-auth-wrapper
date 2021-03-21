import serverless_wsgi

from . import bootstrap


def lambda_handler(event, context):
    """
    Lambda handler entry point
    """
    return serverless_wsgi.handle_request(bootstrap(), event, context)
