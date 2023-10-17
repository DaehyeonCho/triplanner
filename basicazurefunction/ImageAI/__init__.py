import logging
import openai
import azure.functions as func

secret_key = "My API key"
# 생성 샘플
# {"prompt" : "Goku running though a field", "n" : 1, "size" : "1024x1024"}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # openai secret key 인증
    openai.api_key = secret_key

    # HTTP에서 변수 받기
    req_body = req.get_json()

    # openai api 부르기
    output = openai.Image.create(
        prompt = req_body["prompt"],
        n = req_body["n"],
        size = req_body["size"]
    )

    # 응답 포맷
    output_text = output["data"][0]["url"]

    # 응답 제공
    return func.HttpResponse(output_text, status_code=200)

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
