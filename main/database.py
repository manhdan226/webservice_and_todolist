import boto3 

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:4566")

def show_all_table(name):
    
    scanResponse = table.scan(TableName=name)
    items = scanResponse['Items']
    print('Scan all items in datatable: ')
    for item in items:
        print(item)

def create_table(name, key):
    table = dynamodb.create_table(
    TableName=name,
    KeySchema=[
        {
            'AttributeName': key,
            'KeyType': 'HASH'
        }
         
    ],
    AttributeDefinitions=[
             {
            'AttributeName': 'id',
            'AttributeType': 'S'
        } 
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName=name)
    #print("Done!")
    

def delete_table(table):
    table.delete()

def insert_table(table, data):
    for item in data:#, "task": "Bài tập học phần SOA", "description": "Hoàn thành phần frontend-backend và webservice", "deadline": "30/05/2021", "status": "50%"}
        table.put_item(Item=item)

if __name__ == "__main__":
    database = "todo_list"
    key = "id"
    create_table(database, key)

    table = dynamodb.Table(database)
    #delete_table(table)
    data = [
    {
        "id": "1",
        "assignee": "Thi",
        "deadline": "30/05/2021",
        "description": "Code Webservice",
        "progress": "working",
        "task": "SOA"
    },
    {
        "id": "2",
        "assignee": "Thi",
        "deadline": "29/05/2021",
        "description": "Code Database",
        "progress": "done",
        "task": "SOA"
    },
    {
        "id": "3",
        "assignee": "Thông",
        "deadline": "01/06/2021",
        "description": "Report",
        "progress": "todo",
        "task": "SOA"
    },
    {
        "id": "4",
        "assignee": "Thi",
        "deadline": "01/06/2021",
        "description": "Code Web Application",
        "progress": "working",
        "task": "SOA"
    }
    ]
    insert_table(table, data)
    print("Done todo database!")

    database = "todo_list_COUNT"
    key = "id"

    create_table(database, key)

    table = dynamodb.Table(database)
    data = [{"id": "1"}, {"id": "2"}, {"id": "3"}, {"id": "4"}]
    insert_table(table, data)
    print("Done todo database_COUNT!")

        