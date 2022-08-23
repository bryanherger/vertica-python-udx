-- Step 1: Create library
\set libfile '\''`pwd`'/PyEncryptUDSF.py\''
CREATE LIBRARY PyAesScalarFunctions AS :libfile DEPENDS '/tmp/crypto/lib/python3.9/site-packages/' LANGUAGE 'Python';

-- Step 2: Create functions
CREATE FUNCTION aes_decrypt AS NAME 'aes_decrypt_factory' LIBRARY PyAesScalarFunctions;

-- Step 3: Test
SELECT aes_decrypt('e8PEhlVv2+nbY/YsU/8vSQ==');

-- Step 4: Clean up
DROP LIBRARY PyAesScalarFunctions CASCADE;
