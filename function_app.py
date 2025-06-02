import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="test_123_madhav")
def test_123_madhav(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}. Welcome")
    else:
        return func.HttpResponse("Welcome Anyways")

# for the local function testing, we can initiate the command func start, copy the localhost URL and paste into postman with key value pair of "name":"value"