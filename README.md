# Training Llama 3.2-Instruct for Historical French Post-OCR Correction using Synthetic Data

This repository contains the code and resources for the paper **"Training Llama 3.2-Instruct for Historical French Post-OCR Correction using Synthetic Data: A Case Study"** presented by Mikhail Biriuchinskii, Motasem Alrahabi, and Glenn Roe from the ObTIC Lab, Sorbonne University.

## Abstract
With the rise of generative AI, this project explores using LLMs to correct OCR errors in 19th-century French texts. The study evaluates the Llama-3.2-Instruct model using real and synthetic datasets, highlighting the challenges of generalization and limitations in improving OCR corrections.

For full details, refer to the [article](LINK NOT READY YET).

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/MichaBiriuchinskii/ObTIC-ocr-correction.git
cd ObTIC-ocr-correction
```
   
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies, and [scrambledtex library](https://github.com/JonnoB/scrambledtext/tree/main):
```bash
pip install -r requirements.txt
python -m pip install git+https://github.com/JonnoB/scrambledtext
```
## Data
Dataset used is deployed on huggingface datasets : [ICDAR2017-filtered-1800-1900-6](https://huggingface.co/datasets/m-biriuchinskii/ICDAR2017-filtered-1800-1900-6)

## Library code description
- lib/split_corpus.py # divide the filtered on years dataset into test, dev, train
- lib/send_to_hugging_face.py # create the first version of the dataset without tokenization in phrases [ICDAR2017-filtered-1800-1900](https://huggingface.co/datasets/m-biriuchinskii/ICDAR2017-filtered-1800-1900)

## Citation
If you use this code or find it helpful, please cite the article:

```arduino
Mikhail Biriuchinskii, Motasem Alrahabi, Glenn Roe. "Training Llama 3.2-Instruct for Historical French Post-OCR Correction using Synthetic Data." Sorbonne University, 2024.
```

## Licence
This project is licensed under the MIT License - see the LICENSE file for details.

