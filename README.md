# 🇦🇷 Argentina Job Market Analysis (Bumeran)

This project analyzes the Argentine job market based on over **13,000 real job listings** from [Bumeran.com.ar](https://www.bumeran.com.ar/).  
It covers the period between March and June 2025 and aims to extract insights about job trends, in-demand positions, regional differences, and the behavior of job postings on the platform.

## 📌 Objectives

- Clean and structure real-world job listing data.
- Classify diverse job titles into meaningful categories.
- Analyze the geographic and categorical distribution of job offers.
- Identify top roles in high-volume sectors like Sales and Administration.

## 🔍 Dataset

- Scraped from [bumeran.com.ar](https://www.bumeran.com.ar/) using **Selenium + BeautifulSoup**.
- Contains ~13,800 rows with fields such as:
  - `Puesto` (Job Title)
  - `Empresa` (Company)
  - `Ubicación` (Location)
  - `Link` (Posting URL)

> Note: Company names were often replaced with placeholders like "Updated X hours ago", which was handled during cleaning.

## 🧹 Data Cleaning

- Removed duplicates and null values.
- Normalized job titles (lowercased, accents removed).
- Replaced placeholder company names with `"Sin información"`.
- Grouped 9,300+ unique job titles into general categories using rule-based logic.

## 📊 Visualizations

The analysis includes:
- Top 10 provinces by number of job postings.
- Most frequent job categories.
- Company frequency by job volume.
- Top job titles in the Sales / Commercial sector.

You can see the PDF summary [https://github.com/Edelan89/Bumeran_Arg_job_market_analisys/blob/main/Bumeran_Arg_job_market_analisys.pdf](./Bumeran_Arg_job_market_analisys.pdf).
Or in HTML format [https://github.com/Edelan89/Bumeran_Arg_job_market_analisys/blob/main/Bumeran_Arg_job_market_analisys.html](./Bumeran_Arg_job_market_analisys.html).

## 📌 Key Insights

- **Buenos Aires** dominates the job market volume, followed by Córdoba and Santa Fe.
- The most frequent job category is **Sales / Commercial**.
- Many postings are made by companies that do not reveal their identity.
- Top Sales roles: *Asesor Comercial*, *Vendedor*, *Ejecutivo de Ventas*.

## 🚫 Limitations

- The dataset is biased toward Buenos Aires, which may not reflect the national market.
- Job title classification was rule-based and not NLP-driven (future improvement opportunity).
- Some fields like salary and posting dates were not available.

## 📚 Learnings

This project was a great opportunity to practice:
- Web scraping
- Data cleaning and categorization
- Exploratory data analysis (EDA)
- Communicating insights in English

## 🚀 Tools Used

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Selenium + BeautifulSoup (Scraping)
- Jupyter Notebook
- GitHub for version control and sharing

---

## 🧠 Author

**Maximiliano Mauricio Pérez Fernández**  
📍 Argentina  
💼 Data Analyst & Tech Explorer  
🔗 [LinkedIn](https://www.linkedin.com/in/maximiliano-mauricio-perez-fernandez-a24878a4/) | [Portfolio](https://github.com/Edelan89)

---

