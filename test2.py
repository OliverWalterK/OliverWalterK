import pickle, all_url

with open("pickle.pkl", 'wb') as pickleFile:
    pickle.dump(all_url.expected_original_find_all_links, pickleFile)

with open("pickle.pkl", 'rb') as pickleFile:
    all_url = pickle.load(pickleFile)

print(all_url)