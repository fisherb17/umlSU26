"""Exercise 8 starter — publish a STREAM of your own domain events.

You do NOT need to write Python. Just edit the EVENTS list below to match the
domain you designed in Part 1 (give every event a "type"). Then run this while
your consumers are watching — or even before them; the broker holds the events.
"""
import json
import time
from kafka import KafkaProducer

BROKER = "localhost:9092"
TOPIC = "events"                      # you may rename this

# ----- EDIT: your events (each is a fact that already happened) -------------
EVENTS = [
    {"type": "TicketOpened", "ticket_id": 101, "customer_id": "alice", "category": "billing", "priority": "high", "subject": "Duplicate charge"},
    {"type": "TicketAssigned", "ticket_id": 101, "agent_id": "sam"},
    {"type": "CommentAdded", "ticket_id": 101, "comment_id": 1, "author_id": "sam", "body": "Looking into this now.", "is_internal": False},
    {"type": "TicketOpened", "ticket_id": 102, "customer_id": "bob", "category": "access", "priority": "low", "subject": "Password reset"},
    {"type": "TicketResolved", "ticket_id": 102, "resolution_code": "self_service", "resolved_by": "system"},
    {"type": "TicketResolved", "ticket_id": 101, "resolution_code": "refund_issued", "resolved_by": "sam"},
    {"type": "SendReceipt", "ticket_id": 101, "customer_id": "alice", "amount": 42.50},
]
# ----------------------------------------------------------------------------

producer = KafkaProducer(
    bootstrap_servers=BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)
for event in EVENTS:
    producer.send(TOPIC, event)
    print("published", event)
    time.sleep(1)                     # brief pause so you can watch consumers react
producer.flush()
producer.close()
print("producer done — it never waited for a consumer.")
