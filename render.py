import requests

url = "https://api.rendernet.ai/pub/v1/generations"

payload = [
    {
        "aspect_ratio": "1:1",
        "batch_size": 1,
        "cfg_scale": 7,
        "character": {"character_id": "chr_01", "weight": 0.6, "enable_facelock": True},
        "control_net": {
            "asset_id": "ast_01",
            "control_mode": 0,
            "name": "Normal",
            "resize_mode": 0,
        },
        "facelock": {"asset_id": "ast_01"},
        "loras": [{"name": "lora_name", "weight": 0.5}],
        "model": "JuggernautXL",
        "narrator": {
            "image_asset_id": "ast_imgxxxxx",
            "video_asset_id": "ast_vidxxxxx",
            "audio_asset_id": "ast_audxxxxx",
            "script": "Thank you for trying Narrator",
            "voice": "Rachel",
        },
        "prompt": {
            "negative": "nsfw, deformed, extra limbs, bad anatomy, deformed pupils, text, worst quality, jpeg artifacts, ugly, duplicate, morbid, mutilated",
            "positive": "a man looking into the camera",
        },
        "quality": "Plus",
        "sampler": "DPM++ 2M Karras",
        "seed": 1234,
        "segment": {"asset_id": "ast_01", "find": "red shirt", "replace": "blue shirt"},
        "steps": 20,
        "style": "Bokeh",
        "style_detail": {"name": "Black & White", "base_model": "flux"},
        "true_touch": {
            "asset_id": "ast_01",
            "enhance_strength": 0.5,
            "scale_factor": 1.5,
        },
    }
]
headers = {
    "X-API-KEY": "9tUI7nn7WqLTFnlmDeFot9u4H8XykwIXXQHMbTFgLkU",
    "Content-Type": "application/json",
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
