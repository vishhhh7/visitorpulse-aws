#  VisitorPulse - AWS Website Visitor Counter

A serverless website visitor counter built using AWS services.

##  Architecture

User → API Gateway → Lambda → DynamoDB

Every API request automatically:
- Increments the visitor count
- Stores it in DynamoDB
- Returns the updated total

##  AWS Services Used

- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB

##  Features

- Real-time visitor counting
- Fully serverless architecture
- Fast NoSQL storage
- REST API endpoint

##  Future Improvements

- Daily visitor tracking
- Unique visitor counting
- Visitor analytics dashboard

## Architecture Diagram

```
User
  ↓
API Gateway
  ↓
Lambda
  ↓
DynamoDB
```
