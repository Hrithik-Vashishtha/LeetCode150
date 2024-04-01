def hIndex(citations):
    citations.sort(reverse=True)  # Sort citations in non-decreasing order
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index
citations = [0,1]
print(hIndex(citations))