"""
Quick helper tool for converting markdown tables into a format
usable by the Obsidian Dataview Plugin

To use, set `--table_path` to a markdown file containing a single
markdown table and no other content. Set `--name_col` as a column 
to be used for a file name. Finally, set `--output_dir` to a
location where a new directory containing the generated markdown
notes will be stored

This script will generate a new directory at `--output_dir`. Within
that directory will be a number of markdown files, each corresponding
to a row of the original markdown table. Other than the column
specified for file naming, the table values will now be represented
as YAML frontmatter.
"""

import pandas as pd
from io import StringIO
import yaml
from pathlib import Path
import argparse
import shutil


def strip_string(value):
    if isinstance(value, str):
        return value.strip()
    return value


def convert_md_pandas(file: str) -> pd.DataFrame:
    """
    Converts the input markdown file (with a table) into a pandas
    dataframe

    args:
    - file (str): the loaded content of the markdown note

    returns:
    df (pd.DataFrame) - DataFrame containing the contents of the markdown
    table
    """

    # ensure file contents are str
    table = StringIO(file)

    # read as csv with | as separator
    df = pd.read_csv(table, sep="|")

    # removes unncessary rows created by csv load
    df = df.drop(columns=["Unnamed: 0", f"Unnamed: {str(len(df.columns) - 2)}"])

    # drop the '| - |' row standard in .md tables
    df = df.drop(index=0)

    # strip all str values within the table
    df = df.map(strip_string)

    # rename columns (often contain extra spaces after conversion)
    for col in df.columns:
        df.rename(columns={col: col.strip()}, inplace=True)

    return df


def write_yaml(df: pd.DataFrame, name_col: str, dir: Path) -> None:
    """
    Converts each row of a dataframe to a dictionary and then
    writes a new Obsidian note with a specified column as the
    name of the note and the remaining contents of the row
    as YAML frontmatter (Properties)

    args:
    - df (pd.DataFrame): DataFrame containing markdown table content
    - name_col (str): Specific column in df to use as file name
    - dir (Path): directory to write new Obsidian notes
    """

    # if no directory is present create
    # else delete dir and create new one
    try:
        dir.mkdir()
    except FileExistsError:
        shutil.rmtree(dir)
        dir.mkdir()
    for _, row in df.iterrows():
        # row to dict
        data = row.to_dict()

        # generate filename and delete name column
        filename = f"/{data[name_col]}.md"
        del data[name_col]

        # yaml / frontmatter formatting
        yaml_data = yaml.dump(data, sort_keys=False)
        frontmatter = f"---\n{yaml_data}---\n"

        # write new note
        with open(dir + filename, "w") as f:
            f.write(frontmatter)
            f.write("\n")


def main(args) -> None:
    table_path = Path(args.table_path)

    with open(table_path, "r") as f:
        md_table = f.read()

    df = convert_md_pandas(md_table)

    output_dir = Path(args.output_dir)
    name_col = args.name_col

    write_yaml(df=df, name_col=name_col, dir=output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--table_path",
        type=str,
        required=True,
        help="Path to the Obsidian table markdown file",
    )
    parser.add_argument(
        "--name_col",
        type=str,
        required=True,
        help="Column name to use as the file name for the notes",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory to store newly generated .md files",
    )
    args = parser.parse_args()

    main(args)
