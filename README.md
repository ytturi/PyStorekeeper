# PyStorekeeper

A Python Backup tool for Databases and files. Dump, compress and unify your data in a single archive.

DB based backups with dump strategy.

## Configuration

Use the option `config ['-c' | '--config' <path>]` to import a configuration file (JSON) with all available configs.

Available configs:

- `verbose`: Level of verbosity, overrided by command-line parameter
  - `-1`: Nullify output
  - `0`: Default output
  - `1`: Sub-Command info (OK or ERROR)
  - `2`: Debug info (vars and Sub-Command logs)
  - `3`: Step-level info
- `paths`: List of paths (as strings) to archive
- `archive_compression`: 
  - `tar.type`: Use tar archiving with 'type' compression, where type can be:
    - `xz`
    - `gzip`
    - `bzip2`
