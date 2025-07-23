import json

def lambda_handler(event, context):
    print("EVENT:", event)

    try:
        method = event.get('httpMethod', '').lower()
        if method != 'post':
            return {
                'statusCode': 400,
                'body': json.dumps('Unexpected method')
            }

        payload = json.loads(event['body'])

        first = payload.get('first')
        second = payload.get('second')
        operation = payload.get('operation')

        if operation not in ['addition', 'subtraction', 'multiplication', 'division']:
            return {
                'statusCode': 400,
                'body': json.dumps('Unknown operation')
            }

        if operation == 'addition':
            result = first + second
        elif operation == 'subtraction':
            result = first - second
        elif operation == 'multiplication':
            result = first * second
        elif operation == 'division':
            result = first / second

        return {
            'statusCode': 200,
            'body': json.dumps(f'{operation} result is {result}')
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }
