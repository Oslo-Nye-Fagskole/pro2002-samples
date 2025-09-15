# Simple event bus: manages subscriptions and publishing of events
class EventBus:
    def __init__(self):
        self.subscribers = {}  # Maps event types to lists of handlers

    def subscribe(self, event_type, handler):
        # Register a function to handle a specific event
        self.subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event_type, data):
        # Call all handlers that subscribed to this event
        for handler in self.subscribers.get(event_type, []):
            handler(data)


# Event handlers: independent functions reacting to events
def notify_customer(item):
    print("Notification: New item available ->", item)


def update_inventory(item):
    print("Inventory updated with:", item)


# Setup event-driven system
bus = EventBus()
bus.subscribe("item_added", notify_customer)
bus.subscribe("item_added", update_inventory)

# Publishing an event: multiple handlers can react to it
bus.publish("item_added", "Squig Apple")