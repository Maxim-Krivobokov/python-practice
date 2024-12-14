# Two types of getting access to the XML

DOM - document object model
 - everything is stored in memory

SAX - Simple API for XML
 - Iterative (good for big files)

Parsers:
 - ElementTree - the standart library
 - lxml - third party

Note:
everything in XML is text, so:
we need to make a conversion of all data fields(str to int, float or datetime)