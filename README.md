# JSON schema for Umbrella Specification 

Umbrella is a tool for specifying comprehensive execution environments,
from the hardware all the way up to software and data. Please refer to http://ccl.cse.nd.edu/software/manuals/umbrella.html
for additional details.

Note that there are two types of Umbrella specifications: self-contained umbrella specification and umbrella 
specification which is attached to a Metadata Database. No attributes except for 
the the name are required in attached a Metadata Database spec. This JSON schema is
 for self-contained spec only. 

This JSON Schema (application/schema+json) has several purposes, one of which is JSON instance validation.

This project include the schema (json_schema.json) as well as set of tests to verify the validity of the schema (tests.py + examples in data directory)
