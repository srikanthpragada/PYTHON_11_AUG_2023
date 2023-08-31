
def mismatch_pos(st1, st2):
    st2_len = len(st2)
    st1_len = len(st1)
    for idx, c in enumerate(st1):
        if idx >= st2_len:
            return idx
        elif c != st2[idx]:
            return idx

    if st1_len < st2_len:
        return st1_len
    else:
        return -1


print(mismatch_pos('abc', 'abc'))
print(mismatch_pos('abc', 'adc'))
print(mismatch_pos('abcdef', 'abc'))
print(mismatch_pos('abc', 'abcdef'))
print(mismatch_pos('abd', 'abcdef'))





