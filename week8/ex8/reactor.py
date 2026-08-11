"""Exercise 8 starter — the REACTOR consumer.
This one reacts DIFFERENTLY depending on the event type. You only edit the
handle() function: add one branch per event type you care about (Part 1).
Everything else can stay as-is.
"""
import json
from kafka import KafkaConsumer
BROKER = "localhost:9092"
TOPIC = "events"
open_count = 0
resolved_count = 0
def handle(event):
    global open_count, resolved_count
    # ----- EDIT: one branch per event type you want to react to -------------
    if event["type"] == "TicketOpened":
        open_count += 1
        print(f"[reactor] Ticket {event['ticket_id']} opened by {event['customer_id']} "
              f"(priority: {event['priority']}). Open tickets so far: {open_count}")
    elif event["type"] == "TicketResolved":
        resolved_count += 1
        backlog = open_count - resolved_count
        print(f"[reactor] Ticket {event['ticket_id']} resolved via {event['resolution_code']}. "
              f"Backlog: {backlog}")
    elif event["type"] == "SendReceipt":
        print(f"[reactor] Sending receipt to {event['customer_id']} for ${event['amount']}")
    else:
        print(f"reactor: ignoring {event.get('type')}")
    # ------------------------------------------------------------------------
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BROKER,
    group_id="reactor",               # its own group -> also receives every event
    auto_offset_reset="earliest",
    value_deserializer=lambda b: json.loads(b.decode("utf-8")),
)
print("reactor: reacting to events (Ctrl-C to stop)")
for message in consumer:
    handle(message.value)
