# MBHP Provider Database Scraper

This repository contains Python scripts that scrape the Massachusetts Behavioral Health Partnership (MBHP) provider database, available at [https://www.masspartnership.com/](https://www.masspartnership.com/). The goal of this project is to make the provider database more accessible and easier to browse.

## Dependencies

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To scrape the provider database, run the following command:

```bash
python main.py
```

This will create a file called `data.jsonl` in the current directory.

Next run the following command to parse each JSON HTML line into structured data:

```bash
python parse.py
```

This will create a file called `processed.jsonl` in the current directory.
