#!/bin/bash
docker buildx build --platform linux/amd64 -t hummus404/book_store --push .

ssh -i ~/.ssh/umut_cloud_deployment.pem ec2-user@35.179.133.219 << 'EOF'

docker stop book_store_hubv || true
docker rm book_store_hubv || true

docker pull hummus404/book_store

docker run -d --name book_store_hubv --network book_store_network -p 5001:5001 hummus404/book_store
EOF
