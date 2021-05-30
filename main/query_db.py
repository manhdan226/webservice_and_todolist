import boto3 

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:4566")
database_name = "todo_list"
database_count = "todo_list_COUNT"
table_todo = dynamodb.Table(database_name)
count_todo = dynamodb.Table(database_count)

# 
def get_all_task():
    data = []
    scanResponse = table_todo.scan(TableName=database_name)
    items = scanResponse['Items']
    for item in items:
        data.append(item)
    return data

def create_task(new_task):
    id = str(count_todo.item_count + 1)
    count_item = {"id": id}
    count_todo.put_item(Item=count_item)
    new_task["id"] = id
    table_todo.put_item(Item=new_task)
    return get_all_task()

def get_task_by_id(id):
    res = table_todo.get_item(Key = {'id': id}, ConsistentRead=True)["Item"]
    return res

def update_task(update_info, id):
    try:
        table_todo.update_item(Key = {"id": id},
                    UpdateExpression = "set task=:t",
                    ExpressionAttributeValues = {':t': update_info["task"]})
        print("Updated task to ", update_info["task"])
    except:
        print("---Can't update task")
    
    try:
        table_todo.update_item(Key = {"id": id},
                    UpdateExpression = "set description=:d",
                    ExpressionAttributeValues = {':d': update_info["description"]})
        print("Updated description to ", update_info["description"])
    except:
        print("---Can't update description")
    
    try: 
        table_todo.update_item(Key = {"id": id},
                    UpdateExpression = "set progress=:p",
                    ExpressionAttributeValues = {':p': update_info["progress"]})
        print("Updated progress to ", update_info["progress"])
    except:
        print("---Can't update progress")
    
    try:
        table_todo.update_item(Key = {"id": id},
                    UpdateExpression = "set deadline=:de",
                    ExpressionAttributeValues = {':de': update_info["deadline"]})
        print("Updated deadline to ", update_info["deadline"])
    except:
        print("---Can't update deadline")

    try:
        table_todo.update_item(Key = {"id": id},
                    UpdateExpression = "set assignee=:as",
                    ExpressionAttributeValues = {':as': update_info["assignee"]})
        print("Updated assignee to ", update_info["assignee"])
    except:
        print("---Can't update assignee")
    
    return get_all_task()

def delete_task(id):
    table_todo.delete_item(Key = {'id': id})
    return get_all_task()