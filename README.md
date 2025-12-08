# 📝 **FIFA 24 Player Clustering**

This project applies **Unsupervised Machine Learning** to group FIFA 24 players based on their attributes.
Using **PCA (Principal Component Analysis)** for dimensionality reduction and **K-Means clustering**, we identify natural player groups such as attackers, midfielders, defenders, goalkeepers.

---

## 🚀 **Project Overview**

### ✔️ **Goal**

To group similar FIFA players using AI, and understand hidden patterns in player attributes.

### ✔️ **Why Unsupervised Learning?**

There are no labels like "good player" or "attacker type" in the dataset.
So we let K-Means **discover the structure** automatically.

---

## 🔍 **Steps Followed**

### **1️⃣ Data Cleaning**

* Loaded FIFA dataset
* Removed unnecessary columns
* Fixed missing values
* Corrected data types



### **3️⃣ Feature Selection**

Selected only numeric attributes useful for clustering
(e.g., Pace, Shooting, Passing, Dribbling, Physical etc).


### **4️⃣ Dimensionality Reduction (PCA)**

* FIFA dataset has 100+ features
* PCA reduces it to 2 components
* Helps visualization
* Removes noise
* Makes clustering more accurate

---

### **5️⃣ Run the AI Model (K-Means)**

K-Means is an **unsupervised ML model** that groups similar items.
We tested different values of **k** using:

### ✔️ **Silhouette Score**

* +1 → perfect clusters
* 0 → overlapping
* −1 → bad clustering

We selected the number of clusters with the **best silhouette score**.

---

### **6️⃣ Visualization**

Plotted:

* PCA 2D scatter clusters
* Cluster centroids
* Attribute comparison charts

---

## 🏁 **Results**

* Players were grouped into meaningful clusters
* Clear separation between attacker-style and defender-style and a great seperation in goal keeper profiles
* PCA showed strong grouping based on key abilities
* Build a player recommendation engine

---

## 📦 **Tech Stack**

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-Learn (PCA, K-Means)**
* **Matplotlib / Seaborn**

---

## 📁 **Project Notebook**

All steps are demonstrated in the notebook:
`fifa_24_clustering.ipynb`

---

## 💡 **Future Improvements**

* Use DBSCAN for density-based clustering
* Try t-SNE / UMAP for better visualization
* Add a simple Streamlit web app

---


