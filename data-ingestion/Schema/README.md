# Schemas
Schema - is a descriprtion, a data about the data, or metadata. 

Difficult to comprehend Database content without schemas

# Ontologies
it deals with naming and defying things in your system. 
It also talks about relations between these things.

In computer science and databases, an ontology is a formal representation of knowledge within a specific domain. It provides a structured framework to define and describe entities, their properties, and the relationships between them.

# What should be in schema?
- description
    -  field "PGTN" described as Pick Up Guest Time
- types
    - int, float, text
- units
    - 1/10 of Celsius, MegaBytes, Kilobytes, milimeters, etc.
- constraints (limits)
    - lowest temp is -25, highest is 40 , etc
- inter field constarints
    - snow cannot be when temperature > 5c
- relations
    - one-to-one, one-to-many, many-to-many

# Schema changes

## Nonbraking changes
Just adding new fields, keeping old ones.
Questions to consider:
- what to do with the old data
- can you add new data?
- what are the default values?
- handling missing data


## Breaking changes
rename or delete fields; old data doesn't fit anymore

Harder to implement, require more planning

Need to prepare a plan, how to make schema changes.
Should write your code in a way that can handle missing fields, version data in your schema, and test everything, even trivial schema changes.

# Schema validations

If you have a schema, make sure to validate your data against it. 
as an example - we can validate schemas, that are defined as as named tuple, and list of functions for every field 
- max temperature must not be > 90
- min temperature < 60
- amount snow must be  int >= 0, etc.
- example in validator/weather.py (data is stored manually inside script itself)