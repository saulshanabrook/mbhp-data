import json

from bs4 import BeautifulSoup
from rich.progress import track

ID_PREFIX = "MainContent_FindBHProvider1_DataList1_lbl"
ID_SUFFIX = "_0"


with open("./data.jsonl", "r") as json_file:
    with open("processed.jsonl", "w") as outfile:
        for line in track(json_file.readlines()):
            root = BeautifulSoup(json.loads(line))
            for provider in root.find_all("p"):
                data: dict[str, str] = {
                    attr.attrs["id"][len(ID_PREFIX) : -(len(ID_SUFFIX) + 1)]: str(
                        attr.string
                    )
                    for attr in provider.find_all(
                        "span", id=lambda x: x and x.startswith(ID_PREFIX)
                    )
                }
                print(json.dumps(data), file=outfile)
