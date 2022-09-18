---
title: Let's deploy ML models in production
date: 2022-09-16
math: true
diagram: true
highlight: true

reading_time: true

image:
  preview_only: true

reading_time: true
pager: true

type: page

summary: 

---

> TLDR;

## Introduction

Training system (Training test) -> Prediction system (Functionality & Validation tests) -> Serving system (Monitoring)

## Model Test Score

Traditional software

- Code -> Running system

  - Unit test -> Integration test -> System monitoring

- Code -> Model training -> Running system
  - Unit test -> Integration test -> System monitoring
  - Monitoring - Prediction monitoring & data monitoring (Serving system)

## Continuous Integration and Continuous Deployment

Inference: Making predictions
Model serving: ML-specific deployment

- REST API
  - as HTTP requests
- Options
  - Deploy code as containers, scale via orchestration
  - Deploy code as a "serverless" function

## Model Serving

## Monitoring

## Harware specific remarks

## Conclusion

## References
