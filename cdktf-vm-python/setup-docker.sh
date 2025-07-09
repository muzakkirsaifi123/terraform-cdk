#!/bin/bash
set -eux

# Wait for cloud-init to fully initialize networking and apt
sleep 10

export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y docker.io

systemctl daemon-reexec
systemctl restart docker
systemctl enable docker
