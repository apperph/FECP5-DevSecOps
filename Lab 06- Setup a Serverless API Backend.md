## Overview:

This activity will demonstrate how to create a Serverless API Backend using AWS Lambda and API Gateway, and near the end of the lab, there will be a little challenge.


## 1. Create a Lambda Function

1-a. Navigate to the Lambda console and set the following

- Function name: SimpleCalculator-< your name >
- Runtime: Python 3.8
- Execution Role: Create a new role with basic Lambda permissions

![](https://sb-next-prod-image-bucket.s3.ap-southeast-1.amazonaws.com/public/CDMP/Session+1/Lab+4/image1.png)

1-b. Once the Lambda function is created, add an API gateway trigger.

![](https://sb-next-prod-image-bucket.s3.ap-southeast-1.amazonaws.com/public/CDMP/Session+1/Lab+4/image2.png)

1-c. Select API Gateway as the trigger, for the API type select REST API and API Key for Security.

![](https://sb-next-prod-image-bucket.s3.ap-southeast-1.amazonaws.com/public/CDMP/Session+1/Lab+4/image3.png)

1-d. Take note of the API endpoint and API Key.

![](https://sb-next-prod-image-bucket.s3.ap-southeast-1.amazonaws.com/public/CDMP/Session+1/Lab+4/image4.png)

1-e. Test the API endpoint using Postman (https://www.postman.com/):

<img width="948" height="525" alt="Screenshot 2025-07-23 at 3 13 58 PM" src="https://github.com/user-attachments/assets/b704ce93-8ce8-4d62-a48c-70be3fd2e832" />

## 2. Create a calculator app.

2-a. Copy the code below and paste it on your Lambda function.

[https://github.com/mikerayco/lambda-simple-calculator/blob/master/lambda_function.py ](https://github.com/apperph/FECP5-DevSecOps/blob/main/lambda_function.py) 

![](https://sb-next-prod-image-bucket.s3.ap-southeast-1.amazonaws.com/public/CDMP/Session+1/Lab+4/image7.png)

This application accepts a JSON payload similar to this: {"first": 1, "second": 2, "operation": "addition"}

2-b Test the API

Using Postman (https://www.postman.com/):



![](https://sb-next-prod-image-bucket.s3.ap-southeast-1.amazonaws.com/public/CDMP/Session+1/Lab+4/image8.png)

Using Postman:

![](https://sb-next-prod-image-bucket.s3.ap-southeast-1.amazonaws.com/public/CDMP/Session+1/Lab+4/image9.png)

## 3. Challenge

3-a. The function for the addition operation is already given in the code, complete the application by creating a function for subtraction, multiplication, and division to complete our API.

Make sure to test your application, after the testing commit your code to CodeCommit, you can copy the code to your Cloud9 environment and push it to a repository named: lambda-simple-calculator-< your name >



----------

Well done!

Please copy and paste the JSON in the textbox below and supply the necessary information.


```
{
 "codecommit-repository-name":"",
 "api-endpoint":""
}
```

Reminder: Please don’t forget to delete your API Gateway and Lambda function!
