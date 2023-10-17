import logging
import openai
import azure.functions as func

secret_key = "My API key"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # openai secret key 인증
    openai.api_key = secret_key

    # HTTP에서 변수 받기
    req_body = req.get_json()

    # openai api 부르기
    output = openai.ChatCompletion.create(
        model = req_body["model"],
        messages = req_body["messages"],
        max_tokens = req_body["max_tokens"],
        temperature = req_body["temperature"]
    )

    # 응답 포맷
    output_text = output.choices[0].message["content"].strip()

    # 응답 제공
    return func.HttpResponse(output_text, status_code=200)

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
