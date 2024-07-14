# webhook.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import uvicorn
import logging
import base64
import os



app = FastAPI()


@app.post("/label/deployment")
async def mutate(request: Request) -> json:
    """
    On pod creation or update, will patch each of them with the labels
    provided in the configmap

    Args:
        request (Request): Request from the k8s API by the webhook

    Returns:
        json: Patch in a json format to return to the k8s API
    """
    request_json = await request.json()
    logging.info(f"Received request: {request_json}")
    
    ingested_labels: str = os.getenv('LABELS')
    labels: json = json.loads(ingested_labels)
    
    patches: list = [
        {
            "op": "add",
            "path": f"/spec/template/metadata/labels/{key}",
            "value": value
        }
        for key, value in labels.items()
    ]
    
    patch_str: str = json.dumps(patches)
    patch_bytes: bytes = patch_str.encode('utf-8')
    patch_base64: base64 = base64.b64encode(patch_bytes).decode('utf-8')
    
    admission_review_response: dict = {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": request_json["request"]["uid"],
            "allowed": True,
            "patchType": "JSONPatch",
            "patch": patch_base64
        }
    }
    
    logging.info(f"Sending response: {admission_review_response}")
    return JSONResponse(admission_review_response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
