---
title: Dynamical System
---

# Dynamical System

The formalism for the [process view](/views/process/).

## What it is

A dynamical system is a mathematical framework for describing how a state evolves over time according to a fixed rule. Formally, it consists of a state space, a time set (discrete or continuous), and an evolution rule mapping each state to its successor. The trajectory of a system — the sequence of states it passes through — is the central object of study.

Key concepts: *fixed points* (states that don't change), *attractors* (states or sets that nearby trajectories converge to), *bifurcations* (qualitative changes in behavior as a parameter varies), and *phase portraits* (the global picture of all trajectories).

See [Dynamical system](https://en.wikipedia.org/wiki/Dynamical_system) on Wikipedia.

## How the process view uses it

Under the process view, a mechanism is not a static structure in a trained model but a formation trajectory — the process by which the mechanism emerged during training. The dynamical system formalism is natural because training *is* a dynamical system: the state is the model's parameters, the evolution rule is the optimizer, and the trajectory is the sequence of checkpoints.

Two process-level descriptions refer to the same mechanism when they follow the same trajectory type — the same sequence of qualitative phases (e.g., memorization → generalization → cleanup), the same bifurcation structure, the same attractor. The specific parameter values at each step are irrelevant; what matters is the shape of the trajectory.

Evidence for the process view comes from training checkpoints, formation knockouts (ablating a component at a specific training step to see if the mechanism recovers), and phase transition analysis. The formalism provides the vocabulary: a mechanism that forms via a sharp phase transition is qualitatively different from one that forms gradually, even if the end states look identical.
