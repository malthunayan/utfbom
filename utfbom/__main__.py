import argparse
import csv
import pathlib


def convert_to_utf8_sig(path: pathlib.Path) -> None:
    with open(path, "r+", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
        f.seek(0, 0)
        csv.writer(f).writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        "utfbom", description="Encode CSV files in UTF-8 with BOM"
    )
    parser.add_argument(
        "infiles",
        type=pathlib.Path,
        nargs="+",
        help="csv files to encode in UTF-8 with BOM",
    )
    args = parser.parse_args()
    for file in args.infiles:
        if file.suffix == ".csv":
            convert_to_utf8_sig(file)
        else:
            print(f"Expected CSV file, found {file}.")


if __name__ == "__main__":
    main()
