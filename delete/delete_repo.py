import boto3
import sys

def is_exist_repo(repo_nam):
    client = boto3.client('codecommit')
    try:
        response = client.get_repository(
            repositoryName=repo_nam
        )
        return True
    except Exception as e:
        pass
    return False

def delete_repo(name):
    client = boto3.client('codecommit')
    try:
        response = client.delete_repository(
            repositoryName=name
        )
        print("delete_repo result:")
        print(response)
    except Exception as e:
        pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage delete_repo.py <repo_nam> <SANDBOX_KEY> <TABLE_NAME>")
        sys.exit()
    repo_name=sys.argv[1]
    if is_exist_repo(repo_name):
        delete_repo(repo_name)
    else:
        print(f"{repo_name} 에는 존재하지 않습니다.")