# mini-manager
Mini Manager is just another warehouse management software.
To be specific it's, Flask based minimal but multiple warehouses manager.

Why?
Because a warehouse management system can be as simple as handling inbound and outbound from a single warehouse and can be complex when you put in group of companies with multiple warehouses, complex internal housekeeping features and much more into the mix.

Initially, the idea is more towards learning and practising tech skills and keeping features just bare minimal.

### Mission

This is side project being used to practice and learn following things primarily:
- Microservice Architecture
- Backend development in Python Environment
- Non-relational Database
Eventually:
- Event Sourcing and CQRS architecture
- AWS

### Planning

Currently the whole software is divided into multiple services handling different concerns:-

- inventory-service: inventory manager of the whole organisation.
- inbound-service: items coming inside warehouse.
- outbound-service: items going outside warehouse.
- housekeeping-service: maintenance of warehouses, probably more useful when having multiple warehoused.
- admin-service: Admin related roles.
