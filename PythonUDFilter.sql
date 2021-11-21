\set libfile '\''`pwd`'/PyJsonFilter.py\''
CREATE LIBRARY PyJsonLib AS :libfile LANGUAGE 'Python';

create filter PyJsonFilter AS name 'PyJsonFilterFactory' library PyJsonLib;

create table jsonSample (a int, b varchar, c_d int, c_e varchar);

COPY jsonSample from stdin with filter PyJsonFilter() parser fjsonparser();
{"a":1,"b":"foo","c":{"d":2,"e":"bar"}}
\.

select * from jsonSample;
drop table jsonSample;

drop library PyJsonLib cascade;

