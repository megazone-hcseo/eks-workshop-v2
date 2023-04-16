import sys
import boto3

def get_key_id(delete_key_alias_name):
    client = boto3.client('kms')
    response = client.list_aliases(
    )
    for alias_info in response['Aliases']:
        if delete_key_alias_name == alias_info['AliasName']:
            print("find key : ", alias_info['TargetKeyId'])
            return alias_info['TargetKeyId']
    return None

def delete_key_alias(delete_key_alias_name):
    client = boto3.client('kms')
    try:
        response = client.delete_alias(
            AliasName=delete_key_alias_name
        )
    except Exception as e:
        pass

def schedule_key_deletion(delete_key_id):
    client = boto3.client('kms')
    response = client.schedule_key_deletion(
        KeyId=delete_key_id,
        PendingWindowInDays=7
    )
    print(f"schedule_key_deletion {response['KeyState']}")

def main(key_name):
    delete_key_alias_name=f"alias/{key_name}"
    delete_key_id = get_key_id(delete_key_alias_name)
    if delete_key_id is None:
        print(f"{delete_key_alias_name}가 존재하지 않습니다.")
        sys.exit()
    delete_key_alias(delete_key_alias_name)
    if delete_key_id is not None:
        schedule_key_deletion(delete_key_id)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage eks_kms_key_delete.py <key_name>")
    key_name=f"{sys.argv[1]}"
    main(key_name)
