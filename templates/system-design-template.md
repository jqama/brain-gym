# System Design: <System Name>

## Goal
What are we building?
> Example: Design a URL shortening service like TinyURL

---

## Requirements

### Functional Requirements
- What should the system do?
- Example:
  - Shorten URLs
  - Redirect to original URL

### Non-Functional Requirements
- Scalability (users, requests/sec)
- Availability vs Consistency
- Latency expectations
- Storage constraints

---

## Capacity Estimation (High-Level)

- Daily active users:
- Requests per second:
- Data storage per day:
- Read/Write ratio:



---

## High-Level Design

Describe the architecture:

- Client → API Gateway → Services → Database

(Optional diagram)

---

## Core Components

### 1. API Layer
- Endpoints
- Request/response format

### 2. Application Layer
- Business logic
- Services involved

### 3. Database
- Type (SQL / NoSQL)
- Schema design

---

## Data Model (Example)

```json
{
  "short_url": "abc123",
  "original_url": "https://example.com",
  "created_at": "timestamp"
}

```

## #######################
## Detailed Design
- How URL is generated (hashing, encoding, etc.)
- Handling collisions
- Caching strategy
- Load balancing

## Scaling the System
- Horizontal scaling
- Database sharding
- Caching (Redis)
- CDN usage
- Queue systems (Kafka, RabbitMQ)

## Bottlenecks & Trade-offs
- Single point of failure?
- DB overload?
- Cache invalidation?

## Security Considerations
- Rate limiting
- Authentication (if needed)
- Data validation

## Key Design Decisions
- Explain why you chose:
- SQL vs NoSQL
- Cache strategy
- Architecture style

## Improvements / Future Work
- Analytics
- Custom aliases
- Expiration links
- Monitoring & logging