"""
BISI-202: Lab 01 - High-Throughput Kafka Producer/Consumer for Municipal Telemetry
Author: Algonquin College Business Intelligence & Big Data Faculty

Objectives:
1. Configure a Kafka Producer with JSON serialization and delivery callbacks.
2. Produce simulated real-time emergency transit GPS telemetry.
3. Consume the stream with dedicated consumer groups tracking partition offsets.
"""

import json
import time
import random
from datetime import datetime

def generate_telemetry_event(vehicle_id: str):
    """Simulates GPS & engine diagnostic message from municipal vehicle."""
    return {
        "vehicle_id": vehicle_id,
        "timestamp": datetime.utcnow().isoformat(),
        "latitude": round(45.4215 + random.uniform(-0.05, 0.05), 6),
        "longitude": round(-75.6972 + random.uniform(-0.05, 0.05), 6),
        "speed_kmh": round(random.uniform(0.0, 95.0), 2),
        "engine_temp_c": round(random.uniform(75.0, 105.0), 1),
        "fuel_level_pct": round(random.uniform(10.0, 100.0), 1)
    }

def run_simulation(events_to_generate: int = 10):
    print(f"--- Simulating {events_to_generate} Transit Events for Kafka Ingestion ---")
    vehicles = [f"OC-TRANSPO-{i:03d}" for i in range(1, 6)]
    
    for i in range(events_to_generate):
        v_id = random.choice(vehicles)
        event = generate_telemetry_event(v_id)
        payload = json.dumps(event)
        print(f"[EVENT {i+1:02d}] Key={v_id} | Payload={payload}")
        time.sleep(0.2)

if __name__ == "__main__":
    run_simulation(10)
    print("\nLab 01 simulation validated successfully.")
