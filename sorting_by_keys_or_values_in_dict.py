country_population={'USA':328_200_000,'France':67_000_000,'china':1_393_000_000}
print(sorted(country_population))
# in assending order:
print(sorted(country_population.items()))

sorted_by_key={k:v for k,v in sorted(country_population.items())}
print(sorted_by_key)

sorted_by_value={k:v for k,v in sorted (country_population.items(),key=lambda v: v[1])}
print(sorted_by_value)

# In decending order:
