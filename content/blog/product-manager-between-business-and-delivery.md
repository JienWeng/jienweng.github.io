+++
title = "How I Define When a Payment Is Complete"
description = "The settlement boundary, its trade-off, and the acceptance criteria I work through with engineers."
date = 2026-07-20
updated = 2026-07-20
draft = false
aliases = ["/posts/product-manager-between-business-and-delivery/"]

[taxonomies]
categories = ["2026"]
tags = ["product management", "web3", "delivery"]

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
topic = "Product Management"
+++

I coordinate an engineering team working on Web3 payments. I maintain the backlog and roadmap, run Scrum ceremonies, and clarify priorities with the business owner.

## When the merchant can credit a payment

“Make deposits more reliable” leaves a decision open: which event allows the merchant to credit its ledger?

I work through that boundary with the business owner and engineers. In the documented CryptoRails flow, the browser detects incoming funds and gives the customer feedback. The merchant backend credits the ledger after receiving and verifying the signed settlement webhook.

The trade-off is waiting for confirmation and server verification before calling the payment complete. The interface still needs to show progress during that wait. Treating detection as completion would let the screen promise an outcome the backend has yet to verify.

## What I put into acceptance criteria

That boundary changes what the team has to test:

- Deposit detection updates the interface without marking the payment settled.
- A delayed confirmation leaves the payment pending.
- The backend verifies the webhook before updating the ledger.
- A repeated webhook or retry cannot credit the same payment twice.

A successful demo covers only one of these paths. I include the delayed and duplicate cases when defining done with the team.

## Keeping the scope deliverable

The request also needs agreed networks, failure cases, and responses for the user. I turn those decisions into backlog items, track dependencies, and raise blocked work or competing requests with the business owner.

The [CryptoRails workflow](@/notes/cryptorails-transaction-lifecycle.md) shows the deposit and consolidation sequence behind these requirements. Product-specific business details, internal metrics, and implementation details remain confidential.
