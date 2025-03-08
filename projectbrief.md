# Project Brief: AI-Powered PDF Processing System for Healthcare

## Project Goal
Develop an AI-powered system for processing large PDF documents, starting with an initial MVP (Deepseek RAG App) and progressing through subsequent phases to create a comprehensive AWS-based solution for healthcare and potentially other industries.

## Project Phases

1. Initial MVP (Deepseek RAG App):
   a. Deploy a locally hosted LLM chatbot on AWS Zurich servers
   b. Process 80-page PDF reports for a single user
   c. Utilize G6.xlarge EC2 instance for GPU-enabled processing
   d. Implement Ollama with DeepSeek R1/8B model
   e. Create a user interface using Streamlit

2. Extended MVP:
   a. Develop a locally hosted solution for a single user (hospital secretary)
   b. Focus on efficient processing of patient-related PDF documents
   c. Ensure compliance with Swiss data protection laws, including FADP
   d. Implement on a standard personal computer

3. Scaled Solution:
   a. Utilize Zurich-based AWS infrastructure
   b. Implement Ollama for general running of models
   c. Upgrade to Mistral-OCR when available
   d. Ensure scalability and cost-effectiveness

## Key Requirements

1. Initial MVP (Deepseek RAG App):
   a. AWS EC2 instance (G6.xlarge) in Zurich region
   b. Nginx reverse proxy for secure access
   c. Ollama for LLM integration
   d. Streamlit for user interface
   e. Ability to process 80-page PDF documents

2. Extended MVP:
   a. Robust PDF processing pipeline for patient documents
   b. Enhanced LLM capabilities for intelligent document analysis
   c. High performance and accuracy in document processing
   d. User-friendly interface for document processing and result retrieval
   e. Security measures compliant with Swiss data protection laws

3. Scaled Solution:
   a. Scalable AWS infrastructure
   b. Multi-user support and larger document volume handling
   c. Advanced features for diverse document types and industries
   d. Cost-effective and high-performance processing at scale

## Objectives

1. Initial MVP (Deepseek RAG App):
   a. Successfully deploy and test the Deepseek RAG App on AWS
   b. Demonstrate PDF processing and question-answering capabilities
   c. Establish a foundation for further development

2. Extended MVP:
   a. Adapt and enhance the initial MVP for specific hospital secretary use case
   b. Integrate additional security measures for healthcare data
   c. Optimize for use on standard personal computers

3. Scaled Solution:
   a. Transition the MVP to a fully scalable AWS infrastructure
   b. Expand system capabilities to handle multiple users and larger document volumes
   c. Implement advanced features for diverse document types and industries
   d. Optimize for cost-effectiveness and performance at scale

This project aims to revolutionize the way large PDF documents are processed and analyzed, starting in healthcare settings and potentially expanding to other industries. It will leverage the power of AI and cloud infrastructure while maintaining strict compliance with data protection regulations.

For detailed implementation steps of the initial MVP, refer to the initialMVP.md file.
