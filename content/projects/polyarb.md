+++
title = "PolyArb: Polymarket Arbitrage Research in Rust"
description = "A Rust arbitrage bot with paper trading, risk checks, and a React dashboard for inspecting Polymarket activity."
template = "project-detail.html"
updated = 2026-11-01
[extra]
project_id = "polyarb"
toc = true
+++

## The market question

PolyArb explores a simple condition in binary prediction markets: can a YES share and a NO share together cost less than their combined $1 settlement value after fees? The bot looks for these pairs using real Polymarket prices.

A detected price gap is a candidate for evaluation. Available liquidity, execution timing, and whether both legs fill determine whether that gap can be captured.

## From market prices to risk checks

The Rust workspace separates market scanning, monitoring, strategy, risk checks, execution, and recording into dedicated crates. This structure makes it possible to inspect the stages between a price observation and an order decision.

The default dry-run mode uses simulated orders and starts with $1,000 in paper funds. It preserves the paper balance across restarts and requires no wallet. Live execution uses a separate wallet setup and explicit configuration.

## Inspecting activity in the dashboard

The React and TypeScript dashboard uses Supabase activity and snapshot data to make the bot's behaviour inspectable. The documented presentation workflow includes an overview of balance and exposure, a market view, a searchable activity feed, and connection diagnostics.

These views help distinguish opportunities detected by the scanner from decisions that pass strategy and risk checks. Event details provide a way to investigate why the bot acted or stayed idle.

## What the prototype demonstrates

The project connects market monitoring, decision rules, simulated execution, and observability in one research workflow.

Paper balances and expected profit are simulated outputs. They do not establish realised returns or prove that both sides of a trade would fill in live conditions. Live mode is not ready for unattended trading.

## Project availability

PolyArb is a private project. Its source code is not publicly shared.

Read [The Maths Behind PolyArb](@/blog/polyarb-arbitrage-math.md) for hypothetical examples of fees, order-book depth, and partial fills.
