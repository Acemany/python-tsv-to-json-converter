from typing import Tuple, Dict
from json import loads
from sys import argv


def tsv_to_json(tsv: str) -> Tuple[Dict[str, str | int]]:
    return [{tsv.split("\n")[0].split("\t")[index]: float(word) if word.replace(".", "", 1).replace("-", "", 1).isdecimal() else word
             for index, word in enumerate(line.split("\t"))}
            for line in tsv.split("\n")[1:]]


def json_to_tsv(json: Tuple[Dict[str, str | int]]) -> Tuple[Tuple[str | int]]:
    return "\n".join(["\t".join(json[0].keys())] + ["\t".join([str(value)
                                                               for value in dict.values()])
                                                    for dict in json])


if __name__ == "__main__":
    with open(argv[1], "r", encoding="utf-8") as f:
        formnew = "tsv" if argv[1].split(".")[-1] == "json" else "json"
        with open(f"{argv[1].split(".")[0]}.{formnew}", "w", encoding="utf-8") as r:
            r.write(str(tsv_to_json(f.read()) if formnew == "json" else
                        json_to_tsv(loads(f.read()))).replace("'", '"'))
