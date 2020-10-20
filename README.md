# -> JSON to CSV parser for virt-who raw data

**This is a small project that helps in parsing the raw json mapping collected by virt-who service into a human-readable csv format.**

1. Information about the files in this repository

    -  data.json          :   Example json data of virt-who parsed from raw virt-who output collected via `virt-who -od`.

    -  json_to_csv.py     :   Main python script to convert the json structure of Host-Guest mapping into a good CSV format.

    -  raw_to_json.sh     :   Script to extract the JSON data from raw virt-who output.

    -  result.csv         :   Example csv output by `json_to_csv.py`.

    -  virt-who-data.txt  :   Example raw `virt-who -od` data to test and work with.
    
    
2. How to use ?

    * Clone this repository.

