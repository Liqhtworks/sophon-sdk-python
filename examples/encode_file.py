import os
import sys
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

import sophon_sdk
from sophon_sdk.models.create_job_request import CreateJobRequest


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        response = urllib.request.addinfourl(fp, headers, req.get_full_url())
        response.code = code
        return response

    http_error_301 = http_error_303 = http_error_307 = http_error_302


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python examples/encode_file.py /path/to/video.mov")

    api_key = os.environ["SOPHON_API_KEY"]
    base_url = os.getenv("SOPHON_BASE_URL", "https://api.liqhtworks.xyz")
    input_path = Path(sys.argv[1])
    mime_type = "video/quicktime" if input_path.suffix == ".mov" else "video/mp4"

    configuration = sophon_sdk.Configuration(host=base_url, access_token=api_key)
    with sophon_sdk.ApiClient(configuration) as api_client:
        uploads = sophon_sdk.UploadsApi(api_client)
        jobs = sophon_sdk.JobsApi(api_client)

        upload = sophon_sdk.upload_file(
            uploads,
            input_path,
            file_name=input_path.name,
            mime_type=mime_type,
            concurrency=4,
        )

        job = sophon_sdk.create_job(
            jobs,
            idempotency_key=str(uuid.uuid4()),
            create_job_request=CreateJobRequest(
                source=sophon_sdk.JobSource.upload(upload.upload_id),
                profile="sophon-espresso",
            ),
        )
        print(f"created {job.id}")

        final = sophon_sdk.wait_for_job(
            jobs,
            job.id,
            timeout_seconds=30 * 60,
            on_progress=lambda j: print(f"job {j.id}: {j.status}"),
        )
        if final.status != "completed":
            raise RuntimeError(f"job ended in {final.status}")

    req = urllib.request.Request(
        f"{base_url}/v1/jobs/{final.id}/output",
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    opener = urllib.request.build_opener(NoRedirectHandler())
    redirect = opener.open(req)
    location = redirect.headers.get("Location")
    if not location:
        raise RuntimeError("missing output redirect")

    download_url = urllib.parse.urljoin(base_url.rstrip("/") + "/", location)
    with urllib.request.urlopen(download_url, timeout=60) as download:
        Path("sophon-output.mp4").write_bytes(download.read())

    print("wrote sophon-output.mp4")


if __name__ == "__main__":
    main()
