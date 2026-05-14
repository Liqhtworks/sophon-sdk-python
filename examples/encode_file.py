import os
import sys
import uuid
from pathlib import Path

import sophon_sdk
from sophon_sdk import CreateJobRequest


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python examples/encode_file.py /path/to/video.mov")

    api_key = os.environ["SOPHON_API_KEY"]
    base_url = os.getenv("SOPHON_BASE_URL", "https://api.liqhtworks.xyz")
    input_path = Path(sys.argv[1])

    configuration = sophon_sdk.Configuration(host=base_url, access_token=api_key)
    with sophon_sdk.ApiClient(configuration) as api_client:
        uploads = sophon_sdk.UploadsApi(api_client)
        jobs = sophon_sdk.JobsApi(api_client)

        upload = sophon_sdk.upload_file(
            uploads,
            input_path,
            file_name=input_path.name,
            concurrency=4,
        )

        job = sophon_sdk.create_job(
            jobs,
            idempotency_key=str(uuid.uuid4()),
            create_job_request=CreateJobRequest(
                source=sophon_sdk.JobSource.upload(upload.upload_id),
                profile=sophon_sdk.JOB_PROFILE_SOPHON_ESPRESSO,
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

    sophon_sdk.download_output(
        base_url=base_url,
        api_key=api_key,
        job_id=final.id,
        dest=Path("sophon-output.mp4"),
    )
    print("wrote sophon-output.mp4")


if __name__ == "__main__":
    main()
