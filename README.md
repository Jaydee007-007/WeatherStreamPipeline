# WeatherStreamPipeline

Real-time weather data streaming pipeline using Apache Kafka and AWS S3

## Architecture

Kafka streaming consumer pulls real-time weather data from distributed broker, deserializes JSON payloads, and persists to S3 with incremental file naming. Consumer runs on 60-second polling interval with automatic offset management.

## Technical Implementation

- **Kafka Consumer:** Connects to broker at 18.234.23.127:9116, subscribes to 'WeatherData' topic
- **Deserialization:** UTF-8 JSON decoding with automatic schema inference
- **S3 Persistence:** Files written as `weather_data_{count}.json` with sequential numbering
- **Storage Pattern:** S3FileSystem integration for direct cloud writes without local buffering

## Dependencies
```
kafka-python==2.0.2
s3fs==2023.6.0
```

## Usage
```python
from kafka_consumer import kafka_consumer

kafka_consumer()
```

## Configuration

- **Kafka Topic:** WeatherData
- **Bootstrap Server:** 18.234.23.127:9116
- **S3 Bucket:** ece5984-s3-davisu/Lab 1/
- **Runtime:** 60-second polling window

## ECE 5984 Assignment Context

Assignment 2 implementation demonstrating streaming data ingestion using weather telemetry.

## Author

Davis Ukoli - Virginia Tech ECE 5984

## Stack

Apache Kafka | Python | AWS S3 | Real-Time Streaming
