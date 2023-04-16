import sys
import boto3

def is_exist_table(table_name):
    client = boto3.client('dynamodb')
    try:
        response = client.describe_table(
            TableName=table_name
        )
        return True
    except Exception as e:
        pass
    return False


def delete_table(table_name):
    client = boto3.client('dynamodb')
    try:
        response = client.delete_table(
            TableName=table_name
        )
        print("delete_table result:")
        print(response)
    except Exception as e:
        pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage delete_dynamodb_table.py <table_name>")
        sys.exit()
    table_name=sys.argv[1]
    if is_exist_table(table_name):
        delete_table(table_name)
    else:
        print(f"{table_name} 은 존재하지 않습니다.")
