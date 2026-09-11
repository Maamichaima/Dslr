# Dslr
dslr/
│
├── datasets/
│   ├── dataset_train.csv
│   └── dataset_test.csv
│
├── models/
│   └── weights.json
│
├── src/
│   ├── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── preprocessing.py
│   │
│   ├── statistics/
│   │   ├── __init__.py
│   │   └── statistics.py
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── histogram.py
│   │   ├── scatter_plot.py
│   │   └── pair_plot.py
│   │
│   └── models/
│       ├── __init__.py
│       ├── logistic_regression.py
│       └── one_vs_all.py
│
├── scripts/
│   ├── describe.py
│   ├── histogram.py
│   ├── scatter_plot.py
│   ├── pair_plot.py
│   ├── logreg_train.py
│   └── logreg_predict.py
│
├── predictions/
│   └── houses.csv
│
├── tests/
│   ├── test_statistics.py
│   ├── test_preprocessing.py
│   └── test_logreg.py
│
├── README.md
├── requirements.txt
└── Makefile