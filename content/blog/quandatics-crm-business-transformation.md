+++
title = "Why We Built an Internal CRM After Trying Salesforce"
description = "How I map sales, delivery, and finance handovers for an internal CRM at Quandatics."
date = 2026-05-25
updated = 2026-05-25
draft = false
aliases = ["/posts/quandatics-crm-business-transformation/"]

[taxonomies]
categories = ["2026"]
tags = ["business transformation", "product management", "CRM", "automation"]

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
topic = "Business Transformation"
+++

At Quandatics, I’m working on an internal CRM connecting sales, project delivery, and finance. The team had tried Salesforce, but its structure required workarounds around our existing process.

We started by mapping what each team needs at a handover: the approved scope, supporting documents, current status, and the person responsible for the next step.

## From lead to sales order

A qualified lead becomes an account, a contact, and an opportunity. One account can have several opportunities, each with its own sales funnel and approval requirements.

When an opportunity is won, the approved quotation becomes a numbered sales order. The order links the sale to a project with its items, budget, team, phases, and milestones.

<figure class="crm-artifact">
  <a href="../../img/blog/quandatics/deal-to-cash-portfolio.png" aria-label="View the full-size CRM deal-to-cash diagram">
    <img src="../../img/blog/quandatics/deal-to-cash-portfolio.png" width="1666" height="944" loading="lazy" decoding="async" alt="Deal-to-cash flow from qualified lead through account, opportunity, approved sales order, project delivery, and payment received.">
  </a>
  <figcaption><span>01 · Lead to approved sales order</span><a href="../../img/blog/quandatics/deal-to-cash-portfolio.png">View full-size diagram</a></figcaption>
</figure>

## From delivery to payment

Each project phase has deliverables and a progress percentage. Once a phase is complete, the team submits a milestone claim with evidence. Management approves it before finance issues the invoice.

The same records need to show delivery progress, billed amounts, receipts, and outstanding payments. Otherwise, finance and delivery have to reconstruct the status separately.

<figure class="crm-artifact">
  <a href="../../img/blog/quandatics/project-to-cash-portfolio.png" aria-label="View the full-size CRM project-to-cash diagram">
    <img src="../../img/blog/quandatics/project-to-cash-portfolio.png" width="1600" height="920" loading="lazy" decoding="async" alt="Project-to-cash flow from an approved sales order through project phases, milestone approval, invoicing, payment receipt, and margin update.">
  </a>
  <figcaption><span>02 · Delivery milestone to collected payment</span><a href="../../img/blog/quandatics/project-to-cash-portfolio.png">View full-size diagram</a></figcaption>
</figure>

## Customer receipts and supplier costs

On the customer side, a milestone claim becomes a sales invoice, then a receipt matched to the invoice. The accounting entry goes to Autocount with its supporting documents.

On the supplier side, a purchase order links to the sales order. Finance matches the supplier invoice to that purchase order, approves a payment voucher, and posts the cost to the project.

<figure class="crm-artifact">
  <a href="../../img/blog/quandatics/o2c-p2p-portfolio.png" aria-label="View the full-size order-to-cash and procure-to-pay diagram">
    <img src="../../img/blog/quandatics/o2c-p2p-portfolio.png" width="1600" height="960" loading="lazy" decoding="async" alt="Two finance flows linked to one sales order: customer milestone claim through invoice and receipt; supplier purchase order through invoice and approved payment voucher. Both post to Autocount and the same project.">
  </a>
  <figcaption><span>03 · Money in and money out</span><a href="../../img/blog/quandatics/o2c-p2p-portfolio.png">View full-size diagram</a></figcaption>
</figure>

## My role

I work across requirements, design, development, production deployment, and support. I clarify who owns each record, what a status means, and what happens when scope changes or an approval arrives late.

Support reveals the gaps that a workflow diagram misses. A late handover or incomplete claim can expose an assumption we need to resolve before adding another field or screen.

## Why an internal system

Custom software adds work of its own. An established CRM can be a better choice when its process matches the business, or when changing the process is worthwhile. Here, the team had already tried adapting to Salesforce and continued to need workarounds.

The internal CRM is still in progress. Client-specific implementation details and operational results remain confidential.
