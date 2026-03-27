# Dealership API - Sample Domain Skeleton

This is a **sample domain structure** for a Car Dealership backend system.

It demonstrates a layered architecture consistent with previous course samples:

- `routes` - API layer  
- `services` - business logic  
- `models` - domain representation  
- `data` - schema and persistence scripts  
- `auth` - authentication and role helpers  
- `types` - shared enums/constants  

All files contain minimal placeholder or dummy implementations.

This sample is **not a finished system**.

## How to Run

To run this sample:

```bash
pip install -r requirements.txt
flask run
```

## Purpose of This Sample

This sample illustrates:

- How to structure a Flask backend using layered architecture  
- How to separate responsibilities between routes and services  
- Where business logic should be implemented  
- How role-based authorization can be organized  

It does **not** provide complete business logic, authentication wiring, or production-ready validation. This is where you come in. It is your job to implement it all 🫡
