# 📰 Fake News Detector using NLP & Machine Learning

## 📌 Project Overview
This project builds a **Fake News Detection model** using the **ISOT Fake News Dataset**.  
It uses **Natural Language Processing (NLP)** and a **Logistic Regression classifier** to distinguish between real and fake news articles.  

✅ **Key Steps**  
- Data cleaning & preprocessing  
- Text vectorization using **TF-IDF**  
- Machine Learning model (Logistic Regression)  
- Evaluation & testing with new examples  

---

## 📊 Dataset
We used the **ISOT Fake News Dataset** from [Kaggle](https://www.kaggle.com/datasets/csmalarkodi/isot-fake-news-dataset).  

- `Fake.csv` → Fake news articles  
- `True.csv` → Real news articles  

They were merged into a single dataset with a binary `label` (1 = Fake, 0 = Real).

---

## 🚀 How to Run

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
