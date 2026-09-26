---
name: winter-storm-triage
description: Standard operating procedures for triaging customer orders delayed by severe winter storms, verifying order and customer loyalty details, issuing compensation, and drafting empathetic customer responses.
---

# Winter Storm Triage Standard Operating Procedures

This skill dictates the standard operating procedures (SOP) for assisting customers whose packages are delayed due to severe winter storms.

## Workflow Procedures

### 1. Order and Loyalty Verification
* Use the `get_order_status` tool with the provided `order_id` to verify the order status, identify delay reasons (confirming it is due to severe winter storms), and retrieve the `customer_id`.
* Use the `get_customer_loyalty_info` tool with the `customer_id` to retrieve the customer's loyalty tier (`PLATINUM`, `GOLD`, `SILVER`, or `MEMBER`).

### 2. Disruption Compensation Policy
Determine the appropriate compensation and shipping upgrade based on the customer's loyalty tier:

| Loyalty Tier | Disruption Credit | Shipping Upgrade |
| :--- | :--- | :--- |
| **Platinum** | $100 credit | Next-Day Air |
| **Gold** | $50 credit | Next-Day Air |
| **Silver** | $25 credit | 3-Day Select |
| **Member** | $10 credit | Priority Shipping |

### 3. Issue Disruption Compensation
* Call the `issue_disruption_compensation` tool with the following parameters:
  * `customer_id`: The verified customer ID.
  * `compensation_amount`: The credit amount corresponding to their loyalty tier (e.g., "$100", "$50", "$25", or "$10").
  * `shipping_upgrade`: The shipping upgrade corresponding to their tier (e.g., "Next-Day Air", "3-Day Select", or "Priority Shipping").

### 4. Empathetic Customer Communication
Draft a polite, empathetic, and professional customer response that:
* Acknowledges and apologizes for the delay caused by the severe winter weather.
* Confirms the current status of their order.
* Details the resolution, explicitly stating the credit amount issued to their account and the upgraded shipping method applied to expedite their delivery.
