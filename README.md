# eb
This repo contains a flask application and deploy it with PaaS (AWS Elastic Beanstalk) and implemented continuous delivery (AWS CodePipeline)

**To find which shell you are using**
```
echo $$
> 5752
cat /proc/5752/comm
> bash
```
OR
```
echo $SHELL
```
To install:
- [AWS Elastic Beanstalk by CLI](https://github.com/aws/aws-elastic-beanstalk-cli-setup)
- [AWS Console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)

An AWS Elastic Beanstalk environment ```eb create <env-name>``` will automatically create these AWS resources: 
- An Amazon Elastic Compute Cloud (Amazon EC2) instance (virtual machine)
- An Amazon EC2 security group
- An Amazon Simple Storage Service (Amazon S3) bucket
- Amazon CloudWatch alarms
- An AWS CloudFormation stack
- A domain name

##### When you create an eb environment you need to have the [instance profiles](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-instanceprofile.html). 
###### [Resolved Issue](https://github.com/aws/aws-elastic-beanstalk-cli/issues/26)
