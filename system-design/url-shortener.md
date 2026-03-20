# System Design: URL Shortener

**Level:** Beginner -> Intermediate
**Focus:** Scalability, Database Design, Caching

## Goal
Design a URL shortening service like TinyURL

---

## Requirements

### Functional Requirements
- generate a Shorter URL from a Long URL
- Redirect user to the original URL using the new shorter link
- Ensure Uniqueness of URLs

### Non-Functional Requirements
- Scalability to millions of URLs
- High Availability - services should always work
- Low latency redirection
- Reliable Storage - no data loss

---

## Capacity Estimation (High-Level)

- Daily new URLs: 100 Thousand
- Read per second:~1000
- Write per second: ~10
- Read heavy system : ~100:1 ratio
- Data storage
  - Assume 500 bytes per URL entry
  - ~ 50MB/ day -> ~19 GB/year



---

## High-Level Design

Describe the architecture:
Client -> API Gateway -> Application Server -> Database (URL Mapping) -> Cache (Redis)


---

## Core Components

### 1. API Layer
- **POST /shorten**
  - Input: Long URL
  - Output: Short URL

- **GET /{short_url}**
  - Redirect to original URL

### 2. Application Layer
- Generate Unique Short IDs
- Handle redirection logic
- Interacts with cache and database

### 3. Database
- Use NoSQL - we need only key-value store
- **Reason"**
  - Fast Lookups
  - Simple schema

---

## Data Model (Example)

```json
{
  "short_url": "abc123",
  "original_url": "https://example.com",
  "created_at": "timestamp",
  "expiry": NULL
}

```

## #######################
## Detailed Design
- How URL is generated ? Options :
  - Hashing (MD5/SHA) - Pros : Simple to implement
                      - Corns : May cause collision
  - Base62 encoding   - Pros : 
                      - Corns :
- Handling collisions
  - Check DB before inserting
  - Retry with new key
  - Use unique ID generator - counter + encoding
- Caching strategy
  - Use Redis to store frequently accessed URLs
  - Cache : short_url -> original_url

## Redirection Flow
- 1) User hits short URL
- 2) Check cache
- 3) If miss -> query DB
- 4) Return original DB
- 5) Store in cache

## Scaling the System
- Horizontal scaling
  - Multiple application server behind load balancer
- Database scaling
  - Sharding by short_url key
  - Replication for high availability
- Caching (Redis)
  - Distributed Cache 
- CDN
  - Cache redirection response globally
- Queue systems (Kafka, RabbitMQ)

## Bottlenecks & Trade-offs
| Issue                   | Solution                 |
| ----------------------- | ------------------------ |
| DB overload             | Add caching              |
| Hot URLs                | Cache aggressively       |
| Collision risk          | Use better ID generation |
| Single point of failure | Replication              |


## Security Considerations
- Rate limiting (prevent abuse)
- Validate URLs (avoid malicious links)
- Optional: authentication for custom URLs

## Key Design Decisions
- NoSQL over SQL -> faster lookups, simple structure
- Base62 encoding -> short, readable URLs
- Cache-first reads -> improves latency

## Improvements / Future Work
- Custom aliases (user-defined URLs)
- Expiration for links
- Analytics (click tracking)
- Admin dashboard
- QR code generation

## Summary
- This is a read-heavy, latency-sensitive system where:
- Fast lookups are critical
- Caching plays a huge role
- Scalability is achieved via horizontal scaling and sharding