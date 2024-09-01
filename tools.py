from langchain.tools import BaseTool
import requests
import json

class ImageCaptionTool(BaseTool):
    name = "Image captioner"
    description = "Use this tool when given the path to an image that you would like to be described. " \
                  "It will return a simple caption describing the image."

    def _run(self, img_path):
        try:
            with open(img_path, 'rb') as image_file:
                api_url = "https://copilot5.p.rapidapi.com/copilot"
                api_key = "25c40aa56fmsh12b48be18760bb1p11101ejsn4236cc697a09"

                payload = {
                    "message": "Describe this image",
                    "conversation_id": None,
                    "tone": "BALANCED",
                    "markdown": False,
                    "photo_url": None
                }
                headers = {
                    "Content-Type": "application/json",
                    "x-rapidapi-host": "copilot5.p.rapidapi.com",
                    "x-rapidapi-key": api_key
                }

                response = requests.post(api_url, headers=headers, data=json.dumps(payload))
                
                if response.status_code == 200:
                    caption = response.json().get("caption", "No caption returned")
                else:
                    caption = f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            caption = f"Error loading image or contacting API: {e}"

        return caption

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")


class ObjectDetectionTool(BaseTool):
    name = "Object detector"
    description = "Use this tool when given the path to an image that you would like to detect objects. " \
                  "It will return a list of all detected objects. Each element in the list is in the format: " \
                  "[x1, y1, x2, y2] class_name confidence_score."

    def _run(self, img_path):
        try:
            with open(img_path, 'rb') as image_file:
                api_url = "https://copilot5.p.rapidapi.com/copilot"
                api_key = "25c40aa56fmsh12b48be18760bb1p11101ejsn4236cc697a09"

                payload = {
                    "message": "Detect objects in this image",
                    "conversation_id": None,
                    "tone": "BALANCED",
                    "markdown": False,
                    "photo_url": None
                }
                headers = {
                    "Content-Type": "application/json",
                    "x-rapidapi-host": "copilot5.p.rapidapi.com",
                    "x-rapidapi-key": api_key
                }

                response = requests.post(api_url, headers=headers, data=json.dumps(payload))

                if response.status_code == 200:
                    detections = response.json().get("detections", "No detections returned")
                else:
                    detections = f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            detections = f"Error loading image or contacting API: {e}"

        return detections

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")
