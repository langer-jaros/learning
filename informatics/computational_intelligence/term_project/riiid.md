# Riiid! Answer Correctness Prediction

## Contents

## Competition

### Rules

- [riiid rules](https://www.kaggle.com/c/riiid-test-answer-prediction/rules)

### Evaluation

- AOC

### Code requirements

- CPU Notebook <= 9 hours run-time
- GPU Notebook <= 9 hours run-time
- TPU Notebook <= 3 hours run-time
- Freely & publicly available external data is allowed, including pre-trained models
- Submission file must be named submission.csv

### Winning Model Documentation Guidelines

- [Winning Model Documentation Guidelines](https://www.kaggle.com/WinningModelDocumentationGuidelines)

### Competition API Detailed Introduction

- [API introduction notebook](https://www.kaggle.com/sohier/competition-api-detailed-introduction)

## Literature

- [ad-click-prediction (FTRL)](https://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf)
- [Time Series Forecasting with Deep Learning and Attention Mechanism](https://towardsdatascience.com/time-series-forecasting-with-deep-learning-and-attention-mechanism-2d001fc871fc)
- [How Deep is Knowledge Tracing? (2016)](https://arxiv.org/pdf/1604.02416.pdf)
- [Attention Is All You Need (2017)](https://arxiv.org/pdf/1706.03762.pdf)
- [A Self-Attentive model for Knowledge Tracing (2019)](https://arxiv.org/abs/1907.06837)

## Terminology

| Abrv. | Name                                         | Description                |
| :---: | ---                                          | ---                        |
| KC    | Knowledge Concept                            |                            |
|       | Knowledge state                              |                            |
| KT    | Knowledge Tracing                            |                            |
|       |                                              | $X = (x_1, x_2, ..., x_t)$ |
|       |                                              | $x_t = (e_t, r_t)$         |
|       |                                              | $p(r_{t+1}=1|e_{t+1}, X)$  |
| DKT   | Deep Knowledge Tracing                       |                            |
| DKVMN | Dynamic Key-value Memory Network             |                            |
| SAKT  | A self-Attentive model for Knowledge Tracing |                            |

## Shared notebooks

### Decision Tree

- [LightGBM](https://lightgbm.readthedocs.io/en/latest/)
    - [0.753 Expanding on Simple LGBM](https://www.kaggle.com/dwit392/expanding-on-simple-lgbm#Modeling)
    - [0.758 Riiid! LGBM Starter](https://www.kaggle.com/shoheiazuma/riiid-lgbm-starter)
    - [0.766 Riiid! Training and Prediction using a state](https://www.kaggle.com/markwijkhuizen/riiid-training-and-prediction-using-a-state)

### Boosting

- [XGBoost](https://xgboost.readthedocs.io/en/latest/)
    - [0.704 Answer Correctness - RAPIDS crazy fast](https://www.kaggle.com/andradaolteanu/answer-correctness-rapids-crazy-fast)

### Logistic regression

- [0.754 Mike simple predictor](https://www.kaggle.com/mikel1/mike-simple-predictor)
- [FTRL](https://datatable.readthedocs.io/en/v0.10.1/ftrl.html)
    - [0.740 RIIID: FTRL FTW !](https://www.kaggle.com/rohanrao/riiid-ftrl-ftw)

### Feed Forward Neural Network (FFN)

- [Pytorch NN](https://pytorch.org/docs/stable/nn.html)
    - [????? Riiid:Super Cool EDA and Pytorch Baseline](https://www.kaggle.com/maunish/riiid-super-cool-eda-and-pytorch-baseline#Pytorch-Baseline-Model-%F0%9F%94%A5)
    - [0.765 A self-Attentive model for Knowledge Tracing](https://www.kaggle.com/wangsg/a-self-attentive-model-for-knowledge-tracing)
- [Fastai Tabular learner](https://docs.fast.ai/tabular.learner.html)
    - [0.751 Fastai Single NN](https://www.kaggle.com/gilfernandes/fastai-single-nn)
    - [0.767 Fastai Tabular with State](https://www.kaggle.com/gannonreynolds/fastai-tabular-with-state)

- [0.541 SAKT Self-Attentive Knowledge Tracing Submitter](https://www.kaggle.com/leadbest/sakt-self-attentive-knowledge-tracing-submitter/comments)
- [0.771 SAKT with Randomization & State Updates](https://www.kaggle.com/leadbest/sakt-with-randomization-state-updates)

### Recurrent Neural Network (RNN)

- Also called Feedback Neural Network (FNN)

