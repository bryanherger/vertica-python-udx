-- Step 0: create a virtualenv and pip3 install geopy. Save the site-packages path to use in the DEPENDS below
-- Example using venv "geocode" created under /home/bryan/work: /home/bryan/work/geocode/lib/python3.9/site-packages
-- or, use the included mkgeopyvenv.sh to create under /tmp which works "as is" below...

-- Step 1: Create library
DROP LIBRARY IF EXISTS ReverseGeocodeFunctions CASCADE;
\set libfile '\''`pwd`'/ST_ReverseGeocode.py\''
CREATE LIBRARY ReverseGeocodeFunctions AS :libfile DEPENDS '/tmp/venv_geocode/lib/python3.9/site-packages' LANGUAGE 'Python';

-- Step 2: Create functions
CREATE FUNCTION reverseGeocode AS NAME 'reverseGeocode_factory' LIBRARY ReverseGeocodeFunctions;

-- Step 3: Use functions
-- 40.773408~-73.870676 (Bing) = LaGuardia Airport (Terminal B, I think), NYC, though remember that (lat,long) swap to (y,x) 
SELECT reverseGeocode(40.773408,-73.870676);
