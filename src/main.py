import dump.dumper as d

ids = d.extract_ids()
dump = d.dump_ids(ids)
d.save_dump(dump)
