-- Step 1: Create library
\set libfile '\''`pwd`'/PyEncryptUDSF.py\''
CREATE LIBRARY PyAesScalarFunctions AS :libfile DEPENDS '/tmp/crypto/lib/python3.9/site-packages/' LANGUAGE 'Python';

-- Step 2: Create functions
CREATE FUNCTION aes_decrypt AS NAME 'aes_decrypt_factory' LIBRARY PyAesScalarFunctions;

-- Step 3: Test
SELECT aes_decrypt('e8PEhlVv2+nbY/YsU/8vSQ==');

-- Step 4: Timing
\timing
CREATE TABLE tempaestester (enc VARCHAR(100));
INSERT INTO tempaestester VALUES ('uWTpHwuMurTfMPHDVbRsI+ExHi3XxtIMNWN5m59ONA02rf2KVaxGAytlMJ/9CykL+c9ODvLGzD66ibXwvPF6xw==');
INSERT INTO tempaestester VALUES ('e8PEhlVv2+nbY/YsU/8vSQ==');
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
INSERT INTO tempaestester SELECT * FROM tempaestester;
SELECT COUNT(*) FROM tempaestester;
\o /dev/null
SELECT aes_decrypt(enc) FROM tempaestester;
SELECT aes_decrypt(enc) FROM tempaestester;
DROP TABLE tempaestester;

-- Step 5: Clean up
DROP LIBRARY PyAesScalarFunctions CASCADE;
