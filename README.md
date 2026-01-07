# ResumeMD
ResumeMD is a Python-based tool designed to convert Markdown-formatted CV into my personalized LaTeX resume format. It streamlines the process of maintaining and updating my CV by allowing me to write in Markdown, which is then programmatically transformed into a polished LaTeX document.

## Usage
1. Ensure you have Python and LaTeX installed on your system.
2. Execute the script using:
   ```bash
    python3 ./src/render.py input/CV.md
   ```

## Markdown Structure Example
```md
# Miguel Aréjula Aísa

## Contact Information
- Email: string
- Phone: string
- LinkedIn: string
- GitHub: string
- Web: string

## Education

### Master in Software Engineering | University of Southern Denmark
> Sept 2025 – June 2027
- Coursework: Advanced Software Engineering Methodologies, Advanced Software Architecture and Analysis Techniques, Big Data and Data Science Technology

### Bachelor in Software Engineering | University of Zaragoza
> Sept 2021 – June 2025
- Coursework: Software Engineer, Distributed Systems, Software Architecture, Prerequisite Engineering, Verification and Validation, Agile Methodologies and Quality, and Artificial Intelligence.
- Achieved high honors in Information Systems II and Verification and Validation, demonstrating exceptional proficiency and understanding in these subjects.

### Cambridge English  Advance
> July 2024

## Experience

### Software Engineer | University of Zaragoza
> June 2024 – August 2025
- Researcher in project TED2021-130449B-I00 at the University of Zaragoza, where I led development of a custom web application for the Traumatology Department (Hospital Clínico Lozano Blesa), from requirements gathering with medical staff to architecture design and final delivery.
- Developed a full-stack system using React and PostgreSQL, with RESTful APIs in Express and FastAPI, streamlining operations and expected to support ~50 patients per day, enhancing efficiency and quality of care.
- Integrated and processed structured clinical data (CSV-based surgical records) into a relational model, enabling generation and validation of clinical pathways through Petri nets and formal methods.

### Teaching Assistant (Incoming) | SDU
> Starting February 2026
- Support students in understanding core software architecture concepts by assisting with lab sessions, assignments, and problem-solving, while clearly explaining technical concepts and collaborating with professors.

## Projects

### Are-Dev | are-dev.es | are-dev.es
- Are-dev is a personal technical blog and YouTube channel focused on software development, front-end technologies, and modern frameworks.
- Publish blog posts and videos, sharing tutorials, project walk-throughs, and insights to engage the developer community.
- Tools Used: Astro, Vercel, Markdown.

### I4 Pizza Production System | github.com/I4-Pizza | https://github.com/The-European-Avengers/pizza-i4-architecture-group2
- Industry 4.0 pizza production system integrating warehouse, production line, and web platform via a distributed architecture.
- Designed, validated, and documented the system architecture using ADD, covering requirements, use cases, microservice boundaries, formal verification with UPPAAL, and experimental evaluation.
- Led system-level coordination, ensured architectural consistency, and supervised implementation. 
- Tools Used: Go, Python, Kafka, Docker, UPPAAL.

### AgroNet | github.com/AgroNet | https://github.com/STW-24-25
-  Designed and developed a full-stack collaborative web platform for farmers, integrating real-time market prices, personalized weather alerts, and interactive geospatial data visualization across Spain.
-  Led the front-end team, developed the web application, and deployed it on Vercel.
-  Managed communication with the backend hosted on AWS, ensuring reliable API integration and real-time data synchronization.
- Tools Used: Astro, NodeJs, TypeScript, MongoDB, AWS, Vercel.

### Energy Price Prediction | github.com/BigDataProject | https://github.com/The-European-Avengers/BigDataProject
- Using Danish Meteorological Institute (DMI) weather datasets and national energy consumption/price data to analyze correlations and forecast future electricity prices.
- Expected insights include: renewable energy impact, peak price periods, seasonal patterns, and cost optimization windows.
- Applying big data frameworks and machine learning models to process large-scale datasets and deliver predictive analytics.
- Tools Used: Kafka, HDFS, Kubernetes, Hive, Spark, Python.
```


