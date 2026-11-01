+++
title = "PolyArb: Polymarket Arbitrage Research in Rust"
description = "Rust Polymarket arbitrage research with fee-aware sizing, exposure limits, paper trading, and an activity dashboard."
template = "project-detail.html"
updated = 2026-11-01
[extra]
project_id = "polyarb"
toc = true
+++

## Paired-trade research

PolyArb is a Rust bot that evaluates Polymarket YES–NO pairs after fees and available order-book depth. It checks quote freshness, order budgets, and exposure before execution.

## Paper trading and monitoring

The default mode uses real prices and simulated orders. Paper balances persist across restarts; no wallet is needed. Live trading requires explicit configuration and is not ready for unattended use.

A React dashboard shows balance, exposure, market activity, and execution events. These records help separate detected opportunities from simulated fills. Paper results do not establish live returns.

## Availability

The source code is not publicly shared. Read [The Maths Behind PolyArb](@/blog/polyarb-arbitrage-math.md) for worked examples of fees, depth, and partial fills.
