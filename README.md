# German Traffic‑Sign Classifier

![Training Metrics](training_metrics.png)

A Keras-based multi‑class classifier for the [German Traffic Sign Recognition Benchmark (GTSRB)](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news), achieving:

- **99 %** validation accuracy  
- **97 %** test accuracy  

Demo your own images via a lightweight [Gradio](https://gradio.app) interface.

---

## 📁 Repository Structure


- **model.h5** – pre‑trained Keras model  
- **class_mapping.txt** – `class_id: sign_name` for all 43 classes  
- **training_metrics.png** – accuracy & loss curves  
- **architecture.png** – _(optional)_ plot of the network structure  
- **notebook.ipynb** – EDA & training code  
- **app.py** – Gradio demo  

---

## 🚀 Quick Start

1. **Clone & activate environment**  
   ```bash
   git clone https://github.com/yourusername/german-traffic-signs.git
   cd german-traffic-signs
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
