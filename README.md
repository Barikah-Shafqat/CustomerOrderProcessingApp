Problem: 
The goal of this test assignment is to design a data processing pipeline taking input in CSV format from a partner and producing output in JSON format for internal processing.

Solution:
The following project can be achieved by using AWS Serverless setup such as AWS Lambda, Amazon S3 for uploading the csv files and Amazon SQS for forwarding the output messages.
The AWS Services can be setup in the following order:
1.	Setting up S3 Bucket where a partner can upload the csv files.
2.	Secondly a Lambda Function can be setup which gets triggered by S3 events (Object Created) on the specified bucket.
3.	The last step would be to set up an SQS queue to send the output JSON messages.

Reasons for choosing AWS:
1.	AWS provides a wide range of managed services that abstract away the complexity.
2.	AWS handles provisioning, scaling, and maintenance tasks, reducing operational overhead.
3.	AWS offers scalability based on demand ensuring that our data pipeline can handle varying workloads.
4.	AWS offers easy Integration making it easy to build complex workflows.

Scaling in AWS Lambda:
•	When it comes to scaling, AWS lambda imposes certain scaling limits such as maximum number of executions per account. However, these limits are quite high making it a perfect choice for this project.
•	AWS lambda automatically scales in response to incoming requests or events. It automatically provisions the necessary compute resources to execute the function code.

Permanent Storage Solution for Processed Data:
•	The processed data could be saved to a database like Amazon DynamoDB for archival purposes.

Additional Improvements:
•	The system could be setup using AWS CodePipeline for automating the process. 
•	Moreover, AWS CloudFormation could be used to set up a pipeline further automating the pipeline process.
•	The performance of Lambda function could be monitored for further optimization as needed.

