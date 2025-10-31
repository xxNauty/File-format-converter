def process(data: str) -> dict:
    pass



process('''meta:
  generated_at: "2025-10-30T13:00:27Z"
  description: "Sample dataset for testing APIs, UIs, and demos (users, products, orders, events)."
users:
  - id: "usr_001"
    username: "alice"
    full_name: "Alice Johnson"
    email: "alice@example.com"
    created_at: "2023-06-12T09:23:00Z"
    active: true
    profile:
      age: 29
      country: "US"
      roles:
        - "admin"
        - "seller"
  - id: "usr_002"
    username: "bob"
    full_name: "Robert Smith"
    email: "bob@example.com"
    created_at: "2024-01-05T15:10:00Z"
    active: true
    profile:
      age: 34
      country: "GB"
      roles:
        - "buyer"
  - id: "usr_003"
    username: "carol"
    full_name: "Carol Becker"
    email: "carol@acme.co"
    created_at: "2025-03-20T08:00:00Z"
    active: false
    profile:
      age: 41
      country: "DE"
      roles:
        - "buyer"
        - "support"
  - id: "usr_004"
    username: "dave"
    full_name: "David Park"
    email: "dave@startup.io"
    created_at: "2025-07-11T19:45:00Z"
    active: true
    profile:
      age: 26
      country: "CA"
      roles:
        - "seller"
  - id: "usr_005"
    username: "eve"
    full_name: "Eve Martinez"
    email: "eve@privacy.net"
    created_at: "2022-11-01T07:30:00Z"
    active: true
    profile:
      age: 38
      country: "AU"
      roles:
        - "buyer"
        - "beta_tester"
products:
  - id: "prod_001"
    sku: "SKU-001"
    name: "Wireless Mouse"
    category: "electronics"
    price: 29.99
    currency: "USD"
    inventory: 120
    tags:
      - "wireless"
      - "mouse"
      - "peripheral"
  - id: "prod_002"
    sku: "SKU-002"
    name: "Mechanical Keyboard"
    category: "electronics"
    price: 129.5
    currency: "USD"
    inventory: 35
    tags:
      - "keyboard"
      - "mechanical"
      - "desktop"
  - id: "prod_003"
    sku: "SKU-003"
    name: "Coffee Mug"
    category: "kitchen"
    price: 9.95
    currency: "USD"
    inventory: 500
    tags:
      - "kitchen"
      - "mug"
      - "ceramic"
  - id: "prod_004"
    sku: "SKU-004"
    name: "Notebook A5"
    category: "stationery"
    price: 4.75
    currency: "USD"
    inventory: 1000
    tags:
      - "stationery"
      - "notebook"
  - id: "prod_005"
    sku: "SKU-005"
    name: "USB-C Cable 1m"
    category: "accessories"
    price: 7.25
    currency: "USD"
    inventory: 250
    tags:
      - "usb-c"
      - "cable"
      - "charging"
orders:
  - id: "ord_1001"
    user_id: "usr_002"
    created_at: "2025-10-28T12:34:56Z"
    status: "shipped"
    items:
      - product_id: "prod_001"
        name: "Wireless Mouse"
        quantity: 1
        unit_price: 29.99
      - product_id: "prod_003"
        name: "Coffee Mug"
        quantity: 2
        unit_price: 9.95
    subtotal: 49.89
    shipping_cost: 5.0
    tax: 3.15
    total: 58.04
    shipping:
      method: "standard"
      address:
        line1: "22 Baker St"
        city: "London"
        region: ""
        postal_code: "NW1 6XE"
        country: "GB"
      tracking_number: "TRACK123456GB"
      shipped_at: "2025-10-29T08:00:00Z"
    notes: ""
  - id: "ord_1002"
    user_id: "usr_001"
    created_at: "2025-10-29T09:10:00Z"
    status: "processing"
    items:
      - product_id: "prod_002"
        name: "Mechanical Keyboard"
        quantity: 1
        unit_price: 129.5
    subtotal: 129.5
    discounts:
      - code: "WELCOME10"
        amount: 12.95
    shipping_cost: 0.0
    tax: 11.69
    total: 128.24
    shipping:
      method: "express"
      address:
        line1: "470 Market St"
        city: "San Francisco"
        region: "CA"
        postal_code: "94105"
        country: "US"
      tracking_number: null
      shipped_at: null
    notes: "Gift wrap"
  - id: "ord_1003"
    user_id: null
    created_at: "2025-09-30T17:20:00Z"
    status: "delivered"
    items:
      - product_id: "prod_005"
        name: "USB-C Cable 1m"
        quantity: 3
        unit_price: 7.25
    subtotal: 21.75
    shipping_cost: 3.5
    tax: 1.95
    total: 27.2
    shipping:
      method: "standard"
      address:
        line1: "Guest Checkout"
        city: ""
        region: ""
        postal_code: ""
        country: ""
      tracking_number: "TRACK-GUEST-0001"
      shipped_at: "2025-10-01T09:00:00Z"
      delivered_at: "2025-10-03T14:12:00Z"
    notes: "Guest order"
  - id: "ord_1004"
    user_id: "usr_005"
    created_at: "2025-08-15T11:05:00Z"
    status: "cancelled"
    items:
      - product_id: "prod_004"
        name: "Notebook A5"
        quantity: 12
        unit_price: 4.75
    subtotal: 57.0
    shipping_cost: 7.0
    tax: 4.12
    total: 68.12
    cancellation:
      cancelled_at: "2025-08-16T10:00:00Z"
      reason: "Out of stock"
    notes: ""
events:
  - event_id: "evt_9001"
    user_id: "usr_001"
    type: "login"
    properties:
      ip: "198.51.100.12"
      device: "desktop"
      method: "password"
    timestamp: "2025-10-30T12:59:01Z"
    severity: "info"
  - event_id: "evt_9002"
    user_id: "usr_002"
    type: "order_created"
    properties:
      order_id: "ord_1001"
      value: 58.04
    timestamp: "2025-10-28T12:34:58Z"
    severity: "info"
  - event_id: "evt_9003"
    user_id: "usr_004"
    type: "product_review"
    properties:
      product_id: "prod_002"
      rating: 5
      comment: "Excellent build quality!"
    timestamp: "2025-10-10T10:05:00Z"
    severity: "info"
  - event_id: "evt_9004"
    user_id: null
    type: "inventory_low"
    properties:
      product_id: "prod_002"
      inventory: 35
      threshold: 50
    timestamp: "2025-10-01T06:00:00Z"
    severity: "warning"
  - event_id: "evt_9005"
    user_id: null
    type: "system_alert"
    properties:
      message: "Payment gateway latency > 2s"
      avg_latency_ms: 2345
    timestamp: "2025-10-29T03:30:00Z"
    severity: "critical"''')