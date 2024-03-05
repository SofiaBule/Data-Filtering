# Filter dataset based on a condition
def filter_dataset(dataset, condition):
    return dataset[condition]

# Example usage:
filtered_data = filter_dataset(dataset, dataset['column'] > 100)
print(filtered_data.head())
