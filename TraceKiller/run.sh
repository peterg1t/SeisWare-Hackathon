#!/usr/bin/env bash

papermill notebooks/Example01.ipynb notebooks/output/Example01_out_${EXECUTION_ID}.ipynb -f notebooks/parameters/params.yml --log-output
