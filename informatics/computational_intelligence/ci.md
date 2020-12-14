# Computational Intelligence

Notes form lectures NI-MVI/FIT/CTU.

`2020, Dec. 13th, Jaroslav Langer`

## Contents <!-- omit in toc -->

- [00 Abstract](#00-abstract)
- [01 Introduction](#01-introduction)
  - [Introduction](#introduction)
  - [Motivation and recent results](#motivation-and-recent-results)
- [02 Machine Learning](#02-machine-learning)
  - [History](#history)
  - [Machine learning tasks](#machine-learning-tasks)
  - [Checkers example](#checkers-example)
  - [Machine learning methods](#machine-learning-methods)
  - [Ants AI challenge](#ants-ai-challenge)
- [03 Evolutionary Algos](#03-evolutionary-algos)
- [04 Neural Networks](#04-neural-networks)
  - [Overview](#overview)
  - [Perceptron](#perceptron)
  - [Backpropagation algorithm](#backpropagation-algorithm)
  - [Backpropagation algorithm variants](#backpropagation-algorithm-variants)
  - [MLP as universal approximator](#mlp-as-universal-approximator)
  - [Self-organizing Map](#self-organizing-map)
- [05 Convolutional Networks](#05-convolutional-networks)
- [06 Autoencoders](#06-autoencoders)
- [07 Text and Graph Embeddings](#07-text-and-graph-embeddings)
- [08 Recurrent Neural Networks](#08-recurrent-neural-networks)
  - [Recurrent Neural Nets](#recurrent-neural-nets)
  - [Attention](#attention)
  - [Differentiable neural computers](#differentiable-neural-computers)
- [09 Transformers](#09-transformers)
- [10 Generative models](#10-generative-models)
- [11 Neuroevolution](#11-neuroevolution)
- [Metalearning](#metalearning)
- [CMAES and Swarm Optimisation](#cmaes-and-swarm-optimisation)

## 00 Abstract

Definitions, terms and knowledge from course NI-MVI.
- [Course page](https://courses.fit.cvut.cz/MIE-MVI/).
- [Computational intelligence vs artificial intelligence](https://ai.stackexchange.com/questions/7446/what-is-the-difference-between-artificial-intelligence-and-computational-intelli#:~:text=In%20the%20modern%20context%2C%20computational,focused%20on%20purely%20deductive%20reasoning.)

## 01 Introduction

### Introduction

#### What is intelligence

#### Evolutionary

#### Genotype phenotype

- fitness function

### Motivation and recent results

#### Significant fields

- self-driving cars
- intelligent assistants
- general artificial intelligence (play game from visual input)

#### Research at Datalab

#### prg.ai

#### ethics

## 02 Machine Learning

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
- semi-supervised
- Active learning
- transfer learning
- few-shot learning
- meta-learning / continual learning

#### Examples by types

#### Measuring the performance

#### Learning systems

#### Defining learning task

- T - task ()
- P - performance
- E - experience

#### Design learning system

- database, prepare data
- choose what to be learnt - target function
- choose representation of target function
- choose learning algorithm
- supply algorithm with performance metric

### Checkers example

Building the database

- Direct experience
  - set of board with correct move
- indirect experience
  - sequences of game moves and final results

Choose target function

- choseMove(board, legalMoves) -> bestMove
- V(board) -> R (how favorable position) - can be applied for all legalMoves

Choose target function representation

### Machine learning methods

### Ants AI challenge

## 03 Evolutionary Algos

## 04 Neural Networks

### Overview

- Introduction to artificial neural networks
- Perceptron, gradient learning
- MLP, Back-propagation of error
- Unsupervised training - SOM

### Perceptron

#### Perceptron training

#### Perceptron gradient learning

#### Deriving gradient of error

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

## 05 Convolutional Networks

## 06 Autoencoders

## 07 Text and Graph Embeddings

## 08 Recurrent Neural Networks

### Recurrent Neural Nets

#### Elman nets

#### Hopfields networks

#### Restricted Boltzmann Machine

#### Supervised training

- Backpropagation through time
- Reservoirs

#### Bidirectional RNN

#### LSTM - Long short-term memory

#### Real-time recurrent learning RTRL

#### Clockwork RNN

#### RNN with stack

#### Neural Turing Machine

### Attention

### Differentiable neural computers

## 09 Transformers

## 10 Generative models

## 11 Neuroevolution

## Metalearning

## CMAES and Swarm Optimisation

