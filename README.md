# SentinelTI

SentinelTI is an educational Threat Intelligence platform currently under development.

The goal of the project is to build a small platform capable of collecting, validating, normalizing, storing and querying Indicators of Compromise (IoCs), while applying software engineering and cybersecurity concepts.

The project is inspired by real-world Threat Intelligence platforms, but it is an independent educational project and is not intended to replicate any existing platform.

## Current Status

🚧 **Work in Progress**

SentinelTI is still under active development. The current version focuses on building the core API and database functionality before moving towards more advanced Threat Intelligence features.

### Currently implemented

- REST API built with FastAPI
- PostgreSQL database
- SQLAlchemy ORM
- CRUD operations for indicators
- Indicator validation
- Support for:
  - IP addresses
  - Domains
  - URLs
  - File hashes
- Confidence validation
- Basic indicator normalization and duplicate detection
- Separation between routes, services and storage layers
- Environment-based database configuration

### Planned features

The project will progressively include:

- Indicator normalization and deduplication improvements
- Risk scoring
- Threat Intelligence enrichment
- Search and filtering
- Indicator correlation
- Data ingestion from external sources
- Background workers and queues
- Authentication and API security
- Logging and monitoring
- Docker support
- Dashboard
- Cloud deployment

## Architecture

The project is being developed with a layered architecture:

```text
Client
  ↓
FastAPI Routes
  ↓
Services
  ↓
Storage
  ↓
PostgreSQL