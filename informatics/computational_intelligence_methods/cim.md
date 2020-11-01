# Computational Intelligence Methods

Notes form lectures MIE-MVI/FIT/CTU

`2020/10/29, Jaroslav Langer`

## Contents <!-- omit in toc -->

- [Abstract](#abstract)
- [Introduction](#introduction)
  - [Introduction](#introduction-1)
  - [Motivation and recent results](#motivation-and-recent-results)
- [Machine Learning](#machine-learning)
  - [History](#history)
  - [Machine learning tasks](#machine-learning-tasks)
  - [Checkers example](#checkers-example)
  - [Machine learning methods](#machine-learning-methods)
  - [Ants AI challenge](#ants-ai-challenge)
- [Evolutionary Algos](#evolutionary-algos)
- [Neural Networks](#neural-networks)
  - [Overview](#overview)
  - [Perceptron](#perceptron)
  - [Backpropagation algorithm](#backpropagation-algorithm)
  - [Backpropagation algorithm variants](#backpropagation-algorithm-variants)
  - [MLP as universal approximator](#mlp-as-universal-approximator)
  - [Self-organizing Map](#self-organizing-map)
- [Convolutional Networks](#convolutional-networks)
- [Text and Graph Embeddings](#text-and-graph-embeddings)
- [Autoencoders](#autoencoders)
- [Neuroevolution](#neuroevolution)
- [Recurent Neural Nets](#recurent-neural-nets)
  - [Recurent Neural Nets](#recurent-neural-nets-1)
  - [Attetion](#attetion)
  - [Differentiable neural computers](#differentiable-neural-computers)
- [Metalearning](#metalearning)
- [CMAES and Swarm Optimisation](#cmaes-and-swarm-optimisation)

## Abstract

Definitions, terms and knowledge from course NI-MVI.1 
[Course page](https://courses.fit.cvut.cz/MIE-MVI/)

## Introduction

### Introduction

#### What is intelligence

#### Evolutionary

#### Genotype fenotype

- fitness function

### Motivation and recent results

#### Significant fields

-  self-driving cars
- intelligent assistents
- general artifical inteligence (play game from visual input)

#### Research at Datalab

#### prg.ai

#### ethics

## Machine Learning

### History

- 1940
- 1950
- 1960
- 1970
- 1980
- 1990
- 2000
- 2010
  - GAN
  - Transformers (pros of conv + recu)
- 2020+
  - AutoML in RL

### Machine learning tasks

- regression / prediction
- classification / recomendation
- clustering / 
- problem solving / planing / control 

#### Types learning

- supervised
- unsupervised
- semisupervised
- Active learning
- transfer learning
- few-shot learning
- meta-learning / continual learning

#### Examples by types

#### Measuring the performace

#### Learning systems

#### Defining learning task

- T - task ()
- P - performance
- E - expirience

#### Design learning system

- database, prepare data
- choose what to be learnt - target function
- choose representation of target function
- choose learning algoritm
- supply algorithm with performance metric

### Checkers example

Building the database

- Direct expirience
  - set of board with correct move
- indirect expirience
  - sequences of game moves and final results

Choose target funciton

- choseMove(board, legalMoves) -> bestMove
- V(board) -> R (how favorible position) - can be applied for all legalMoves

Choose target funciton representation

### Machine learning methods

### Ants AI challenge

## Evolutionary Algos

## Neural Networks

### Overview

- Introduction to artificial neural networks
- Perceptron, gradient learning
- MLP, Back-propagation of error
- Unsupervized training - SOM

### Perceptron

#### Perceptron training

#### Perceptron gradient learning

#### Deriving gradietn of error

#### Cross entropy loss

### Backpropagation algorithm

#### Multilayer perceptron – MLP

#### Chain rule and backprop

#### Training MLP

#### Propagating the error through multiple layers

#### Backprop summary

### Backpropagation algorithm variants

#### Backprop variants

#### Modified transfer functions

#### Backprop with momentum

#### Batch updates and variable learning rate

#### Second order methods

### MLP as universal approximator

### Self-organizing Map

## Convolutional Networks

## Text and Graph Embeddings

## Autoencoders

## Neuroevolution

## Recurent Neural Nets

### Recurent Neural Nets

#### Elman nets

#### Hopfields networks

#### Restricted Boltzmann Machine

#### Supervised training

- Backpropagation trhough time
- Reservoirs

#### Bidirectional RNN

#### LSTM - Long short-term memory

#### Real-time recurent learning RTRL

#### Clockwork RNN

#### RNN with stack

#### Neural Turing Machine

### Attetion

### Differentiable neural computers

## Metalearning

## CMAES and Swarm Optimisation
