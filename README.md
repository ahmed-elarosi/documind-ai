
# DocuMind AI


[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)




DocuMind AI is an AI-powered document management and intelligence platform designed to ingest, process, and analyze documents at scale. The platform enables users to extract structural and semantic intelligence from unstructured data through efficient backend pipelines and simple API integrations.


## Architecture Overview

DocuMind AI follows a decoupled, three-tier service architecture:

* **Frontend Client:** React-based single-page application for uploading, viewing, and querying documents.
* **Core Application Server:** Asynchronous FastAPI backend providing REST API endpoints, request validation, and orchestrating workflow pipelines.
* **Relational Storage:** PostgreSQL database storing document records, processing statuses, and relational metadata.

```bash 
𝗥𝗲𝗮𝗰𝘁 𝗙𝗿𝗼𝗻𝘁𝗲𝗻𝗱
      │
      │ HTTP GET /documents
      ▼
𝗙𝗮𝘀𝘁𝗔𝗣𝗜 𝗕𝗮𝗰𝗸𝗲𝗻𝗱
      │
      │ SQL Query
      ▼
𝗣𝗼𝘀𝘁𝗴𝗿𝗲𝗦𝗤𝗟 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲
      │
      │ Document Records
      ▼
𝗙𝗮𝘀𝘁𝗔𝗣𝗜 𝗕𝗮𝗰𝗸𝗲𝗻𝗱
      │
      │ JSON Response (200 OK)
      ▼
𝗥𝗲𝗮𝗰𝘁 𝗙𝗿𝗼𝗻𝘁𝗲𝗻𝗱

```