# Scenario 1:

`Task:` Fix the issues with template-1.yaml to deploy the sample lambda

`Definition of success:` CloudFormation template is sucessfully deployed and lambda executes sucessfully
```
Aims:
- Deploy the lambda using CloudFormation (manual code upload to S3 is ok)
- Adhere to AWS best practices
- Create relevant SSM paramaters and outputs
- Document issues found/best practices applied
```
```
Answers:
- Added code to S3 bucket and created SSM parameter
- Used least privilages for lambda serverless function
- Added SSM parametes of S3 bucket and SSM key value
-   - No Transform template added
    - Corrected Ref! rLambdaFunctionRole Ref! for ARN attribute
    - Circular dependancy on Alarms
    - Added AutoPublishAlias and runtime
```