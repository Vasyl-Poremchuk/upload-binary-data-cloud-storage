# Upload Binary Data Cloud Storage

## Description
A simple Flask app to upload binary data to Amazon S3 storage. Based on Python, Flask, and using Boto3.

## Installing using GitHub
```shell
git clone https://github.com/Vasyl-Poremchuk/upload-binary-data-cloud-storage
cd upload_binary_data_cloud_storage
python -m venv venv
venv\Scripts\activate (Windows) or source venv/bin/activate (Linux or macOS)
pip install -r requirements.txt
```

## Get Amazon S3 ACCESS KEY and SECRET ACCESS KEY
NOTE: You must have an existing AWS account.

1. Open the **IAM console**.
2. From the navigation menu, click **Users**.
3. Select your IAM user name.
4. Click **User Actions**, and then click **Manage Access Keys**.
5. Click **Create Access Key**.
6. Your keys will look something like this:
   * Access key ID example: **AKIAIOSFODNN7EXAMPLE**.
   * Secret access key example: **wJaIrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY**.
7. Click Download Credentials, and store the keys in a secure location.


## Configure AWS CLI
In the terminal, enter the command below:
```
aws configure
```
Then fill in the fields according to the sample below:
```
AWS Access Key ID [None]: YOUR_ACCESS_KEY_ID
AWS Secret Access Key [None]: YOUR_SECRET_KEY
Default region name [None]: YOUR_DEFAULT_REGION_NAME
Default output format [None]: You can leave this field blank
```

## Update BUCKET_NAME
Create a bucket in the AWS dashboard and change the value of the **BUCKET_NAME** variable in the app.py file.

## Run the application using the command below
```shell
python app.py
```
## Follow the URL below
http://127.0.0.1:5000/bucket

## Demo

![Website Interface](index.png)
![Website Interface](bucket.png)