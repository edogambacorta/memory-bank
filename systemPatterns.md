# System Patterns: AI-Powered PDF Processing System for Healthcare

## Architecture Overview
Our system starts with a locally hosted MVP for a hospital secretary and evolves into a scalable AWS-based solution for handling large document volumes across multiple industries.

```mermaid
graph TD
    subgraph "MVP (Local Deployment)"
    A[Hospital Secretary] -->|Upload PDF| B[Local Storage]
    B --> C[Local Processing Application]
    C -->|Process PDF| D[Local LLM]
    D --> E[Result Processing]
    E -->|Store Results| F[Local Storage]
    E -->|Display| G[User Interface]
    end

    subgraph "Scaled Solution (AWS)"
    H[Client] -->|Upload PDF| I[S3 Bucket]
    I --> J{Lambda Trigger}
    J -->|Initiate Processing| K[SQS Queue]
    K --> L[EC2 with Ollama]
    L -->|Process PDF| M[DeepSeek R1/8B Model]
    M --> N[Result Processing]
    N -->|Store Results| O[S3 Bucket]
    N -->|Notify| P[SNS Topic]
    P --> Q[Client Notification]
    end
```

## Key Components

### MVP Phase

1. Local Processing Application
   - Purpose: Handle PDF upload, processing, and result display
   - Implementation: Desktop application with user-friendly interface
   - Security: Implement local encryption and access controls

2. Local LLM
   - Purpose: Perform document analysis and information extraction
   - Configuration: Optimized for running on a standard PC
   - Integration: Tightly coupled with the local processing application

3. Local Storage
   - Purpose: Store input PDFs and processed results
   - Security: Implement encryption and secure access mechanisms
   - Organization: Maintain clear structure for easy retrieval and backup

### Scaled Solution Phase

1. EC2 Instances
   - Purpose: Host Ollama and LLM models
   - Configuration: GPU-optimized instances for efficient model inference
   - Scalability: Auto Scaling groups to handle varying loads

2. S3 (Simple Storage Service)
   - Purpose: Store input PDFs and processed results
   - Configuration: Versioning enabled for data integrity
   - Security: Server-side encryption for data at rest

3. Lambda Functions
   - Purpose: Orchestrate workflow and trigger processing tasks
   - Implementation: Python-based functions for flexibility and ease of development
   - Integration: Tight coupling with S3 events and SQS for efficient processing

4. SQS (Simple Queue Service)
   - Purpose: Manage processing jobs and ensure scalability
   - Configuration: FIFO queues for maintaining processing order when necessary
   - Retry Logic: Implement dead-letter queues for handling processing failures

5. CloudWatch
   - Purpose: Monitoring and logging
   - Implementation: Custom metrics for tracking processing times and success rates
   - Alerts: Set up alarms for abnormal system behavior or performance issues

## Data Flow

### MVP Phase

1. PDF Upload
   - Hospital secretary uploads PDF through the local application interface
   - PDF is stored in a designated local directory

2. PDF Processing
   - Local application triggers the processing pipeline
   - PDF text is extracted and sent to the local LLM for analysis

3. Result Storage and Display
   - Processed results are stored locally
   - Results are displayed in the application interface for the secretary to review

### Scaled Solution Phase

1. PDF Upload
   - Client uploads PDF to designated S3 bucket
   - S3 event triggers Lambda function

2. Job Queue
   - Lambda function creates a processing job and sends it to SQS
   - Job includes reference to PDF location and processing parameters

3. PDF Processing
   - EC2 instances running Ollama poll SQS for new jobs
   - When a job is received, the instance downloads the PDF from S3

4. LLM Processing
   - PDF text is extracted and sent to DeepSeek R1/8B model via Ollama
   - Model performs required analysis (e.g., summarization, entity extraction)

5. Result Storage
   - Processed results are stored back in S3
   - Original PDF and results are linked for easy retrieval

6. Client Notification
   - SNS topic is used to notify the client of completed processing
   - Notification includes link to results in S3

## Scalability Considerations
- Design MVP with modularity to facilitate future AWS integration
- Plan for data migration from local storage to S3 during scaling phase
- Utilize EC2 Auto Scaling groups in AWS phase to dynamically adjust processing capacity
- Implement SQS in AWS phase to decouple PDF upload from processing, allowing for smooth handling of traffic spikes

## Security Patterns
- Implement strong local security measures in MVP phase, including data encryption and access controls
- In AWS phase, implement VPC for network isolation of EC2 instances
- Use IAM roles for secure, key-less authentication between AWS services
- Enable encryption in transit (HTTPS) and at rest (S3 encryption) for all data in AWS phase
- Ensure compliance with Swiss data protection laws (including FADP) in both phases

## Monitoring and Logging Patterns
- Implement local logging and performance monitoring in MVP phase
- In AWS phase, centralize logs using CloudWatch Logs
- Set up CloudWatch Dashboards for real-time system overview in AWS phase
- Implement custom metrics for tracking PDF processing times and success rates in both phases

This system architecture and these patterns provide a scalable, secure, and efficient foundation for our AI-Powered PDF Processing System, starting with a focused MVP for healthcare and evolving into a comprehensive AWS-based solution for multiple industries.

[Note: Specific MVP features and implementation details to be added once provided.]
