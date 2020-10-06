# Usage

Set environment variables first:  
`export PYTHONPATH=$PYTHONPATH:path/to/package-import-test`.

Then run:  
```bash
for file in $(ls main/test*.py); do
    python3 $file
done

python3 -m main
```
