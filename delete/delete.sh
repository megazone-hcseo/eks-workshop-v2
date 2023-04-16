#!/usr/bin/env bash

python3 delete_repo.py eks-workshop-gitops
python3 delete_dynamodb_table.py eks-workshop-carts
python3 eks_kms_key_delete.py eks-workshop-cmk
python3 delete_log_group.py /aws/lambda/eks-workshop-cloud9-bootstrap
python3 eks_kms_key_delete.py eks-workshop
python3 eks_kms_key_delete.py eks-workshop-cw-fluent-bit
