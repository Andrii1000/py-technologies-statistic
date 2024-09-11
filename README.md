# py-technologies-statistics
This project allows you to analyze the job market on dou.ua.

## Installation
To get started with the project, clone the repository:

```bash
git clone https://github.com/Andrii1000/py-technologies-statistics.git
```
Create and activate the virtual environment:

```bash
python -m venv venv
```
For Linux/MacOS
```bash
source venv/bin/activate
```
For Windows
```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
+ Run the dou.ua website scraper and save the results to the vacancies.csv file:
```bash
scrapy crawl vacancies -O vacancies.csv
```

+ Use the Jupyter Notebook. Open the dou_analys.ipynb file and execute all code cells.

## Demo
***
![Top 15 required technologies for Python Dev on dou.ua vacancies](screenshots/top_15_tech.png)
***

![Top 10 companies by count of vacancies](screenshots/pie_plot_for_companyes.png)
***

![Top places for work by count of vacancies](screenshots/top_work_location.png)
***
![Count of vacancies by date](screenshots/num_vacancies_by_date.png)
***
![Count of vacancies by seniority level](screenshots/num_vac_by_seniority_level.png)
***