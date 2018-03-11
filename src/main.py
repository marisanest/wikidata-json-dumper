import dumper

ids = dumper.extract_ids()
dump = dumper.dump_ids(ids)
dumper.save_dump(dump)
