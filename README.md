# Docker for nspdk

Repo for creating `NSPDK` features using `EDeN` in `Docker` with `python2`.

How create `NSPDK` descriptors:  
```console
$docker build -t nspdk_run .  
$docker run --rm -v /abs/path/on/local/machine:/usr/src/code/ nspdk_run -i input_file.txt  -c 3 -b 8 -o output_file.txt
```  
   
`-i` - input `smi`/`txt`-file. Input file structure:  `SMILES №1\n`   
`-c` - the complexity of the features extracted  
`-b` - the number of bits that defines the feature space size: |feature space|=2^nbits  
`-o` - output `txt`-file with nspdk descriptors. Output file structure: `descriptor for str №1 \n`

