# Airflow-DataHub-MongoStack

A Docker-based stack for integrating **Apache Airflow**, **DataHub**, and **MongoDB** for metadata management and workflow automation.

## Features

- **MongoDB**: Stores and manages data for DataHub and workflows.
- **Apache Airflow**: Orchestrates data pipelines.
- **DataHub**: Provides metadata management and lineage tracking.
- **Docker Compose**: Simplifies deployment and configuration.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository:

   ```sh
   git clone https://github.com/yourusername/Airflow-DataHub-MongoStack.git
   cd Airflow-DataHub-MongoStack
   ```

2. Start the services:

   ```sh
   docker-compose up -d
   ```

3. Access the services:
   - **Airflow**: [http://localhost:8081](http://localhost:8081) (Username: `admin`, Password: `admin`)
   - **DataHub UI**: [http://localhost:9002](http://localhost:9002)
   - **MongoDB**: `mongodb://admin:password@localhost:27017/`

## Configuration

- Update **MongoDB credentials** in `docker-compose.yml` if necessary.
- Modify Airflow DAGs in `./airflow/dags/` to define workflows.

## Stopping Services

To stop and remove all containers, run:

```sh
docker-compose down
```

## License

This project is open-source and available under the MIT License.

---

Happy coding! 🚀
