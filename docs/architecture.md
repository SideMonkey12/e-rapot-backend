# System Architecture

## 1.overview

This document describes the system architecture of the E-Raport Backend project. The system is designed using Clean Architecture principles to ensure scalability, maintainability, and testability.

The backend is built using FastAPI and follows a layered architecture approach.

## 2. Architecture Pattern

This project uses Clean Architecture / Layered Architecture.

Main principles:

- Separation of concerns
- Dependency rule (outer layers depend on inner layers)
- Easy to test
- Framework independent

Layers:

- 1. Router Layer
- 2. Service Layer
- 3. Repository Layer
- 4. Model Layer

## 3. Folder Structure

## 4. Layer Responsiblities

### 4.1 Layer Route

Responsibilities:

- Handle HTTP requests
- Validate request data
- Call service layer
- Return responses

### 4.2 Layer Service

Responsibilities:

- Handle business logic
- Coordinate multiple repositories
- Apply validation rules
- Manage transactions

### 4.3 Layer Repository

Responsibilities:

- Communicate with database
- Perform CRUD operations
- Handle queries
- Abstract ORM logic

### 4.4 Model Layer

Responsibilities:

- Define database tables
- Represent domain entities
- Define relationships
