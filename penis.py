import gdown
import os

# Set the file path of the .pth file on the remote server
remote_file_path = '/home/ubuntu/epn/EPN_PointCloud/trained_models/models/playground/model_20240511_15:01:54/ckpt/playground_net_Iter30000.pth'

# Set the desired name for the file in Google Drive
drive_file_name = 'playground_net_Iter30000.pth'

# Set the path where the file will be temporarily downloaded on the remote server
temp_file_path = '/tmp/' + drive_file_name

# Download the file to the temporary location on the remote server
os.system(f'cp {remote_file_path} {temp_file_path}')

# Upload the file to Google Drive
url = 'https://drive.google.com/uc?id=' + gdown.upload(temp_file_path, quiet=False)

# Remove the temporary file from the remote server
os.remove(temp_file_path)

print(f"File uploaded to Google Drive: {url}")