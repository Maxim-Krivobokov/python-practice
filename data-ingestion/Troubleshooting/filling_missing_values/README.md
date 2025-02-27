# Pandas 

pandas has methods to work with Null values.

- nan - Not a Number
- NaT - Not a Time

# Check that value is empty:
```python
pd.isnull(myvar) # equal True if myvar in nan, null, etc

# Check for pandas dataframe-object
values = pd.Series([1.2, 2.3, float('nan'), 4.5])
print(pd.isnull(values))   # [False, False, True, False]
```

# Filling missing data

```python
values = pd.Series([1., 2., np.nan, 4., 5., np.nan, 7.0])
print(values.fillna(5.))  # [1, 2, 5, 4, 5, 5, 7]
print(values.interpolate())  # [1, 2, 3, 4, 5, 6, 7] - Uses linear interpolation by default.
```