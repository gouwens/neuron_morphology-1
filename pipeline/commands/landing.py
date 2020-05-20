import os
import zipfile
import io
import uuid
from datetime import datetime
from typing import Optional

import boto3

from harness import step_fns_ecs_harness


s3 = boto3.client("s3")


def extract_reconstruction_id(key: str):
    """The reconstruction id is the name of the upload package
    """
    return key.split("/")[-1].split(".")[0]


def landing(token: Optional[str] = None):
    """Extract a zip archive of pipeline inputs from the landing bucket and 
    transfer them to the working bucket. Generate an id for this run.

    Returns
    -------
    a dictionary:
        base_key : The prefix of the unzipped object keys in the working bucket
        bucket_name : the working bucket's name
        reconstruction_id : The identifier of this reconstruction
        run_id : A generated identifier for this pipeline run

    """
    working_bucket = os.environ["WORKING_BUCKET"]
    landing_bucket = os.environ["LANDING_BUCKET"]
    upload_package_key = os.environ["UPLOAD_PACKAGE_KEY"]

    run_id = str(uuid.uuid4())
    reconstruction_id = extract_reconstruction_id(upload_package_key)
    now = datetime.now().strftime(r"%Y-%m-%d-%H-%M-%S")
    base_key = f"{reconstruction_id}/{now}_{run_id}"

    upload_package_response = s3.get_object(
        Bucket=landing_bucket, Key=upload_package_key
    )

    archive = zipfile.ZipFile(
        io.BytesIO(
            upload_package_response["Body"].read()
        )
    )

    for name in archive.namelist():
        s3.put_object(
            Body=archive.read(name),
            Bucket=working_bucket,
            Key=f"{base_key}/{name}"
        )

    s3.delete_object(Bucket=landing_bucket, Key=upload_package_key)

    return {
        "base_key": base_key,
        "bucket_name": working_bucket,
        "reconstruction_id": reconstruction_id,
        "run_id": run_id
    }


def main():
    step_fns_ecs_harness(landing)


if __name__ == "__main__":
    main()