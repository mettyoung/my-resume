Contact Information
{: .contact-label}

Singapore
✉ mail@mettyoung.com
{: .contact}

# Emmett N. Young
Staff Software Engineer
{: .role}

## Featured Portfolio

[https://mettyoung.com/railway-routing-service/](https://mettyoung.com/railway-routing-service/)

Created a containerized web app for suggesting railway routes to travelers in Singapore.

## Technical Summary

|  |  |
| :-- | :-- |
| **Architecture** | DDD, CQRS, Outbox, Hexagonal Architecture, Microservice |
| **Back-end** | Spring Boot, REST, Thrift, MySQL, Postgres, MongoDB, Redis, Elasticsearch, Clickhouse, Kafka, RocketMQ, JUnit, Spock, Cucumber, JMeter, Taurus |
| **Front-end** | ReactJS, Ant Design, Redux |
| **DevOps** | Liquibase, Maven, Gradle, Docker, Nexus Artifactory, Kubernetes, Ansible, TeamCity, Jenkins, ELK, Prometheus, Open Tracing, Grafana |

## Employment

### Staff Software Engineer (CRM) @ Tiktok Pte. Ltd. | Sep 2021 – Apr 2026

- Awarded **Outstanding Employee** (top performance recognition) for technical leadership and impact across the sales planning & forecasting platform.
- Bootstrapped and led the development of a microservice from scratch, implemented Hexagonal architecture, and onboarded the team to launch **sales planning MVP** for the METAP region within 6 weeks.
    - Started with horizontal slices for smoother onboarding, then repackaged into vertical slices to enhance maintainability.
- Led the **sales forecasting MVP** to the US and METAP regions within 6 weeks, onboarding 3 engineers across regions.
    - Established **CQRS** architecture, building the Elasticsearch ingestion flow as a time-series query model — resolving complex cross-source aggregation, eliminating leader-view latency, and enabling sorting for the sales IC view.
    - Standardized forecasting models by onboarding the SMB market into the KA market.
    - Onboarded 10 engineers over 16 months for the global rollout.
- Built a daily forecast ingestion flow using Clickhouse to power as-is, best-case, and worst-case forecast views in a daily chart.
- Spearheaded the **Agency Breakdown Forecast** MVP and LTS, building a new Elasticsearch ingestion flow piloted in METAP, Japan, Germany, and UK, enhancing APM-BPM collaboration.
- Optimized a high-latency data ingestion process by decoupling the catch-all update trigger into event-driven projections that update only relevant data — cutting user input latency from 10s to <1s during peak times via partial Elasticsearch document updates.
- Took over the **Opportunity microservice** managing the sales pipeline for time-bound campaigns, revamping its data model to daily-value storage to enable seamless snapshot-date switchover and metrics consistent with Plan & Forecast, and launched opportunity automation integrating with the reservation ad calendar, inventory, and quote service.
- Delivered a **zero-downtime revenue snapshot-date switchover** across 3 phases:
    - Phase 1 (5 days, during GCRM offsite in Hangzhou) — snapshot refresh by region, cutting data downtime from 4h20m to 5 minutes per region.
    - Phase 2 (4 days) — dual revenue snapshots to close the snapshot-date gap between the two revenue sources: an account refresh could land between the recent 7/14/30-day revenue dataset and the latest revenue dataset update, so queries in that window served correct data from whichever snapshot was current.
    - Phase 3 — final cutover keeping two Elasticsearch, forecast, and Hive snapshots for zero downtime.
- Drove **org-wide technical influence**: piloted the Java 17 upgrade for Sales Plan & Forecast, and organized a DDD knowledge-sharing session attended by 200+ engineers across three regions.
    - Featured a guest speaker — a tech lead from AxonIQ — and showcased a working CQRS proof-of-concept modeled on the Axon Framework's reference architecture ([AxonIQ/opportunity-poc](https://github.com/AxonIQ/opportunity-poc)), spanning the CRM domain (Customer, Opportunity, Quote, Product, Inventory).
    - Demonstrated tactical DDD patterns including aggregates, CQRS, event sourcing, sagas, and deadlines.
- Resolved a long-standing 2019 issue by upgrading 14/36 projects to Spring Boot 2, cutting application startup time from 2.65 min to 29s (~2 hours saved per build across 100 engineers); won **1st place at MT Quality Week**.
- Crafted a lightweight test fixture using DI to centralize mocks, overcoming integration-test limitations caused by the tight coupling of ByteDance Java SDKs.

## Previous Employment {: #previous-employment}

### Engineer Lead @ Rakuten Asia Pte. Ltd. | Jun 2021 – Sep 2021

- Onboarded and mentored 3 backend engineers to full-stack development.
- Led one software release with zero deployment issues.

### Software Engineer @ Rakuten Asia Pte. Ltd. | Aug 2019 – May 2021

- Received the **Outstanding Newcomer award** for early impact and contributions to the team.
- Designed and presented the architecture for eventual consistency between two databases to the architecture review team (Outbox Pattern, Kafka).
- Designed an ad creative review process with a task-based UI (submission, review, approve, reject, amend), using outside-in TDD (Spring Boot, Cucumber, JUnit5) and ReactJS/Redux for the review screen.
- Wrote the team's test framework single-handedly (inspired by outside-in TDD), improving test suite performance by 600%.
- Implemented 6 API endpoints with outside-in TDD — approved with zero revisions and no reported bugs (Spring Boot, Cucumber, JUnit5).
- Identified and resolved API performance issues through load testing (JMeter, Taurus).

### Software Engineer @ Exist Software Labs | Aug 2017 – Jun 2019

- Worked in the energy market domain using Spring Boot, Apache NiFi, and AngularJS — covering data pipelines (Apache NiFi), a market data subscription system, and core energy-domain services.

### Software Engineer @ Nelsoft Systems, Inc. | Feb 2015 – Apr 2017

- Built an inventory system (PHP, JavaScript) and branch database syncing and smart deployment processes (C# WinForms, WPF).

## Education Background

### Computer Engineering @ De La Salle University Manila | May 2010 – Dec 2014

- Graduated with honorable mention having a CGPA of 3.203.
- Awarded **2nd place** at Shell Eco-Marathon Asia 2014; designed and implemented the vehicle telemetry system, and designed, crafted, and mounted the solar panels to the battery management system.
- Awarded **2nd place** for undergraduate thesis on cooperative autonomous UAV 3D mapping and localization (dual quadrotors).
