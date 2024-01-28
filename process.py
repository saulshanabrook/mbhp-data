import json

from bs4 import BeautifulSoup
from rich.progress import track

ID_PREFIX = "MainContent_FindBHProvider1_DataList1_lbl"
ID_SUFFIX = "_0"

SPLIT_COLUMNS = ["SpecialInterests", "AgeCategories", "BoardCertification"]

with open("./data.jsonl", "r") as json_file:
    with open("processed.jsonl", "w") as outfile:
        for line in track(json_file.readlines()):
            root = BeautifulSoup(json.loads(line))
            for provider in root.find_all("p"):
                data: dict[str, str] = {
                    (NAME := attr.attrs["id"][len(ID_PREFIX) :].split("_")[0]): str(
                        attr.string
                    )
                    if NAME not in SPLIT_COLUMNS
                    else str(attr.string).split(", ")
                    for attr in provider.find_all(
                        "span", id=lambda x: x and x.startswith(ID_PREFIX)
                    )
                }
                print(json.dumps(data), file=outfile)
