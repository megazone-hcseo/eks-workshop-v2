import sys
import boto3

def is_log_group(log_group_name):
    client = boto3.client('logs')
    try:
        response = client.describe_log_groups(
            logGroupNamePattern=log_group_name
        )
        return True
    except Exception as e:
        pass
    return False


def delete_log_group(log_group_name):
    client = boto3.client('logs')
    try:
        response = client.delete_log_group(
            logGroupName=log_group_name
        )
        print("delete_log_group result:")
        print(response)
    except Exception as e:
        print(f"{log_group_name} 은 존재하지 않습니다.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage delete_log_group.py <log_group_name>")
        sys.exit()
    log_group_name=sys.argv[1]
    if is_log_group(log_group_name):
        delete_log_group(log_group_name)
    else:
        print(f"{log_group_name} 은 존재하지 않습니다.")
