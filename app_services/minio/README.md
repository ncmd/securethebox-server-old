# Install Minio Server and Client
https://min.io/download#/macos


Server:
brew install minio/stable/minio


Client:
brew install minio/stable/mc

Python SDK:
pip install minio


 1. Start minio server on "/home/shared" directory.
     $ minio server /home/shared

  2. Start minio server bound to a specific ADDRESS:PORT.
     $ minio server --address 192.168.1.101:9000 /home/shared

  3. Start minio server and enable virtual-host-style requests.
     $ export MINIO_DOMAIN=mydomain.com
     $ minio server --address mydomain.com:9000 /mnt/export

  4. Start erasure coded minio server on a node with 64 drives.
     $ minio server /mnt/export{1...64}`