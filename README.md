# -> JSON to CSV parser for virt-who mapping data ( vCenter )

**This is a small project that helps in parsing the raw json mapping collected by virt-who service into a human-readable csv format.**

1. Information about the files in this repository

    -  data.json          :   Example json data of virt-who parsed from raw virt-who output collected via `virt-who -od`.

    -  json_to_csv.py     :   Main python script to convert the json structure of Host-Guest mapping into a good CSV format.

    -  raw_to_json.sh     :   Script to extract the JSON data from raw virt-who output.

    -  result.csv         :   Example csv output by `json_to_csv.py`.

    -  virt-who-data.txt  :   Example raw `virt-who -od` data to test and work with.
    
    
2. How to use ?

    * Clone this repository on Satellite or in the location where your virt-who data is present.
        ~~~
        # git clone https://github.com/sayan3296/virt_who_jsontocsv.git
        # cd virt_who_jsontocsv/
        ~~~
        
    * Enusre that the `virt-who-data.txt` file is present somewhere. It should be provided by customer or you can use `virt-who -od &> virt-who-data.txt` to collect the same.
    
    * Process the file in this way.
        ~~~
        # ./raw_to_json.sh /path/to/virt-who-data.txt &> data.json
        # ./json_to_csv.py -i data.json -o result.csv
        ~~~
        
    * Either open the file with excel\spreadsheet type of software or read it using following command.
        ~~~
        # cat result.csv | column -s',' -t | less
        ~~~

