from google.cloud import storage


def cors_configuration(bucket_name):
    """Set a bucket's CORS policies configuration."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.cors = [
        {
            "origin": ["*"],
            "responseHeader": ["Content-Type", "x-goog-resumable"],
            "method": ["PUT", "POST", "GET"],
            "maxAgeSeconds": 3600,
        }
    ]
    bucket.patch()

    print("Set CORS policies for bucket {} is {}".format(bucket.name, bucket.cors))
    return bucket

# 구글 스토리지 compute@developer.gserviceaccount.com의 키를 json으로 받은 후 아래 경로에 추가!
# Windows: $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/ryan/GCP/service_key_master.json"


cors_configuration("shrinkers-bucket-fc")
