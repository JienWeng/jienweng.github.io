+++
title = "A Web3 Payment Needs More Than a Transaction Hash"
description = "The product decisions behind payment states, confirmation, and settlement in a Web3 gateway."
date = 2026-05-18
updated = 2026-05-18
draft = false
aliases = ["/posts/web3-payment-status-product/"]

[taxonomies]
categories = ["2026"]
tags = ["web3", "product management", "payments"]

[extra]
lang = "en"
toc = true
comment = true
copy = false
outdate_alert = false
outdate_alert_days = 120
math = false
mermaid = false
featured = false
reaction = true
topic = "Web3"
+++

A transaction hash identifies a submitted transaction. The backend still needs to confirm what happened before crediting a ledger or releasing an order.

While working on a multi-chain gateway, I kept returning to when each person can act on a payment state.

## What each state needs to tell us

- The customer needs to know whether to wait or retry.
- The merchant needs to know whether to release the order.
- The backend needs verified evidence before updating the ledger.
- QA needs acceptance criteria for each transition.

Submission, confirmation, failure, and settlement need distinct meanings in the interface, webhook handler, and support process.

## Detection and settlement

Client-side detection provides quick feedback when funds appear. Settlement requires a verified server-side signal, with checks for the network, token, recipient, amount, transaction status, and duplicate processing.

## Acceptance criteria I would write

- Give each payment request a unique reference and expiry.
- Check the selected token and network before signing.
- Record the transaction hash without marking it settled.
- Define separate responses for delays, failures, and duplicates.
- Verify a webhook before it updates the ledger.
- Prevent retries from crediting the same payment twice.

The [CryptoRails lifecycle note](@/notes/cryptorails-transaction-lifecycle.md) covers the documented deposit and consolidation flow. These are generalised requirements; internal details and performance results remain confidential.


## Related reading

- [Deposit detection, consolidation, and settlement in CryptoRails](@/notes/cryptorails-transaction-lifecycle.md).
- [How I define when a payment is complete](@/blog/product-manager-between-business-and-delivery.md).
